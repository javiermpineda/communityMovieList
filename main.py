# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for
import requests
#import mysql.connector

# Flask app configuration
app = Flask(__name__, static_folder='static')


# MySQL database configuration
#db = mysql.connector.connect(
#    host="localhost",
#    user="your_username",
#    password="your_password",
#    database="movies_db"
#)
#cursor = db.cursor()

# Utelly API key
utelly_api_key = "7f574861edmshca8d93cf3a84ddep1e9cc8jsn73d42ccca55f"

# Home route - displays all available movies
@app.route('/')
def home():
    #This one defaults to 1 in case the URL does not specify it.
    page_number = request.args.get('page', 1, type=int)

    # Fetch movies from Utelly API
    utelly_endpoint = "https://moviesdatabase.p.rapidapi.com/titles/"

    headers = {
        "X-RapidAPI-Key": "7f574861edmshca8d93cf3a84ddep1e9cc8jsn73d42ccca55f",
        "X-RapidAPI-Host": "moviesdatabase.p.rapidapi.com"
    }

    # You might want to modify the parameters to search for specific contents
    #params = {
    #    "term": "wolf",
    #    "country": "us",
    #}
    #response = requests.get(utelly_endpoint, headers=headers, params=params)

    response = requests.get(utelly_endpoint, headers=headers)
    movies_data = response.json()
    print(movies_data)

    # Render the home template with the movies data
    return render_template('home.html', movies_data=movies_data, page_number=page_number)

# Favorites route - displays details of selected favorite movies
@app.route('/favorites')
def favorites():
    # Fetch favorites from the local database
    #cursor.execute("SELECT * FROM favorites")
    #favorites_data = cursor.fetchall()
    # Render the favorites template with the favorites data
    #return render_template('favorites.html', favorites_data=favorites_data)
    return ""

# Endpoint to add a movie to favorites
@app.route('/add_to_favorites/<movie_id>')
def add_to_favorites(movie_id):
    # Fetch movie details from the Utelly API based on the movie_id
    # You can customize this based on the Utelly API response structure
    # For example, assuming the movie title is present in the response
    #cursor.execute("INSERT INTO favorites (movie_id, movie_title) VALUES (%s, %s)", (movie_id, "Movie Title"))
    #db.commit()

    # Redirect back to the home page after adding to favorites
    return redirect(url_for('home'))

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
