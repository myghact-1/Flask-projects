import requests
from flask import Flask, render_template

app = Flask(__name__)


def get_biodata():
    url = "https://randomuser.me/api/"
    r = requests.get(url)
    res = r.json(encoding='latin')
    data = res['results'][0]

    biodata = {}

    gender = data['gender']
    title = data['name']['title']
    first_name = data['name']['first']
    last_name = data['name']['last']

    street_number = data['location']['street']['number']
    street_name = data['location']['street']['name']
    city = data['location']['city']
    state = data['location']['state']
    country = data['location']['country']
    post_code = data['location']['postcode']
    email = data['email']
    dob = data['dob']['date'].split('T')[0]
    age = data['dob']['age']
    phone = data['phone']
    cell = data['cell']
    image_url = data['picture']['large']

    biodata['gender'] = gender
    biodata['title'] = title
    biodata['first_name'] = first_name
    biodata['last_name'] = last_name
    biodata['street_number'] = street_number
    biodata['street_name'] = street_name
    biodata['city'] = city
    biodata['state'] = state
    biodata['country'] = country
    biodata['post_code'] = post_code
    biodata['email'] = email
    biodata['dob'] = dob
    biodata['age'] = age
    biodata['phone'] = phone
    biodata['cell'] = cell
    biodata['image_utl'] = image_url

    return biodata


@app.route("/", methods=['GET', 'POST'])
def home():
    biodata = get_biodata()
    return render_template('home.html', biodata=biodata)


if __name__ == "__main__":
    app.run(debug=True)
