from flask import render_template, make_response

from . import tracks_api, get_db

FIELDS_TO_FILTER = ['id', 'first_name', 'last_name']


@tracks_api.route("/count/")
def get_count_of_records():
    db = get_db()
    count = db.execute("SELECT COUNT(1) FROM tracks").fetchone()
    return make_response(f'<h1>Count of tracks - {count[0]}</h1>')


@tracks_api.route("/duration/")
def get_customers():
    db = get_db()
    tracks = db.execute("SELECT name, duration FROM tracks").fetchall()
    return render_template('tracks.html', tracks=tracks)
