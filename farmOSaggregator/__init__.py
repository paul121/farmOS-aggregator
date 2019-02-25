# Import Flask.
from flask import Flask

# Import Flask Admin.
from flask_admin import Admin

# Import default settings.
import farmOSaggregator.default_settings

# Create a Flask application.
app = Flask(__name__, instance_relative_config=True)

# Load configuration from defaults first, then override with a settings.py file
# inside the instance path.
app.config.from_object('farmOSaggregator.default_settings')
app.config.from_pyfile('settings.py', silent=True)

# Create a Flask Admin interface.
service_name = 'farmOS Aggregator'
admin = Admin(app, name=service_name, template_mode='bootstrap3', url='/')
