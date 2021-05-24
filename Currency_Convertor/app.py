import json
import configparser
import requests

from flask import Flask, render_template, request

app = Flask(__name__)


def get_details(path='response.json'):
    with open(path, encoding='latin') as f:
        data = json.load(f)
    currency_codes = [details['id'] for details in data['data']]
    currency_names = [details['name'] for details in data['data']]
    return currency_codes, currency_names


def get_api_key():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['currencyconverter']['api']


def get_converted_value(cfrom, cto, api):
    url = f"http://free.currconv.com/api/v7/convert?q={cfrom}_{cto}&compact=ultra&apiKey={api}"
    r = requests.get(url)
    return r.json()


@app.route('/')
def home():
    codes, names = get_details()
    code_name = dict(zip(codes, names))
    return render_template('home.html', code_name=code_name)


@app.route('/results', methods=['POST'])
def results():
    codes, names = get_details()
    amount = request.form['amount']
    currency_code_from = request.form['currency_code_from']
    currency_code_to = request.form['currency_code_to']
    cfrom_name = names[codes.index(currency_code_from)]
    cto_name = names[codes.index(currency_code_to)]
    api = get_api_key()
    data_dict = get_converted_value(
        currency_code_from, currency_code_to, api)

    result = [value for (key, value) in data_dict.items()][0]
    result = float(amount) * result
    return render_template('results.html', result=result, amount=amount, currency_code_from=currency_code_from,
                           currency_code_to=currency_code_to, cfrom_name=cfrom_name, cto_name=cto_name)


if __name__ == "__main__":
    app.run()
