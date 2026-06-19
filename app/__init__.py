import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

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
    return render_template('hobbies.html', title="Hobbies", url=os.getenv("URL"))
