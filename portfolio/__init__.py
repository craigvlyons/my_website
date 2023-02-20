from flask import Flask, abort, render_template

app = Flask(__name__)

projects = [
    {   
    "name": "Flask Image server",
    "thumb": "img/application.png",
    "hero": "img/application.png",
    "categories": ["Python", "Flask", "Dropzone", "HTML", "CSS"],
    "slug": "image_server",
    "prod": "deployment"
    },
    {   
    "name": "Solidworks Addin",
    "thumb": "img/solidworks.png",
    "hero": "img/solidworks.png",
    "categories": ["VB.NET", "SQL", "Solidworks API"],
    "slug": "solidworks",
    "prod": "deployment"
    },
]

slug_to_project = {project["slug"]: project for project in projects }

@app.route("/")
def home():
    return render_template("home.html", projects=projects)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/project/<string:slug>")
def project(slug):
    if slug not in slug_to_project:
        abort(404)
    return render_template(
        f"project_{slug}.html", 
        project=slug_to_project[slug]
        )

@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404
