from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from Url_shortener.hash import calculateHash


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{path}Url.db'
app.config['SQLALCHEMY_TRACK_MODIFCATIONS'] = False

db = SQLAlchemy(app)
# used for first request
initialized = False


class Url(db.Model):
    id_ = db.Column("id_", db.Integer, primary_key=True)
    longurl = db.Column("longurl", db.String())
    shorturl = db.Column("shorturl", db.String())

    def __init__(self, longurl, shorturl):
        self.longurl = longurl
        self.shorturl = shorturl


@app.before_request
def initialize():
    global initialized
    if not initialized:
        # Code to be executed before the first request
        db.create_all()
        initialized = True


@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == "POST":
        longurlinput = request.form["url_inp"]
        urlexist = Url.query.filter_by(longurl=longurlinput).first()
        if urlexist:
            return redirect(url_for("display_short_url", urlinput=urlexist.shorturl))
        else:
            shorturlinput = calculateHash(longurlinput)
            new_input_url = Url(longurlinput, shorturlinput)
            db.session.add(new_input_url)
            db.session.commit()
            return redirect(url_for("display_short_url", urlinput=shorturlinput))
    else:
        return render_template('home.html')


@app.route('/display/<urlinput>')
def display_short_url(urlinput):
    return render_template('shorturl.html', shorturlvalue=urlinput)


@app.route('/<short_url>')
def redirection(short_url):
    longurlvalue = Url.query.filter_by(shorturl=short_url).first()
    if longurlvalue:
        return redirect(longurlvalue.longurl)
    else:
        return f'<h1>Url doesnt exist</h1>'


if(__name__ == '__main__'):
    app.run(port=5000, debug=True)
