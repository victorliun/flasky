#####################################################################
## /config.py will be storing all the module configurations. 
## Here, the database is setup to use SQLite, because it's a very 
## convenient dev env database. Most likely /config.py won't be a 
## part of your repository and will be different on your test and 
## production servers.
#####################################################################

import os

#_basedir is a trick for you to get the folder where the script runs
_basedir = os.path.abspath(os.path.dirname(__file__))

# DEBUG indicates that it is a dev environment, you'll get the very
# helpful error page from flask when an error occurs.
DEBUG = True

# SECRET_KEY will be used to sign cookies. Change it and all your 
# users will have to login again.
SECRET_KEY = '?AAAAACRPIllxA7wvXjIE4'

# ADMINS will be used if you need to email information to the site 
# administrators.
ADMINS = frozenset(['youremail@yourdomain.com'])

# SQLALCHEMY_DATABASE_URI and DATABASE_CONNECT_OPTIONS are SQLAlchemy 
# connection options (hard to guess)
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(_basedir, 'app.db')
DATABASE_CONNECT_OPTIONS = {}

# THREAD_PAGE my understanding was 2/core... might be wrong :)
THREADS_PER_PAGE = 8

# CSRF_ENABLED and CSRF_SESSION_KEY are protecting against form post fraud
CSRF_ENABLED = True
CSRF_SESSION_KEY = "somethingimpossibletoguess"

# RECAPTCHA_* WTForms comes with a RecaptchaField ready to use... 
# just need to go to recaptcha website and get your public and private key.
RECAPTCHA_USE_SSL = False
RECAPTCHA_PUBLIC_KEY = '6LeYIbsSAAAAACRPIllxA7wvXjIE411PfdB2gt2J'
RECAPTCHA_PRIVATE_KEY = '6LeYIbsSAAAAAJezaIq3Ft_hSTo0YtyeFG-JgRtu'
RECAPTCHA_OPTIONS = {'theme': 'white'}