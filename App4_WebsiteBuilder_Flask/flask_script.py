from flask import Flask

my_app = Flask(__name__)


# Create a root page for homepage
@my_app.route('/')
def home():
    return 'My website content here please!'


# Run main file (my_app) as a debugging script
if __name__ == "__main__":
    my_app.run(debug=True)
