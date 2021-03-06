__author__ = 'colinmoore-hill'


import os
basedir = os.path.abspath(os.path.dirname(__file__))

CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

OPENID_PROVIDERS = [
    {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
    {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}]

GRAPHENEdb = ""

# mail server settings
MAIL_SERVER = 'pop.gmail.com'
MAIL_PORT = 25
MAIL_USERNAME = 'itestedthis1'
MAIL_PASSWORD = 'itestedthis1'


# administrator list
ADMINS = ['itestedthis1@gmail.com']