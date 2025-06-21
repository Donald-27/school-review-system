  SHOOL REVIEW SYSTEM
This is a simple Flask web app that allows users to browse and review secondary schools. You can sign up, log in, and leave a review for a school. Admins can view all schools and reviews. Schools can also be filtered by things like region, type (boarding or day), and pathways (like STEM).

What this project does
Lets users register and log in

Allows users to see a list of schools

Lets users review schools

Admins can add, update, or delete schools

Admins can view all users and reviews

Technologies used
Python

Flask

Flask-SQLAlchemy

Flask-Migrate

Flask-CORS

SQLite (used for the database)

Pipenv (used for managing dependencies)

Step by Step Setup
run these commands from the root of the project, which is the school-review-system/ folder.

Step 1 - Clone the project
Open your terminal and run:

bash
Copy code
git clone
cd school-review-system
Step 2 - Install Pipenv 

pip install pipenv

Step 3 - Install project dependencies
Now that you're inside the project folder, install everything using pipenv:

pipenv install
Then activate the virtual environment:

Set Environment Variable
Still in the root folder, run:

  export FLASK_APP=server/app.py
This tells Flask where to find the main app.

Database Setup

Step 4 - Initialize the database
This only needs to be done once to set up migrations:
flask db init

Step 5 - Create your database schema (migrations)
After making sure flask db init ran without errors:

flask db migrate -m "initial migration"
flask db upgrade
This will create your SQLite database file (app.db).

Seeding the database
You can add some initial data like users, schools, and reviews.

Run this command from the root folder:

python server/seed.py
If it runs without errors, you now have some data in your database to work with.

Run the app
To start your Flask server, run:

python server/app.py
You should now see something like:
Running on http://localhost:5555
Open your browser and visit: http://localhost:5555/reviews or http://localhost:5555/schools

Testing the API
You can test routes like:

GET http://localhost:5555/users
GET http://localhost:5555/schools
POST http://localhost:5555/reviews

