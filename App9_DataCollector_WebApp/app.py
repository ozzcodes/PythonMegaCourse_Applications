# noinspection PyUnresolvedReferences,PyPackageRequirements
from send_email import send_email
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
import email

# Create the flask app
app = Flask(__name__)
POSTGRES = {
    'user': 'postgres',
    'pw': '0212181',
    'db': 'height_data',
    'host': 'localhost',
    'port': '5432',
}

# Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\
%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
SQLALCHEMY_TRACK_MODIFICATIONS = True
db = SQLAlchemy(app)


# Create a DB model with ability to pill results by certain criteria
class Result(db.Model):
    __tablename__ = 'data'

    id = db.Column(db.Integer, primary_key=True)
    email_ = db.Column(db.String(120), unique=True)
    height_ = db.Column(db.Integer)

    def __init__(self, email_, height_):
        self.email_ = email_
        self.height_ = height_

    def __repr__(self):
        return '<id {}>'.format(self.id)


migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()


# Create a root page for homepage
@app.route('/')
def index():
    return render_template('index.html')


# Landing page after rendering the index page request
@app.route('/success', methods=['POST'])
def success():
    if request.method == 'POST':
        email = request.form['email_name']
        height = request.form['height_name']
        send_email(email, height)
        print('email address:' + email, height + ' inches')

        if db.session.query(Result).filter(Result.email_ == email).count() == 0:
            # Create a data instance of the object class
            data = Result(email, height)

            # Add the data to the database and then commit it
            db.session.add(data)
            db.session.commit()

            # Calculation for average height
            average_height = db.session.query(func.avg(Result.height_)).scalar()
            average_height = round(average_height, 1)
            print(average_height)

            return render_template('success.html')
    return render_template('index.html',
                           text='Seems like the entered email address has already been used!')


# Run main file (app) as a development package
if __name__ == "__main__":
    app.run(debug=True)
