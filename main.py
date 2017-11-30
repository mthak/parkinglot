import requests
from flask import Flask, render_template
import gettext
from flask_ask import (
                       Ask,
                       request as ask_request,
                       session as ask_session,
                       statement,
                       question as ask_question
                       )


app = Flask(__name__)
ask = Ask(app, "/")
ASK_APPLICATION_ID = "amzn1.ask.skill.00125890-0644-49fd-a5dd-2825979440a5"
app.config['ASK_VERIFY_REQUESTS'] = False



@ask.intent('GetParking')
def get_parking():
    location = ask_request.intent.slots.dest.value
    
    text = gettext.find_my_slot(location)
    print text
    print location
    print "++++++"
    return statement(text)


@ask.intent('GetPlates')
def get_plates():
    plate = ask_request.intent.slots.plate.value
    
    text = gettext.find_my_plate(plate)
    print text
    print "++++++"
    return statement(text)

if __name__ == '__main__':
    app.run(debug=True)

