from flask import *
from flask_session import Session
from Database import books,book_titles, authors, types, image_links, descriptions, prices, stars, reviews_1, reviews_2, sellers, stocks


app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False #So this session has a default time limit of some number of minutes or hours or days after which it will expire.
app.config["SESSION_TYPE"] = "filesystem" #It will store in the hard drive (these files are stored under a /flask_session folder in your config directory.) or any online ide account, and it is an alternative to using a Database or something else like tha
Session(app)

USERS = {
            "tirthraj2004@gmail.com":["Tirthraj", "tirthraj123"],
            "amey@gmail.com":["Amey","amey123"],
            "danish@gmail.com":["Danish", "danish123"],
            "irfan@gmail.com":["Irfan","irfan123"]
        }

def validateUser(email,password):
    if email not in USERS.keys():
        return False

    # print(USERS[email])
    if USERS[email][1] == password:
        return True
    return False

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/loginpage')
def renderLogin():
    return render_template("login1.html")

@app.route('/selectcollege')
def renderClgPage():
    if not session.get("email"):
        return redirect("/loginpage")
    return render_template("selectcollege.html")

@app.route('/selectClg', methods=["POST"])
def renderClg():
    college = request.form.get('college')
    return render_template('marketplace.html',college=college)

@app.route('/seller')
def seller():
    return render_template('seller.html')   

@app.route('/<int:num>')
def book(num):
    book = books[num]
    print("Current Book",book)
    return render_template('./bookpage.html', book = book )

@app.route('/checkout')
def checkout():
    return render_template('checkout.html')

@app.route('/login', methods=["POST"])
def login():
    email = request.form.get("email")
    password = request.form.get("password")

    #Validation
    if validateUser(email,password):
        session["email"] = request.form.get("email")
        session["password"] = request.form.get("password")
        return render_template("index.html",login='true')
    else:
        error = "Incorrect Credentials"
        return render_template("login1.html",error=error)


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=81)
