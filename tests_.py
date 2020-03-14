from unittest import TestCase

from app import app
from models import db, Pet


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///test_adopt'
app.config['SQLALCHEMY_ECHO'] = False

# Make Flask errors be real errors, rather than HTML pages with error info
app.config['TESTING'] = True
app.config['WTF_CSRF_ENABLED'] = False


db.drop_all()
db.create_all()

class PetTests(TestCase):

    def setUp(self):
        self.pet = Pet(name="test_cat", species="Cat", age=2)
        
    def tearDown(self):
        Pet.query.delete()
        db.session.commit()
    
    def test_image(self):
        self.assertEqual(self.pet.set_image(), 'https://cdn3.f-cdn.com/ppic/3151051/logo/7139949/cat%20fb.jpg')

class FlaskTests(TestCase):

    def tearDown(self):
        Pet.query.delete()
        db.session.commit()
      

    def test_add_get(self):
        with app.test_client() as client:
            resp = client.get("/add")
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 200)
            self.assertIn('Add a Pet', html)
           

    def test_add_post(self):
        with app.test_client() as client:
            d = {"name": "test_dog", "species": "Dog", "age": 2}
            resp = client.post("/add", data=d, follow_redirects=True)
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 200)
            self.assertIn('test_dog is <b class= "text-success">Available!', html)

            # test if pet was added to database correctly
            pet = Pet.query.get(1)
            self.assertEqual(pet.name, "test_dog" )
            
    def test_edit_pet(self):
        self.pet = Pet(name="test_cat", species="Cat", age=2)
        db.session.add(self.pet)
        db.session.commit()
        with app.test_client() as client:
            d = {"name": "test_dog", "species": "Dog", "age": 2}
            resp = client.post("/edit_pet/2", data=d, follow_redirects=True)
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 200)
            self.assertIn('test_dog', html)

            # test if pet was updated in database correctly
            pet = Pet.query.get(2)
            self.assertEqual(pet.name, "test_dog" )

           

    