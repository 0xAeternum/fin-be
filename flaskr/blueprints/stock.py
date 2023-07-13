from flask import Blueprint
from flask import jsonify
from datetime import date, timedelta
import os
import requests

POLYGON_API_KEY = os.environ.get('POLYGON_API_KEY')

stock_bp = Blueprint('stock', __name__)

@stock_bp.route('/tickers/',  strict_slashes=False)
def get_tickers():
    tickers = __get_stock_tickers__()
    return tickers


@stock_bp.route('/<string:name>/')
def get_stock(name):
    print(name)
    stock_info = __get_stock_info__(name, date.today())
    return stock_info


@stock_bp.route('/aggregates/<string:name>/')
def get_stock_aggregate(name):
    today = date.today()
    five_days_ago = today - timedelta(days=30)

    agg = __get_stock_aggreates__(name, five_days_ago, today)
    return agg


@stock_bp.route('/status/')
def stock_market_status():
    status = __get_stock_market_status__()
    return status


def __get_stock_tickers__():
    tickers = requests.get(f'https://api.polygon.io/v3/reference/tickers?active=true&limit=100&apiKey={POLYGON_API_KEY}').json()
    return jsonify(tickers)

def __get_stock_info__(ticker, date):
    stock_info = requests.get(f'https://api.polygon.io/v3/reference/tickers/{ticker.upper()}?date={date}&apiKey={POLYGON_API_KEY}').json()
    print(stock_info)
    return jsonify(stock_info)

def __get_stock_aggreates__(ticker, from_date, to_date, timespan='day', multiplier=1):
    stock_aggregates = requests.get(f'https://api.polygon.io/v2/aggs/ticker/{ticker.upper()}/range/{multiplier}/{timespan}/{from_date}/{to_date}?adjusted=true&sort=asc&limit=120&apiKey={POLYGON_API_KEY}').json()
    return jsonify(stock_aggregates)

def __get_stock_market_status__():
    status = requests.get(f'https://api.polygon.io/v1/marketstatus/now?apiKey={POLYGON_API_KEY}').json()
    return jsonify(status)

def __get_stock_news(ticker):
    news = requests.get(f'').json()
    return jsonify(news)