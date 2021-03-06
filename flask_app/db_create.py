#Authors: Leo M. Holm & Axel Holm
#Coding: utf-8

from project import db, bcrypt
from project.models import Recipe, User, Ingredient
 
 
# drop all of the existing database tables
db.drop_all()
 
# create the database and the database table
db.create_all()

# insert user data
user1 = User('Axel', 'axl@holm.se', '2safe4me')
user2 = User('Tamim', 'ta@mim.se', '2safe4me')
user3 = User('Anton', 'an@ton.se', '2safe4me')
db.session.add(user1)
db.session.add(user2)
db.session.add(user3)

#admin
admin_user = User(username = 'Admin', email='lol@holm.se', password_plaintext='2safe4me', role='admin')
db.session.add(admin_user)

# insert ingredient data
ingredient1= Ingredient(name='Potatis', measurement_unit='Styck')
ingredient2= Ingredient(name='Matlagningsgrädde', measurement_unit='Deciliter')
ingredient3= Ingredient(name='Gul Lök', measurement_unit='Styck')
ingredient4= Ingredient(name='Röd Lök', measurement_unit='Styck')
ingredient5= Ingredient(name='Nötfärs', measurement_unit='Gram')
ingredient6= Ingredient(name='Cheddarost', measurement_unit='Gram')
ingredient7= Ingredient(name='Ryggbiff', measurement_unit='Gram')
ingredient8= Ingredient(name='Salt', measurement_unit='Gram')
ingredient9= Ingredient(name='Peppar', measurement_unit='Gram')
ingredient10= Ingredient(name='Soja', measurement_unit='Centiliter')
ingredient11= Ingredient(name='Olivolja', measurement_unit='Deciliter')
ingredient12= Ingredient(name='Rapsolja', measurement_unit='Deciliter')
ingredient13= Ingredient(name='Timjan', measurement_unit='Gram')
ingredient14= Ingredient(name='Basilika', measurement_unit='Gram')


# insert recipe data
recipe1 = Recipe(title='Hembakat surdegsbröd', description = 'Underbart hembakat surdegsbröd, luftigt och knaprigt precis som om du hade köpt det på ditt favorit bageri.', image_filename ='bread.jpeg', image_url="http://localhost:5000/static/img/bread.jpeg", user_id='4', is_public=True)
recipe2 = Recipe(title='Håll-käften-burgare', description = 'En burgare fit for a king, hoppas du tog med dig din aptit för denna burgaren kommmer du inte avsluta hungrig.', image_filename ='burgare.jpeg', image_url="http://localhost:5000/static/img/burgare_1.jpeg", user_id='4', is_public=True)
recipe3 = Recipe(title='Pannkakor', description = 'Luftiga amerikanska pannkakor, perfekta själva men häll på lite sirap eller sylt för en otrolig upplevelse.', image_filename ='pannkakor.jpeg', image_url="http://localhost:5000/static/img/pannkakor.jpeg", user_id='4', is_public=True)
recipe4 = Recipe(title='Churros', description = 'Hembakade churros med socker och kanel, vad kan vara bättre? Perfekt för snack eller ge till barn med sockersug.', image_filename ='churros.jpeg', image_url="http://localhost:5000/static/img/churros.jpeg", user_id='4', is_public=True)
recipe5 = Recipe(title='Bakad lax', description = 'Bakad lax, detta receptet kan du inte gå fel med. Precis som att sitta på fiskekrogen i Göteborg men njutningen att vara hemma', image_filename ='lax.jpeg', image_url="http://localhost:5000/static/img/lax.jpeg", user_id='4', is_public=True)
recipe6 = Recipe(title='Penne Arrabiata', description = 'Klassisk italienskt recept för en het pasta med alla ingredienser som gör Italien speciellt. Laga receptet några gånger och ta dina färdigheter till Rom och visa upp.', image_filename ='pennearrabiata.jpeg', image_url="http://localhost:5000/static/img/pennearrabiata.jpeg", user_id='4', is_public=True)
db.session.add(recipe1)
db.session.add(recipe2)
db.session.add(recipe3)
db.session.add(recipe4)
db.session.add(recipe5)
db.session.add(recipe6)

db.session.add(ingredient1)
db.session.add(ingredient2)
db.session.add(ingredient3)
db.session.add(ingredient4)
db.session.add(ingredient5)
db.session.add(ingredient6)
db.session.add(ingredient7)
db.session.add(ingredient8)
db.session.add(ingredient9)
db.session.add(ingredient10)
db.session.add(ingredient11)
db.session.add(ingredient12)
db.session.add(ingredient13)
db.session.add(ingredient14)

  
# commit the changes
db.session.commit()


