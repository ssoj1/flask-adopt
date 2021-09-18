"""Flask app for adopt app."""

from flask import Flask, flash, redirect, render_template
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///adopt"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "oh-so-secret"


connect_db(app)
db.create_all()

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)


@app.get("/")
def render_home():
    """Render the homepage"""
    pets = Pet.query.all()
    return render_template("pets.html", pets=pets)


@app.route("/add", methods=["GET", "POST"])
def add_pet():
    """Pet add form; handle adding."""

    form = AddPetForm()

    # breakpoint()
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data or None
        age = form.age.data
        notes = form.notes.data

        new_pet = Pet(name=name, species=species,
                      photo_url=photo_url, age=age, notes=notes)
        db.session.add(new_pet)
        db.session.commit()

        flash(f"Added {name}")
        return redirect("/")

    else:
        return render_template(
            "pet_form.html", form=form)


@app.route("/<int:pet_id>", methods=["GET", "POST"])
def edit_pet(pet_id):
    """Pet add form; handle adding."""

    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        photo_url = form.photo_url.data
        notes = form.notes.data
        available = form.available.data

        pet.photo_url = photo_url
        pet.notes = notes
        pet.available = available

        db.session.commit()

        flash(f"Updated {pet.name}")
        return redirect(f"/{pet_id}")

    else:
        return render_template(
            "pet_detail.html", form=form, pet=pet)
