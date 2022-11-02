"""
WSGI config for twitter project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

认准一手微信study322 其他均为翻录倒卖
九章来offer都有  需要的+我
课程目录
https://www.yuque.com/study001/xk/list


import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'twitter.settings')

application = get_wsgi_application()
