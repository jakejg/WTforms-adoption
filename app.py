
from flask import Flask, request, redirect, render_template, flash
from models import db, connect_db, Pet
from forms import AddPet, EditPet
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True


connect_db(app)
db.create_all()

from flask_debugtoolbar import DebugToolbarExtension
app.config['SECRET_KEY'] = "SECRET!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

@app.route('/')
def home_list():
    """Lists all pets"""

    pets = Pet.query.all()
    return render_template('home_list.html', pets=pets)
    


@app.route('/add', methods=["GET", "POST"])
def add_pet_form():
    """Show add pet form and handle new pet data"""

    form = AddPet()
    
    if form.validate_on_submit():
        pet_info = {key:val for key,val in form.data.items() if key != 'csrf_token'}
        new_pet = Pet(**pet_info)
        db.session.add(new_pet)
        db.session.commit()
        return redirect('/')
    else:
        return render_template('add_pet.html', form=form)

@app.route('/<int:pet_id>')
def show_pet_details(pet_id):
    """Show pet details"""

    pet = Pet.query.get_or_404(pet_id)
    return render_template('pet_details.html', pet=pet)

@app.route('/edit_pet/<int:pet_id>', methods=["GET", "POST"])
def edit_pet_form(pet_id):
    """Show edit pet form and handle updated data"""

    pet = Pet.query.get_or_404(pet_id)
    form = EditPet(obj=pet)
    
    if form.validate_on_submit():
        pet.name = form.name.data
        pet.photo_url = form.photo_url.data
        pet.age = form.age.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.add(pet)
        db.session.commit()
        return redirect(f'/{pet_id}')
    else:
        return render_template('edit_pet.html', form=form)

