# TODO: in the terminal available at the bottom menu bar,
# install the following packages: flask flask-wtf wtforms requests
import countries as countries
from flask import Flask, request, render_template
from flask_wtf import FlaskForm, form
from wtforms import SubmitField, SelectField, IntegerField, validators
import requests
import os
import json


app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(16).hex()

""" ----------- I - JSON DOCUMENTS ----------- """


def save_to_file(data, filename):
    with open(filename, 'w') as write_file:
        json.dump(data, write_file, indent=2)


def read_from_file(filename):
    with open(filename, 'r') as read_file:
        data = json.load(read_file)
    return data


# API METHODS

def request_key():
    apiDict = read_from_file("JSON_Files/api_key.json")
    return apiDict['key']


def request_top_artists(country_code, number_of_results):
    url = "https://api.musixmatch.com/ws/1.1/chart.artists.get?country={0}&page_size={1}&apikey={2}" \
        .format(country_code, number_of_results, request_key())
    response = requests.get(url).json()
    return response


def request_top_tracks(country_code, chart_name, number_of_results):
    url2 = "https://api.musixmatch.com/ws/1.1/chart.tracks.get?country={0}&chart_name={1}&page_size={2}&apikey={3}" \
        .format(country_code, chart_name, number_of_results, request_key())
    response2 = requests.get(url2).json()
    return response2


# FORMS

class Search(FlaskForm):
    chart = SelectField("chartType", choices=[
        ("top", "Top tracks by editorial chart"),
        ("hot", "Most viewed lyrics in the last 2 hours"),
        ("mxmweekly", "Most viewed lyrics in the last 7 days"),
        ("mxmweekly", "Most viewed new-released lyrics in the last 7 days")
    ])

    country = SelectField("countries", choices=["Afghanistan",
                                                "Aland Islands",
                                                "Albania",
                                                "Algeria",
                                                "American Samoa",
                                                "Andorra",
                                                "Angola",
                                                "Anguilla",
                                                "Antarctica",
                                                "Antigua and Barbuda",
                                                "Argentina",
                                                "Armenia",
                                                "Aruba",
                                                "Australia",
                                                "Austria",
                                                "Azerbaijan",
                                                "Bahamas",
                                                "Bahrain",
                                                "Bangladesh",
                                                "Barbados",
                                                "Belarus",
                                                "Belgium",
                                                "Belize",
                                                "Benin",
                                                "Bermuda",
                                                "Bhutan",
                                                "Bolivia, Plurinational State of",
                                                "Bonaire, Sint Eustatius and Saba",
                                                "Bosnia and Herzegovina",
                                                "Botswana",
                                                "Bouvet Island",
                                                "Brazil",
                                                "British Indian Ocean Territory",
                                                "Brunei Darussalam",
                                                "Bulgaria",
                                                "Burkina Faso",
                                                "Burundi",
                                                "Cambodia",
                                                "Cameroon",
                                                "Canada",
                                                "Cape Verde",
                                                "Cayman Islands",
                                                "Central African Republic",
                                                "Chad",
                                                "Chile",
                                                "China",
                                                "Christmas Island",
                                                "Cocos (Keeling) Islands",
                                                "Colombia",
                                                "Comoros",
                                                "Congo",
                                                "Congo, The Democratic Republic of the",
                                                "Cook Islands",
                                                "Costa Rica",
                                                "C\u00f4te d'Ivoire",
                                                "Croatia",
                                                "Cuba",
                                                "Cura\u00e7ao",
                                                "Cyprus",
                                                "Czech Republic",
                                                "Denmark",
                                                "Djibouti",
                                                "Dominica",
                                                "Dominican Republic",
                                                "Ecuador",
                                                "Egypt",
                                                "El Salvador",
                                                "Equatorial Guinea",
                                                "Eritrea",
                                                "Estonia",
                                                "Ethiopia",
                                                "Falkland Islands (Malvinas)",
                                                "Faroe Islands",
                                                "Fiji",
                                                "Finland",
                                                "France",
                                                "French Guiana",
                                                "French Polynesia",
                                                "French Southern Territories",
                                                "Gabon",
                                                "Gambia",
                                                "Georgia",
                                                "Germany",
                                                "Ghana",
                                                "Gibraltar",
                                                "Greece",
                                                "Greenland",
                                                "Grenada",
                                                "Guadeloupe",
                                                "Guam",
                                                "Guatemala",
                                                "Guernsey",
                                                "Guinea",
                                                "Guinea-Bissau",
                                                "Guyana",
                                                "Haiti",
                                                "Heard Island and McDonald Islands",
                                                "Holy See (Vatican City State)",
                                                "Honduras",
                                                "Hong Kong",
                                                "Hungary",
                                                "Iceland",
                                                "India",
                                                "Indonesia",
                                                "Iran, Islamic Republic of",
                                                "Iraq",
                                                "Ireland",
                                                "Isle of Man",
                                                "Israel",
                                                "Italy",
                                                "Jamaica",
                                                "Japan",
                                                "Jersey",
                                                "Jordan",
                                                "Kazakhstan",
                                                "Kenya",
                                                "Kiribati",
                                                "Korea, Democratic People's Republic of",
                                                "Korea, Republic of",
                                                "Kuwait",
                                                "Kyrgyzstan",
                                                "Lao People's Democratic Republic",
                                                "Latvia",
                                                "Lebanon",
                                                "Lesotho",
                                                "Liberia",
                                                "Libya",
                                                "Liechtenstein",
                                                "Lithuania",
                                                "Luxembourg",
                                                "Macao",
                                                "Macedonia, Republic of",
                                                "Madagascar",
                                                "Malawi",
                                                "Malaysia",
                                                "Maldives",
                                                "Mali",
                                                "Malta",
                                                "Marshall Islands",
                                                "Martinique",
                                                "Mauritania",
                                                "Mauritius",
                                                "Mayotte",
                                                "Mexico",
                                                "Micronesia, Federated States of",
                                                "Moldova, Republic of",
                                                "Monaco",
                                                "Mongolia",
                                                "Montenegro",
                                                "Montserrat",
                                                "Morocco",
                                                "Mozambique",
                                                "Myanmar",
                                                "Namibia",
                                                "Nauru",
                                                "Nepal",
                                                "Netherlands",
                                                "New Caledonia",
                                                "New Zealand",
                                                "Nicaragua",
                                                "Niger",
                                                "Nigeria",
                                                "Niue",
                                                "Norfolk Island",
                                                "Northern Mariana Islands",
                                                "Norway",
                                                "Oman",
                                                "Pakistan",
                                                "Palau",
                                                "Palestinian Territory, Occupied",
                                                "Panama",
                                                "Papua New Guinea",
                                                "Paraguay",
                                                "Peru",
                                                "Philippines",
                                                "Pitcairn",
                                                "Poland",
                                                "Portugal",
                                                "Puerto Rico",
                                                "Qatar",
                                                "R\u00e9union",
                                                "Romania",
                                                "Russian Federation",
                                                "Rwanda",
                                                "Saint Barth\u00e9lemy",
                                                "Saint Helena, Ascension and Tristan da Cunha",
                                                "Saint Kitts and Nevis",
                                                "Saint Lucia",
                                                "Saint Martin (French part)",
                                                "Saint Pierre and Miquelon",
                                                "Saint Vincent and the Grenadines",
                                                "Samoa",
                                                "San Marino",
                                                "Sao Tome and Principe",
                                                "Saudi Arabia",
                                                "Senegal",
                                                "Serbia",
                                                "Seychelles",
                                                "Sierra Leone",
                                                "Singapore",
                                                "Sint Maarten (Dutch part)",
                                                "Slovakia",
                                                "Slovenia",
                                                "Solomon Islands",
                                                "Somalia",
                                                "South Africa",
                                                "South Georgia and the South Sandwich Islands",
                                                "Spain",
                                                "Sri Lanka",
                                                "Sudan",
                                                "Suriname",
                                                "South Sudan",
                                                "Svalbard and Jan Mayen",
                                                "Swaziland",
                                                "Sweden",
                                                "Switzerland",
                                                "Syrian Arab Republic",
                                                "Taiwan, Province of China",
                                                "Tajikistan",
                                                "Tanzania, United Republic of",
                                                "Thailand",
                                                "Timor-Leste",
                                                "Togo",
                                                "Tokelau",
                                                "Tonga",
                                                "Trinidad and Tobago",
                                                "Tunisia",
                                                "Turkey",
                                                "Turkmenistan",
                                                "Turks and Caicos Islands",
                                                "Tuvalu",
                                                "Uganda",
                                                "Ukraine",
                                                "United Arab Emirates",
                                                "United Kingdom",
                                                "United States",
                                                "United States Minor Outlying Islands",
                                                "Uruguay",
                                                "Uzbekistan",
                                                "Vanuatu",
                                                "Venezuela, Bolivarian Republic of",
                                                "Viet Nam",
                                                "Virgin Islands, British",
                                                "Virgin Islands, U.S.",
                                                "Wallis and Futuna",
                                                "Yemen",
                                                "Zambia",
                                                "Zimbabwe"])
    numberResults = IntegerField("Quantity")
    number_of_results = [5, 10, 15, 20]
    submit = SubmitField("Submit")


# ROUTES

@app.route('/', methods=["GET", "POST"])
def index():
    form = Search(request.form)
    if request.method == "POST":
        selected_country = request.form["country"]
        number_of_results = request.form["numberResults"]
        top_artists = request_top_artists(selected_country, number_of_results)
        list_of_artists = []
        for i in top_artists["message"]["body"]["artist_list"]:
            artist = (i["artist"]["artist_name"], i["artist"]["artist_twitter_url"])
            list_of_artists.append(artist)

        selected_country = request.form["country"]
        selected_chart = request.form["chart"]
        number_of_results = request.form["numberResults"]
        top_tracks = request_top_tracks(selected_country, selected_chart, number_of_results)
        list_of_tracks = []
        for i in top_tracks["message"]["body"]["track_list"]:
            track_and_charts = (i["track"]["track_name"], i["track"]["artist_name"], i["track"]["track_share_url"])
            list_of_tracks.append(track_and_charts)

        return render_template('results.html', lst_artists=list_of_artists, list_of_tracks=list_of_tracks,
                               country=selected_country, quantity=number_of_results)
    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run(port=5050, debug=True)
