from flask import Flask, abort, render_template


def create_app():
    app = Flask(__name__)

    projects = [
        {   
        "name": "Places App",
        "thumb": "img/places_Screens1.png",
        "hero": "img/places_Screens2.png",
        "categories": ["Android", "SQLite", "Google API"],
        "slug": "places",
        "prod": "https://github.com/craigvlyons/PlacesApp.git"
        },
        {   
        "name": "Solidworks Addin",
        "thumb": "img/solidworks.png",
        "hero": "img/solidworks.png",
        "categories": ["VB.NET", "SQL", "Solidworks API"],
        "slug": "solidworks",
        "prod": ""
        },
        {   
        "name": "Flask Image server",
        "thumb": "img/application.png",
        "hero": "img/application.png",
        "categories": ["Python", "Flask", "Dropzone", "HTML", "CSS"],
        "slug": "image_server",
        "prod": "https://github.com/craigvlyons/Flask-image-server.git"
        },        
        {   
        "name": "Job Tracker",
        "thumb": "img/computer.png",
        "hero": "img/plotlyDashboard.png",
        "categories": ["Python", "SQL", "Dash", "Plotly", "HTML", "CSS"],
        "slug": "job_tracker",
        "prod": ""
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

    return app