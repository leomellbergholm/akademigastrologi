from project import db
from project.models import Recipe, User
 
 
# drop all of the existing database tables
db.drop_all()
 
# create the database and the database table
db.create_all()

# insert user data
user1 = User('axl@holm.se', '2safe4me')
user2 = User('ta@mim.se', '2safe4me')
user3 = User('an@ton.se', '2safe4me')
db.session.add(user1)
db.session.add(user2)
db.session.add(user3)

#admin
admin_user = User(email='lol@holm.se', password_plaintext='2safe4me', role='admin')
db.session.add(admin_user) 

# insert recipe data
recipe1 = Recipe('Hembakat surdegsbröd', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris arcu ex, lacinia ac venenatis a, dictum a mi. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis.', admin_user.id, True)
recipe2 = Recipe('Håll-käften-burgare', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris arcu ex, lacinia ac venenatis a, dictum a mi. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis.', admin_user.id, True)
recipe3 = Recipe('Pasta Carbonara', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris arcu ex, lacinia ac venenatis a, dictum a mi. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis.', admin_user.id, True)
db.session.add(recipe1)
db.session.add(recipe2)
db.session.add(recipe3)


  
# commit the changes
db.session.commit()


