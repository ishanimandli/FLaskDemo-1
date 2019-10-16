"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']


@app.route("/")
def start_here():
    """Home page."""

    return '<!doctype html><html>Hi! This is the <a href="/hello">home page.</a></html>'


@app.route("/hello")
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          What's your name? <input type="text" name="person">
          <input type="submit" value="Submit"> <br/>
          Choose a compliment: <select name="compliment">
          <option value="awesome">Awesome</option>
          <option value="terrific">Terrific</option>
          </select><br/>
          Choose your favorite color:
          <input type="color" name="fav_color">
        </form>
      </body>
    </html>
    """


@app.route("/greet")
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    # compliment = choice(AWESOMENESS)

    compliment = request.args.get("compliment")
    color = request.args.get("fav_color")

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
        <style>

        </style>
      </head>
      <body style="color:{}">
        Hi, {}! I think you're {}!
        <a href ="/diss/{}"> Get to know more about you</a>
      </body>
    </html>
    """.format(color,player, compliment, player)
# Ishani you are awesome

@app.route("/diss/<player>")
def diss(player):

  

  compliment = choice(AWESOMENESS)

  return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        And <b>{}</b>, I think you're also {}!
        <a href ="/diss"> Get to know more about you</a>
      </body>
    </html>
    """.format(player, compliment)


if __name__ == "__main__":
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0", port="5000")
