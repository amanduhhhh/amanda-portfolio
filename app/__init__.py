import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

about_paragraphs = [
    "I'm a CS + Co-op student at the University of Waterloo. I've built countless "
    "full-stack applications, from web apps for crochet pattern design to patient "
    "portals used in real health centres!",
    "I'm also an absolute puzzle fiend. Be it minesweeper, crosswords, or 90's point "
    "and click adventure games (LucasArts especially), if I'm not coding, I've got my "
    "head buried in one of these.",
]

current_work = [
    "Currently a platform developer for Hack The North!",
    "Completing a Ubisoft mentorship, where I'll be developing a game under industry leadership.",
    "Served as Waterloo's Campus Crusade for Cheese president. I've since committed to "
    "sampling one new cheese every week. Saint Albray's is a recent favourite.",
    "From May–December 2025, completed a software internship at Oak Ridges Heart Centre, "
    "where I built an AI clinic scribe, a food portion size model, and a mobile app, "
    "amongst other things.",
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
    return render_template(
        'index.html',
        title="Amanda Xi",
        url=os.getenv("URL"),
        about_paragraphs=about_paragraphs,
        current_work=current_work,
    )


@app.route('/hobbies')
def hobbies():
    return render_template('hobbies.html', title="Hobbies", url=os.getenv("URL"))
