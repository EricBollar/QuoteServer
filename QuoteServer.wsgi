#flaskapp.wsgi
import sys
sys.path.insert(0, '/var/www/html/QuoteServer')

from app import app as application
