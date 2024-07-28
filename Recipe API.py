
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data/recipes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Recipe(db.Model):
    __tablename__ = 'recipes'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    ingredients = db.Column(db.Text, nullable=False)
    instructions = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Recipe {self.title}>'

@app.route('/recipes', methods=['GET'])
def get_recipes():
    recipes = Recipe.query.all()
    recipe_list = [{
        'id': recipe.id,
        'title': recipe.title,
        'ingredients': recipe.ingredients,
        'instructions': recipe.instructions,
        'image_url': recipe.image_url,
        'created_at': recipe.created_at
    } for recipe in recipes]
    return jsonify(recipe_list)

@app.route('/recipes/<int:id>', methods=['GET'])
def get_recipe(id):
    recipe = Recipe.query.get_or_404(id)
    return jsonify({
        'id': recipe.id,
        'title': recipe.title,
        'ingredients': recipe.ingredients,
        'instructions': recipe.instructions,
        'image_url': recipe.image_url,
        'created_at': recipe.created_at
    })

@app.route('/recipes', methods=['POST'])
def create_recipe():
    data = request.get_json()
    new_recipe = Recipe(
        title=data['title'],
        ingredients=data['ingredients'],
        instructions=data['instructions'],
        image_url=data.get('image_url', None)
    )
    db.session.add(new_recipe)
    db.session.commit()
    return jsonify({'message': 'Recipe created successfully'}), 201

@app.route('/recipes/<int:id>', methods=['PUT'])
def update_recipe(id):
    recipe = Recipe.query.get_or_404(id)
    data = request.get_json()
    recipe.title = data['title']
    recipe.ingredients = data['ingredients']
    recipe.instructions = data['instructions']
    recipe.image_url = data.get('image_url', None)
    db.session.commit()
    return jsonify({'message': 'Recipe updated successfully'})

@app.route('/recipes/<int:id>', methods=['DELETE'])
def delete_recipe(id):
    recipe = Recipe.query.get_or_404(id)
    db.session.delete(recipe)
    db.session.commit()
    return jsonify({'message': 'Recipe deleted successfully'})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

