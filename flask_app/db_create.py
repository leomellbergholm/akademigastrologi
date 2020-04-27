from project import db
from project.models import Recipe
 
 
# drop all of the existing database tables
db.drop_all()
 
# create the database and the database table
db.create_all()
 
# insert recipe data
recipe1 = Recipe('Hembakat surdegsbröd', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris arcu ex, lacinia ac venenatis a, dictum a mi. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis.')
recipe2 = Recipe('Håll-käften-burgare', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris arcu ex, lacinia ac venenatis a, dictum a mi. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis.')
recipe3 = Recipe('Pasta Carbonara', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris arcu ex, lacinia ac venenatis a, dictum a mi. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis.')
db.session.add(recipe1)
db.session.add(recipe2)
db.session.add(recipe3)
 
# commit the changes
db.session.commit()