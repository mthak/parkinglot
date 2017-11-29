from ask import alexa
import get-text
import logging

def lambda_handler(request_obj, context={}):
    ''' All requests start here '''
    print "request object is " , request_obj
    return alexa.route_request(request_obj)


@alexa.default
def default_handler(request):
    """ The default handler gets invoked if no handler is set for a request """
    return alexa.create_response(message="Ask me Now")

@alexa.request("LaunchRequest")
def launch_request_handler(request):
    return alexa.create_response(message="Welcome to my Bart App. We can tell you more information about bart schedules       for example bart from Fremont to Daly City ",
           reprompt_message = "Would you like to know more?")


@alexa.request(request_type="SessionEndedRequest")
def session_ended_request_handler(request):
    return alexa.create_response(message="Goodbye!",end_session=True)


@alexa.intent('GetParking')
def get_posts_intent_handler(request):
    print " I am in checking",request,request.slots
    data = request.slots['dest']
    found = get-text.find_my_slot(data)
    return alexa.create_response(message='' .join(str(myoutput)),end_session=True)

@alexa.intent('GetPlate')
def get_posts_intent_handler(request):
    print " I am in checking",request,request.slots
    data = request.slots['plate']
    found = get-text.find_my_plate(data)
    return alexa.create_response(message='' .join(str(myoutput)),end_session=True)


@alexa.intent('AMAZON.HelpIntent')
def help_intent_handler(request):
    #st_list = str(mybart.stations)
    message = ["You can ask for Parking lot supsene - ",
               ]
    return alexa.create_response(message=' '.join(message),
                            reprompt_message='Would you like to know more about bart schedule?')


@alexa.intent('AMAZON.StopIntent')
def stop_intent_handler(request):
    return alexa.create_response(message="Goodbye!",end_session=True)

@alexa.intent('AMAZON.CancelIntent')
def stop_intent_handler(request):
    return alexa.create_response(message="Goodbye!",end_session=True)
