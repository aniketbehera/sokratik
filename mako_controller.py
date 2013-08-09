#!/usr/bin/python
#
#   Author:  Conan Albrecht <ca&byu,edu>
#   License: Public Domain
#   Version: 2011.12.02
#
__doc__ = '''
                                      DESCRIPTION
                             
  NOTE: I wrote an extended HOWTO on this module at http://warp.byu.edu/site/content/907.
  See that link for a detailed walkthrough in setting up Django, Apache, and Mako.                           
                                      
  An extension to Django to use Mako templates rather than the built-in Django templates.  Why
  use Mako instead of Django's built-in template language?  Because while most of Django is
  wonderful, the template language is weak sauce.  In fact, Django shamelessly points out that
  it keeps the template language simple to encourage developers to use views for functionality.
  I agree that logic should be kept to views, but I already have to learn HTML, Javascript, JQuery,
  Python, Django, and a host of other languages to make this all work.  Now they want to throw
  another language into the mix--for no other reason than to encourage me to behave?  No thanks.
  
  Mako is strong sauce: it uses Python itself for the templating language.  All the power and ease 
  of Python, right within the web page.  And Mako integrates with Django easily.  This module
  is the glue that binds Django and Mako together in one happy family..

  In particular, this module provides the following two things:  
  
  1. Defines the MakoTemplateRenderer object, which runs a Mako template.  Any view function
     can call this method to render a template.  Example views.py:

     import mako_controller
     templater = mako_controller.MakoTemplateRenderer('thisappname')  # only need one of these per app
     
     def myview(request, urlparams):
       # a bunch of processing here
       # now render the template called "mytemplate.html", sending paramA and paramB as variables
       return templater.render(request, 'mytemplate.html', { 'paramA': 'asdf', 'paramB': 0 })

     If all you want to do is use Mako for your Django templating and do everything else the Django way, 
     you can stop reading here.  The above code makes it work.  #2 below is only a shortcut that makes
     calling views easier -- with it, you can shorten your urls.py file.

  2. Defines the HtmlPageServer class, which serves any view and any template file.  Django normally
     requires that every page in the program have a urls.py entry.  This is stupid, since a simple
     notation can call pages automatically from a controller like this.  To enable
     this, add the following to your urls.py file for each app (change appname to your app name):
  
     from mako_controller import HtmlPageServer
     urlpatterns = patterns('',
       (r'^appname/(?P<path>.*\.html)(?P<funcname>!.*?)?(?P<urlparams>/.*)?$',
     )

     This matches any URL containing .html, such as http://www.mysite.com/myapp/somepage.html.
     You can use any extension here or even have multiple extensions like this:
     
       (r'^account/(?P<path>.*\.(html|htm|css))(?P<funcname>!.*?)?(?P<urlparams>/.*)?$',
     
     URLs are provided in /appname/pagename.html!funcname/param1/param2/param3/ format.  This has three parts:
       - The path name is everything up to the .html (per the regex in urls.py). The path name specifies the
         module look in.  Any periods in the path name are replaced with underscores (since Python doesn't allow 
         periods in module or function names).
       - The function to call is specified after the exclamation point.  This is optional.  If no exclamation point 
         and function name are given, the standard function 'process_request' is called in the module.  If an 
         exclamation point and function name are given, process_request_functionname is called.  The static string 
         'process_request' is added to the front of the function name for security. That way module functions are 
         protected from access via the web except those explicitly made available with a name starting with process_request.
       - Parameters can be provided, separated by slashes.  These parameters are placed in a list and sent to the view/page
         in the 'urlparams' variable.  These are an alternative to standard, named parameters (name=value),
         and they are purely for asthetics -- these type of parameters just make URLs prettier.

     Following are some examples of URLs and their processing:
     
       /appname/pagename.html!funcname/1/2/3/4/
         Module    = views/pagename_html.py
         Function  = process_request_funcname(request, [ '1', '2', '3', '4', ''])
                     If this module or function is not found, templates/pagename.html is rendered through Mako.
         
       /appname/pagename.css
         Module    = views/pagename_css.py
         Function  = process_request(request, [])
                     If this module or function is not found, templates/pagename.css is rendered through Mako.
                     (this assume you have an entry in urls.py to send .css files this way)
                     
       /appname/pagename.html/abc/def?name1=val1&name2=val2
         Module    = views/pagename_html.py
         Function  = process_request(request, [ 'abc', 'def' ])
                     If this mdoule or function is not found, templates/pagename.html is rendered through Mako.
                     { 'name1': 'val1', 'name2': 'val2' } is available via request.GET like normal
        
  3. Requirements: the following need to be in settings.py:
  
       # The root folder of the entire site (where settings.py lives)
       import os.path
       SITE_ROOT = os.path.dirname(os.path.realpath(__file__))

       # identifies where the Mako templates are stored relative to each app (it's a subdir of a given app dir)
       MAKO_CONTROLLER_TEMPLATES_DIR = 'templates'
       
       # identifies where the Django view files are stored relative to each app (it's a subdir of a given app dir)
       MAKO_CONTROLLER_VIEWS_DIR = 'views'

       # identifies where the Mako template cache will be stored.  There's only one cache directory per project.
       # template cache files are not stored within the app directories because they just clutter things up.
       MAKO_CONTROLLER_TEMPLATES_CACHE_DIR = 'template_cache/applications/'

       # the default page to render in Mako when no path is given by the browser
       MAKO_DEFAULT_HTML_PAGE = 'index.html'  
     
'''

from django.template import RequestContext
from django.http import HttpResponse, Http404, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.conf import settings
from django.utils.importlib import import_module
from django.core.urlresolvers import get_mod_func
from mako.exceptions import TopLevelLookupException, html_error_template
from mako.lookup import TemplateLookup
import sys, os, os.path, urllib
import logging; log = logging.getLogger('django')

class HtmlPageServer:
  '''A class that serves any html page.  It prevents us from having to list each request in urls.py'''
  
  def __init__(self, app_path):
    '''@app_path: the application directory, relative to the location of mako_controller.py. If you put mako_controller.py in your project root, this is just the application name.
    '''
    # set up our renderer
    self.app_path = app_path
    self.templater = MakoTemplateRenderer(app_path)
    
  def __call__(self, request, path=None, funcname=None, urlparams=None):
    '''The URL resolver for a given app calls the object through this method.'''
    # if empty url, default to the index page
    if not path:
      path = settings.MAKO_DEFAULT_HTML_PAGE

    # prepare the function name and parameters
    funcname = funcname and funcname[1:] or '' # remove the leading ! and ensure a string
    parameters = urlparams and [ urllib.unquote(s) for s in urlparams[1:].split('/') ]  or [] # [1:] to remove the leading and convert to list
    
    # first try going to the view function for this request
    # we look for a views/name.py file where name is the same name as the HTML file
    response = None
    function_name = 'process_request' + (funcname and ('_' + funcname) or '')
    # see if we have a view and function with these names
    full_module_name = '.'.join([ self.app_path, settings.MAKO_CONTROLLER_VIEWS_DIR, path.replace('.', '_').replace('/', '.') ])
    # this next line assumes that mako_controller.py is one level below the settings.py file (hence the '..')
    module_filename = os.path.normpath(os.path.join(settings.SITE_ROOT, self.app_path, settings.MAKO_CONTROLLER_VIEWS_DIR, path.replace('.', '_') + '.py'))
    if os.path.exists(module_filename):
      __import__(full_module_name)
      module_obj = sys.modules[full_module_name]
      if hasattr(module_obj, function_name):
        try: 
          # we have a process_request() in views/page.py, so process the request
          response = getattr(module_obj, function_name)(request, parameters)
        except RedirectException, e: # redirect to another page
          if e.permanent:
            return HttpResponsePermanentRedirect(e.redirect_to)
          return HttpResponseRedirect(e.redirect_to)
          
    # render the html page if we didn't get an HttpResponse
    if response == None:
      response = self.templater.render(request, path, { 'urlparams': parameters } )
  
    # return the response
    return response  


###############################################################
###   render_template functionality (calls Mako templates)

class TemplateException(Exception):
  '''A template exception while rendering Mako templates'''
  def __init__(self, error, message):
    self.error = error
    Exception.__init__(self, message)


class RedirectException(Exception):
  '''Immediately stops processing of a view function or template and redirects to the given page.
     Note that this exception only works when urls.py routes the call through the classes in this
     module.  Django should have shipped with this one.  Perhaps it takes a little too much liberty
     with exceptions, but it makes returning from a huge call stack really nice.'''
  def __init__(self, redirect_to, permanent=False):
    self.redirect_to = redirect_to
    self.permanent = permanent


class MakoTemplateRenderer:
  '''Renders Mako templates'''
  def __init__(self, app_path):
    '''Creates a renderer to the given path (relateive to the project root where settings.STATIC_ROOT points to)'''
    project_path = os.path.normpath(settings.SITE_ROOT)
    self.app_path = app_path
    self.app_template_root = os.path.abspath(os.path.join(project_path, self.app_path, settings.MAKO_CONTROLLER_TEMPLATES_DIR))
    self.cache_root = os.path.abspath(os.path.join(project_path, settings.MAKO_CONTROLLER_TEMPLATES_CACHE_DIR, app_path)) # reversed from app_template_dir because the template cache files are all under one root (to keep app dirs uncluttered)
    self.tlookup = TemplateLookup(directories=[ self.app_template_root ], module_directory=self.cache_root, collection_size=2000)

    
  def render(self, request, template, urlparams):
    '''Runs a template and returns an HttpRequest object to it. 
    
       @request  The context request from Django
       @template The template file path to render.  This is relative to the app_path/MAKO_CONTROLLER_TEMPLATES_DIR/ directory.
                 For example, to render app_path/templates/page1.html, set template="page1.html", assuming you have
                 set up the variables as described in the documentation above.
       @urlparams   A dictionary of name=value variables to send to the template page.
       
    '''
    # Django's RequestContext automatically runs all the TEMPLATE_CONTEXT_PROCESSORS and populates with variables
    context = RequestContext(request,urlparams)
    response = HttpResponse()
    context_dict = { 'response': response }  # this allows the template to add cookies or headers to the response object
    # must convert the request context to a real dict to use the ** below
    for d in context:
      context_dict.update(d)
    # render the response with the given template and params
    try:
      template_obj = self.tlookup.get_template(template)
      if not hasattr(template_obj, 'template_path'):
        template_obj.template_path = template
      if not hasattr(template_obj, 'mako_template_renderer'):  # if the first time, add a reference to this renderer object
        template_obj.mako_template_renderer = self
      content = template_obj.render(**context_dict)
      response.write(content)
      return response
    except TopLevelLookupException: # template file not found    
      raise Http404()
    except RedirectException, e: # redirect to another page
      if e.permanent:
        return HttpResponsePermanentRedirect(e.redirect_to)
      return HttpResponseRedirect(e.redirect_to)




































