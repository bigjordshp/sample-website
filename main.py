from flask import Flask, render_template

website = Flask(__name__,)

@website.route('/')
def home():
    return render_template("index.html")

if __name__ == "__main__":
    website.run(debug=True)