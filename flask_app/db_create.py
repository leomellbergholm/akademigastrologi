#Authors: Leo M. Holm & Axel Holm
#Coding: utf-8

from project import db, bcrypt
from project.models import Recipe, User
 
 
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

# insert recipe data
recipe1 = Recipe(title='Hembakat surdegsbröd', description = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris arcu ex, lacinia ac venenatis a, dictum a mi. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis.', image_filename ='bread.jpeg', image_url="http://localhost:5000/static/img/burgare_1.jpeg", user_id='1', is_public=True)
recipe2 = Recipe(title='Håll-käften-burgare', description = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris arcu ex, lacinia ac venenatis a, dictum a mi. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis.', image_filename ='burgare.jpeg', image_url="http://localhost:5000/static/img/burgare_1.jpeg", user_id='1', is_public=True)
recipe3 = Recipe(title='Pannkakor', description = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris arcu ex, lacinia ac venenatis a, dictum a mi. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis.', image_filename ='pannkakor.jpeg', image_url="http://localhost:5000/static/img/burgare_1.jpeg", user_id='1', is_public=True)
recipe4 = Recipe(title='Churros', description = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris arcu ex, lacinia ac venenatis a, dictum a mi. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis.', image_filename ='churros.jpeg', image_url="http://localhost:5000/static/img/burgare_1.jpeg", user_id='1', is_public=True)
recipe5 = Recipe(title='Bakad lax', description = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris arcu ex, lacinia ac venenatis a, dictum a mi. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis.', image_filename ='lax.jpeg', image_url="http://localhost:5000/static/img/burgare_1.jpeg", user_id='1', is_public=True)
recipe6 = Recipe(title='Penne Arrabiata', description = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris arcu ex, lacinia ac venenatis a, dictum a mi. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis.', image_filename ='pennearrabiata.jpeg', image_url="http://localhost:5000/static/img/burgare_1.jpeg", user_id='1', is_public=True)
db.session.add(recipe1)
db.session.add(recipe2)
db.session.add(recipe3)
db.session.add(recipe4)
db.session.add(recipe5)
db.session.add(recipe6)

  
# commit the changes
db.session.commit()


