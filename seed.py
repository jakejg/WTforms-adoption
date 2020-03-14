from models import Pet
from app import app, db

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
Pet.query.delete()

# Add pets
cat1 = Pet(name="Wiskers", species="Cat", photo_url="https://cdn.pixabay.com/photo/2019/11/08/11/56/cat-4611189__340.jpg", age="1", notes="Wiskers is a wonderful cat!", available=True)
dog1 = Pet(name="Todd", species="Dog", photo_url="https://www.sciencemag.org/sites/default/files/styles/inline__450w__no_aspect/public/pearl_16x9.jpg?itok=Tq-dVV3X", age="3", notes="Todd is a great Dog!", available=True)
rabbit1 = Pet(name="Muffins", species="Rabbit", photo_url="https://cdn.shopify.com/s/files/1/0078/8575/0369/products/Cute_Rabbit_Diamond_Painting_300x300.jpg?v=1571713794", age="2", notes="Muffins is a cute Rabbit!", available=False)


# Add new objects to session, so they'll persist
db.session.add_all([cat1, dog1, rabbit1])

# Commit--otherwise, this never gets saved!
db.session.commit()
