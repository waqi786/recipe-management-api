# Recipe API

This project is a simple RESTful API for managing recipes using Flask and SQLAlchemy. The API allows users to create, read, update, and delete recipes. It also supports Cross-Origin Resource Sharing (CORS) to enable interaction with the API from different domains.

## Features
- **Retrieve all recipes**: Get a list of all recipes in the database.
- **Retrieve a single recipe**: Get details of a specific recipe by ID.
- **Create a new recipe**: Add a new recipe to the database.
- **Update an existing recipe**: Modify details of an existing recipe.
- **Delete a recipe**: Remove a recipe from the database.

## Endpoints
### Get All Recipes
- **URL**: `/recipes`
- **Method**: `GET`
- **Response**: JSON array of recipes.

### Get Recipe by ID
- **URL**: `/recipes/<int:id>`
- **Method**: `GET`
- **Response**: JSON object of the specified recipe.

### Create Recipe
- **URL**: `/recipes`
- **Method**: `POST`
- **Request Body**: JSON object with `title`, `ingredients`, `instructions`, and optionally `image_url`.
- **Response**: Message indicating successful creation.

### Update Recipe
- **URL**: `/recipes/<int:id>`
- **Method**: `PUT`
- **Request Body**: JSON object with updated `title`, `ingredients`, `instructions`, and optionally `image_url`.
- **Response**: Message indicating successful update.

### Delete Recipe
- **URL**: `/recipes/<int:id>`
- **Method**: `DELETE`
- **Response**: Message indicating successful deletion.

## Installation

1. **Clone the repository**:
   ```sh
   git clone https://github.com/waqi786/recipe-api.git
   cd recipe-api

2.Create and activate a virtual environment:

    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. Install the required dependencies:

    pip install -r requirements.txt

4. Set up the database:

    flask db upgrade

5. Run the application:

    flask run

**Dependencies:**

1. Flask
2. Flask-SQLAlchemy
3. Flask-CORS

Install the dependencies using the command:

    pip install flask flask_sqlalchemy flask_cors

**Database**

The application uses SQLite as the database. The database file is located at data/recipes.db. The Recipe model has the following fields:

id: Integer, primary key.
title: String, required.
ingredients: Text, required.
instructions: Text, required.
image_url: String, optional.
created_at: DateTime, default is the current UTC time.


**Usage**
Example Request to Get All Recipes

    curl -X GET http://127.0.0.1:5000/recipes

    curl -X POST http://127.0.0.1:5000/recipes -H "Content-Type: application/json" -d '{
      "title": "Pancakes",
      "ingredients": "Flour, Milk, Eggs, Sugar, Baking Powder",
      "instructions": "Mix all ingredients and cook on a hot griddle.",
      "image_url": "http://example.com/image.jpg"
    }'

**Contribution**
Feel free to fork this repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

**Developed by Waqar Ali.**

This README provides a detailed overview of the project, including installation steps, endpoint documentation, and example usage. It should help others understand the purpose of your project and how to get started with it.

Uploaded Date:

7/27/2024

