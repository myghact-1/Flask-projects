import requests
from flask import Flask, render_template, request

app = Flask(__name__)


def get_data(url="http://www.boredapi.com/api/activity"):
    r = requests.get(url)
    res = r.json()
    return res


@app.route('/', methods=['GET', 'POST'])
def home():
    data = get_data()
    activity = data['activity']
    return render_template('home.html', activity=activity)


# @app.route('/results', methods=['POST'])
# def results():
#     data = get_data()
#     activity = data['activity']
#     return render_template('results.html', activity=activity)


if __name__ == "__main__":
    app.run()
