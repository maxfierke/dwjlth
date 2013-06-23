"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/

This file creates your application.
"""

import re
import os
import pprint
from flask import Flask, make_response, render_template, request, redirect, url_for, json, jsonify

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'this_should_be_configured')

restaurants_handle = open('data/restaurants.json', 'r')
restaurants = json.load(restaurants_handle)
###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html', restaurants=restaurants)


@app.route('/search')
def search():
    restaurant = request.args.get('q', '', type=str)
    if restaurant == '':
        return make_response('', 400)

    verdict = acquire_verdict(restaurant)
    if verdict is not False:
        return jsonify(restaurant=verdict)
    return page_not_found('')


def acquire_verdict(restaurant):
    """Get the verdict for the requested restaurant"""
    for key, value in restaurants.iteritems():
        if re.match(key, restaurant, flags=re.IGNORECASE):
            return value
    return False


###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
