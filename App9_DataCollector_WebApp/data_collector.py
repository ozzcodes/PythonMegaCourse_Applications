from flask import Flask, render_template, request
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config(['SQLALCHEMY_DATABASE_'])
db = SQLAlchemy

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
        print(email, height)

        return render_template('success.html')


# Run main file (app) as a development package
if __name__ == "__main__":
    app.run(debug=True)
