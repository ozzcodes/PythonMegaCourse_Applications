from flask import Flask, render_template

my_app = Flask(__name__)


# Create a root page for homepage
@my_app.route('/')
def home():
    return render_template('home.html')


# Example root to an about page (although not currently linked)
@my_app.route('/about/')
def about():
    return render_template('about.html')


# Run main file (my_app) as a development package
if __name__ == "__main__":
    my_app.run(debug=True)
