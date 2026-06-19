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

experiences = [
    {
        "role": "Production Engineering",
        "org": "Meta & Major League Hacking",
        "dates": "Jun 2026 – Present",
        "description": "Building and operating full-stack projects through the MLH Production Engineering Fellowship.",
    },
    {
        "role": "ML Engineering",
        "org": "AI4Good Lab",
        "dates": "Apr 2026 – Present",
        "description": "Created Sensa, a pregnancy and period tracker designed for individuals with low vision.",
    },
    {
        "role": "Frontend Developer",
        "org": "Hack the North",
        "dates": "Feb 2026 – Present",
        "description": "Developing hackthenorth.com and museum.hackthenorth.com.",
    },
    {
        "role": "Software Developer",
        "org": "UW Blueprint",
        "dates": "Jan 2026 – May 2026",
        "description": "Built software for the Oakville and Milton Humane Society.",
    },
    {
        "role": "Develop at Ubisoft Mentee",
        "org": "Ubisoft",
        "dates": "Oct 2025 – May 2026",
        "description": "Developing a game under industry mentorship, working in C++ and algorithms.",
    },
    {
        "role": "Software Engineer",
        "org": "Oak Ridges Heart Clinic",
        "dates": "May 2025 – Jan 2026",
        "description": "Built an AI clinic scribe, a full-stack patient portal, and a cross-platform mobile app.",
    },
]

education = [
    {
        "program": "BCS, Computer Science (Co-op)",
        "school": "University of Waterloo",
        "dates": "Expected 2029",
    },
]

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

locations = [
    {"name": "Toronto, ON", "lat": 43.6532, "lng": -79.3832},
    {"name": "Waterloo, ON", "lat": 43.4643, "lng": -80.5204},
    {"name": "Montreal, QC", "lat": 45.5019, "lng": -73.5674},
    {"name": "New York City, NY", "lat": 40.7128, "lng": -74.0060},
    {"name": "Los Angeles, CA", "lat": 34.0522, "lng": -118.2437},
    {"name": "Charlottetown, PEI", "lat": 46.2382, "lng": -63.1311},
    {"name": "Halifax, NS", "lat": 44.6488, "lng": -63.5752},
    {"name": "Fredericton, NB", "lat": 45.9636, "lng": -66.6431},
    {"name": "Beijing, China", "lat": 39.9042, "lng": 116.4074},
]

pages = [
    {"name": "Home", "endpoint": "index"},
    {"name": "Hobbies", "endpoint": "hobbies"},
    {"name": "Travel", "endpoint": "travel"},
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
        experiences=experiences,
        education=education,
    )


@app.route('/hobbies')
def hobbies():
    return render_template(
        'hobbies.html',
        title="Hobbies",
        url=os.getenv("URL"),
        hobbies=hobbies_list,
    )


@app.route('/travel')
def travel():
    return render_template(
        'travel.html',
        title="Travel",
        url=os.getenv("URL"),
        locations=locations,
    )
