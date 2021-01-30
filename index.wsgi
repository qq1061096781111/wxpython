# _*_ coding: utf-8 _*_

import os
import sae
import web
from weixin import WeixinInterface

url = (
'/weixin','WeixinInterface'

)

app_root = os.path.dirname(__file__)
templates_root = os.path.join(app_root,'templates')
render = web.template.render(templates_root)

app = web.application(urls,globals()).wsgifunc()
application = sae.create_wsgi_app(app)