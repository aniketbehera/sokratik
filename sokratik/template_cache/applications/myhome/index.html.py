# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 8
_modified_time = 1375652865.790428
_enable_loop = True
_template_filename = u'/home/pupun/sokratik/sokratik/myhome/templates/index.html'
_template_uri = u'index.html'
_source_encoding = 'ascii'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<!DOCTYPE html>\n<html class=" js cssanimations" lang="en"><head><script src="/home/sokratik/sokratik/myhome/static/js/user_timeline.json" async=""></script>\n<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">\n<title>Scaffold responsive website template</title>\n<meta name="viewport" content="width=device-width, initial-scale=1.0">\n<meta name="description" content="">\n<meta name="author" content="">\n<link href="/home/sokratik/sokratik/myhome/static/css/bootstrap.css" rel="stylesheet">\n<link href="/home/sokratik/sokratik/myhome/static/css/bootstrap-responsive.css" rel="stylesheet">\n<link href="/home/sokratik/sokratik/myhome/static/css/docs.css" rel="stylesheet">\n<link href="/home/sokratik/sokratik/myhome/static/css/prettyPhoto.css" rel="stylesheet">\n<link href="/home/sokratik/sokratik/myhome/static/css/prettify.css" rel="stylesheet">\n<link href="/home/sokratik/sokratik/myhome/static/css/flexslider.css" rel="stylesheet">\n<link href="/home/sokratik/sokratik/myhome/static/css/style.css" rel="stylesheet">\n<link href="/home/sokratik/sokratik/myhome/static/css/success.css" rel="stylesheet">\n<script src="/home/sokratik/sokratik/myhome/static/js/jquery-1.js"></script>\n<script src="/home/sokratik/sokratik/myhome/static/js/jquery_004.js"></script>\n<script src="/home/sokratik/sokratik/myhome/static/js/prettify.js"></script>\n<script src="/home/sokratik/sokratik/myhome/static/js/modernizr.js"></script>\n<script src="/home/sokratik/sokratik/myhome/static/js/bootstrap.js"></script>\n<script src="/home/sokratik/sokratik/myhome/static/js/jquery_003.js"></script>\n<script src="/home/sokratik/sokratik/myhome/static/js/jquery_005.js"></script>\n<script src="/home/sokratik/sokratik/myhome/static/js/jquery.js"></script>\n<script src="/home/sokratik/sokratik/myhome/static/js/jquery_002.js"></script>\n<script src="/home/sokratik/sokratik/myhome/static/js/application.js"></script>\n<!--[if (gte IE 6)&(lte IE 8)]>\n<script src="selectivizr.js"></script>\n<![endif]-->\n<!-- Portfolio hover -->\n<script src="/home/sokratik/sokratik/myhome/static/js/jquery-hover-effect.js"></script>\n<script src="/home/sokratik/sokratik/myhome/static/js/setting.js"></script>\n<script src="/home/sokratik/sokratik/myhome/static/js/custom.js"></script>\n<!-- fav and touch icons -->\n<link rel="shortcut icon" href="/home/sokratik/sokratik/myhome/static/images/favicon.ico">\n<link rel="apple-touch-icon-precomposed" sizes="144x144" href="/home/sokratik/sokratik/myhome/static/images/apple-touch-icon-144-precomposed.png">\n<link rel="apple-touch-icon-precomposed" sizes="114x114" href="/home/sokratik/sokratik/myhome/static/images/apple-touch-icon-114-precomposed.png">\n<link rel="apple-touch-icon-precomposed" sizes="72x72" href="/home/sokratik/sokratik/myhome/static/images/apple-touch-icon-72-precomposed.png">\n<link rel="apple-touch-icon-precomposed" href="/home/sokratik/sokratik/myhome/static/images/apple-touch-icon-57-precomposed.png">\n</head>\n<body>\n<header>\n<!-- Navbar\n================================================== -->\n<div class="navbar navbar-fixed-top">\n\t<div class="navbar-inner">\n\t\t<div class="container" style="padding-bottom:15px">\n\t\t\t<!-- logo -->\n\t\t\t<a class="brand logo" href="/index.html">\n\t\t\t<img src="/home/sokratik/sokratik/myhome/static/images/logo.png" alt="">\n\t\t\t</a>\n\t\t\t<!-- end logo -->\n\t\t\t<!-- top menu -->\n\t\t\t<div>\n\t\t\t\t<nav>\n\t\t\t\t<ul class="nav topnav">\n\t\t\t\t\t<div class="btn-toolbar cta" style="padding-top:5px;padding-bottom:5px;height:20px">\n\t\t\t\t\t\t\t<a class="btn btn-large btn-danger" href="#"><i style="font-size:12.5px;height:12px"></i> Signup ')
        # SOURCE LINE 57
        __M_writer(unicode(2+2))
        __M_writer(u'</a>\n\t\t\t\t\t\t\t<a class="btn btn-large btn-success" href="#"><i style="font-size:12.5px;height:12px"></i> Login</a>\n\t\t\t\t\t\t</div>\n\t\t\t\t\t\n\t\t\t\t</ul>\n\t\t\t\t</nav>\n\t\t\t</div>\n\t\t\t<!-- end menu -->\n\t\t</div>\n\t</div>\n</div>\n</header>\n<section id="intro">\n<div class="jumbotron masthead">\n\t<div class="container" style="margin-top:-20px">\n\t\t<div class="row">\n\t\t\t<div class="span12">\n\t\t\t\t<!-- Place somewhere in the <body> of your page -->\n\t\t\t\t<div id="mainslider" class="flexslider">\n\t\t\t\t\t\n\t\t\t\t<ul class="slides"><li data-thumb="/home/sokratik/sokratik/myhome/static/images/img4.jpg">\n\t\t\t\t\t\t<img src="/home/sokratik/sokratik/myhome/static/images/img4.jpg" alt="">\n\t\t\t\t\t\t<div class="flex-caption danger">\n\t\t\t\t\t\t\t<h2>Lot of features</h2>\n\t\t\t\t\t\t\t<h4>Lorem ipsum dolor sit amet vix ceteros noluisse intellegat</h4>\n\t\t\t\t\t\t</div>\n\t\t\t\t\t\t</li>\n\t\t\t\t\t\t<li data-thumb="/home/sokratik/sokratik/myhome/static/images/img1.jpg">\n\t\t\t\t\t\t<img src="/home/sokratik/sokratik/myhome/static/images/img1.jpg" alt="">\n\t\t\t\t\t\t<div class="flex-caption primary">\n\t\t\t\t\t\t\t<h2>Twitter bootstrap</h2>\n\t\t\t\t\t\t\t<h4>Lorem ipsum dolor sit amet vix ceteros noluisse intellegat</h4>\n\t\t\t\t\t\t</div>\n\t\t\t\t\t\t</li>\n\t\t\t\t</ul></div>\n\t\t\t</div>\n\t\t</div>\n\t</div>\n</div>\n</section>\n<footer class="footer">\n<div class="container">\n\t<div class="row">\n\t\t<div class="span1.5" style="height:20px">\n\t\t\t<h5>About Us</h5>\n\t\t</div>\n\t\t<div class="span1.5" style="height:20px">\n\t\t\t<h5>Terms of Service</h5>\n\t\t</div>\n\t\t<div class="span1.5" style="height:20px">\n\t\t\t\t<h5>Privacy policy</h5>\n\t\t</div>\n\t\t<div class="span6" style="height:20px">\n\t\t\t\t<h5></h5>\n\t\t</div>\n\t\t<div class="span1.5" style="height:20px">\n\t\t\t\t<h5></h5>\n\t\t</div>\n\t\t<div class="span1.5" style="height:20px">\n\t\t\t\t<h5>Built on <a>edX</a></h5>\n\t\t</div>\n\t\t\n\t</div>\n</div>\n</footer>\n<script>\n(function(){\n// Append a close trigger for each block\n$(\'.box-tile .content\').append(\'<span class="close">x</span>\');\n// Show window\nfunction showContent(elem){\nhideContent();\nelem.find(\'.content\').addClass(\'expanded\');\nelem.addClass(\'cover\');\n}\n// Reset all\nfunction hideContent(){\n$(\'.box-tile  .content\').removeClass(\'expanded\');\n$(\'.box-tile  li\').removeClass(\'cover\');\n}\n// When a li is clicked, show its content window and position it above all\n$(\'.box-tile  li\').click(function() {\nshowContent($(this));\n});\n// When tabbing, show its content window using ENTER key\n$(\'.box-tile  li\').keypress(function(e) {\nif (e.keyCode == 13) {\nshowContent($(this));\n}\n});\n// When right upper close element is clicked  - reset all\n$(\'.box-tile  .close\').click(function(e) {\ne.stopPropagation();\nhideContent();\n});\n// Also, when ESC key is pressed - reset all\n$(document).keyup(function(e) {\nif (e.keyCode == 27) {\nhideContent();\n}\n});\n})();\n</script>\n</body>\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()

