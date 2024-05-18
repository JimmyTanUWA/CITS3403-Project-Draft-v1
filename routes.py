from app import flaskApp, db
from flask import render_template, redirect, flash, url_for
from app.models import movie 

@flaskApp.route('/')
def index():
    tags = db.session.query(movie.tag).distinct().all()
    movies = movie.query.all()
    return render_template('original.html', movies=movies, tags=tags)

@flaskApp.route('/moviedetails/<name>')
def moviedetails(name):
    # Query the movie by its name
    movieD = movie.query.filter_by(name=name).first_or_404()  # This will return 404 if no movie is found
    return render_template('moviedetails.html', movieD=movieD)

@flaskApp.route('/movietag/<tag>')
def movietag(tag):
    movieT = movie.query.filter_by(tag=tag).all()  # Fetch all movies with the given tag
    return render_template('movietag.html', movieT=movieT)

