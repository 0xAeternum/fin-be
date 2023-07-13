from flask import Flask
from flask_cors import CORS
from blueprints.stock import stock_bp
import requests


POLYGON_API_KEY = '9m27Z4BYAYdp0TZABtH5cHztk30RLyCt'


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

app.config.from_mapping(
        SECRET_KEY='dev',
        #DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

app.register_blueprint(stock_bp, url_prefix='/stock')


app.run(host='0.0.0.0', port=3001)