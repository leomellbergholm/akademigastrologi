#Authors: Leo M. Holm & Axel Holm
#Coding: utf-8

#################
#### imports ####
#################
 
from flask import render_template, Blueprint, request, flash, redirect, url_for, jsonify
from project.models import Recipe, User, Ingredient, IngredientSchema
from .Forms import AddRecipeForm
from project import db, images
from flask_login import LoginManager, login_required, login_user, current_user, logout_user
from flask_uploads import UploadSet, IMAGES, configure_uploads


################
#### config ####
################
 
recipes_blueprint = Blueprint('recipes', __name__) 
 
################
#### routes ####
################
@recipes_blueprint.route('/')
def index():
    all_public_recipes = Recipe.query.filter_by(is_public=True)
    return render_template('index.html', public_recipes=all_public_recipes)

@recipes_blueprint.route('/public')
def public_recipes():
    all_public_recipes = Recipe.query.with_entities(Recipe.id, Recipe.recipe_title, Recipe.recipe_description).filter_by(is_public=True)
    return render_template('public_recipes.html', public_recipes=all_public_recipes)

@recipes_blueprint.route('/add', methods=['GET', 'POST'])
@login_required
def add_recipe():
    form = AddRecipeForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            filename = images.save(request.files['recipe_image'])
            url = images.url(filename)
            new_recipe = Recipe(form.recipe_title.data, form.recipe_description.data, current_user.id, form.is_public.data, filename, url)
            db.session.add(new_recipe)
            db.session.commit()
            flash('New recipe, {}, added!'.format(new_recipe.recipe_title), 'success')
            return redirect(url_for('recipes.user_recipes'))
        else:
            #flash_errors(form)
            flash('ERROR! Recipe was not added.', 'error')
    else:
        
        return render_template('add_recipe.html', form=form)

@recipes_blueprint.route('/ingredientlist', methods=['GET'])
@login_required
def get_ingredients():
    ingredient_list = Ingredient.query.all()
    ingredient_schema = IngredientSchema(many=True)
    output = ingredient_schema.dump(ingredient_list)
    return jsonify({'ingredients' : output})

@recipes_blueprint.route('/recipes')
@login_required
def user_recipes():
    all_user_recipes = Recipe.query.filter_by(user_id=current_user.id)
    return render_template('user_recipes.html', user_recipes=all_user_recipes)



@recipes_blueprint.route('/recipe/<recipe_id>')
def recipe_details(recipe_id):
    recipe_with_user = db.session.query(Recipe, User).join(User).filter(Recipe.id == recipe_id).first()
    if recipe_with_user is not None:
        if recipe_with_user.Recipe.is_public:
            return render_template('recipe_detail.html', recipe=recipe_with_user)
        else:
            if current_user.is_authenticated and recipe_with_user.Recipe.user_id == current_user.id:
                return render_template('recipe_detail.html', recipe=recipe_with_user)
            else:
                flash('Error! Incorrect permissions to access this recipe.', 'error')
    else:
        flash('Error! Recipe does not exist.', 'error')
    return redirect(url_for('recipes.public_recipes'))