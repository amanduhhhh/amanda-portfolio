import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

hobbies_list = [
    {
        "name": "Whittling",
        "description": "Recently got started whittling. Here's a silly cat I made!",
        "images": ["img/whittling_1.jpg", "img/whittling_2.jpg"],
    },
    {
        "name": "Drawing",
        "description": "I've been drawing for ~10 years! Some fanart for games I like:",
        "images": ["img/art_1.jpg", "img/art_2.jpg"],
    },
]

pages = [
    {"name": "Home", "endpoint": "index"},
    {"name": "Hobbies", "endpoint": "hobbies"},
]


@app.context_processor
def inject_pages():
    """Make the nav page list available to every template."""
    return {"pages": pages}


@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"))


@app.route('/hobbies')
def hobbies():
    return render_template(
        'hobbies.html',
        title="Hobbies",
        url=os.getenv("URL"),
        hobbies=hobbies_list,
    )
