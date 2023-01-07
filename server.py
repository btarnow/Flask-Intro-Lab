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

#route
#Add a link (<a>) to the HTML returned by the / route so that when you click the link, you’re taken to /hello.
# W3 Schools <a> example: <a href="https://www.w3schools.com">Visit W3Schools.com!</a>
@app.route('/')
#view function -a function that returns a web response 
def start_here():
    """Home page."""

    return "<!doctype html><html>Hi! This is the home page.<a href='/hello'> Hello!</a></html>"

#route
# allow the user to select a compliment from a radio button
#<input type="radio">
@app.route('/hello')
#view function- a function that returns a web response 
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

        <div>
          <form action="/greet">
            What's your name? <input type="text" name="person">

            <input type="submit" value="Submit">
          </div>

          <div>
            Choose a compliment:
            <input type = "radio" name="compliment" value="awesome">
            <label>Awesome</lable>
            <input type = "radio" name="compliment" value="cool">
            <label>Cool</lable>
            <input type = "radio" name="compliment" value="Fantastic">
            <label>Fantastic</lable>
          </div>
          
        </form>
      </body>
    </html>
    """

#route
@app.route('/greet')
#view function -a function that returns a web response
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return f"""
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're {compliment}!
      </body>
    </html>
    """


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
