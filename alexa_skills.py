# -*- coding: utf-8 -*-

# This sample demonstrates handling intents from an Alexa skill using the Alexa Skills Kit SDK for Python.
# Please visit https://alexa.design/cookbook for additional examples on implementing slots, dialog management,
# session persistence, api calls, and more.
# This sample is built using the handler classes approach in skill builder.
import logging
import ask_sdk_core.utils as ask_utils

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model import Response

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool

        return ask_utils.is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Hello, Welcome to My Vote Matters. I am Alexa. What is your name?"
        #reprompt("I'm Alexa and Welcome to My Vote Matters. What is your name?")
        #handler_input.response_builder.speak(speak_output)
        reprompt_text = "I am Alexa, What is your name"

        handler_input.response_builder.speak(speak_output).ask(reprompt_text)

        return handler_input.response_builder.response
        
        # .ask(reprompt_text)
        #return handler_input.response_builder.response



class CaptureNameIntentHandler(AbstractRequestHandler):
    """Handler for capture Name Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("captureName")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        slots = handler_input.request_envelope.request.intent.slots
        user_name = slots["user_name"].value
        speak_output = "Thanks, I will remember that. {user_name}, how can I help you today. You can say things like 'why should i vote.".format(user_name=user_name)
        handler_input.response_builder.speak(speak_output)
        return handler_input.response_builder.response




class CaptureInitialQuestionIntentHandler(AbstractRequestHandler):
    """Handler for capture initial question."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("captureInitialQuestion")(handler_input)
    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        intent_name = ask_utils.get_intent_name(handler_input)
        if(intent_name == "captureInitialQuestion"):
            speak_output = "Did you know that only 19 percentage of people aged 18 to 24 cast their ballot in 2016 presidential election. How do you feel about that?"
            reprompt_text = "I agree. Fewer young people get to directly influence issues that might affect their lives for years to come, including college tuition reform and federal job programs. Are you interested in learning more about 2020 Presidential Election. You can say Yes and I will guide you."
            handler_input.response_builder.speak(speak_output).ask(reprompt_text)
            return handler_input.response_builder.response
        

class YesIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.YesIntent")(handler_input)
    def handle(self, handler_input):
        speak_output = " Ok! Brace Yourself. There are currently 19 people running for the 2020 Democratic nomination. President Donald Trump has picked up some Republican challengers too. Would you like to know the nominees from Democratic party or Republican party or both."
        reprompt_text = "hola hola which party"
        handler_input.response_builder.speak(speak_output).ask(reprompt_text)
        return handler_input.response_builder.response

class CapturePartyIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("captureParty")(handler_input)
    def handle(self, handler_input):
        
        slots = handler_input.request_envelope.request.intent.slots
        party  = slots["party"].value
        if(party.startswith('democrat')):
            speak_output= "Here is the list of all leaders from {party}".format(party=party)
        else:
            speak_output= "Donald trump is from Republican and here are all the leader".format(party=party)
        return(
            handler_input.response_builder
                .speak(speak_output)
                .response
        )



class HelpIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "You can say hello to me! How can I help?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class CancelOrStopIntentHandler(AbstractRequestHandler):
    """Single handler for Cancel and Stop Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (ask_utils.is_intent_name("AMAZON.CancelIntent")(handler_input) or
                ask_utils.is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Goodbye!"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )


class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for Session End."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        # Any cleanup logic goes here.

        return handler_input.response_builder.response


class IntentReflectorHandler(AbstractRequestHandler):
    """The intent reflector is used for interaction model testing and debugging.
    It will simply repeat the intent the user said. You can create custom handlers
    for your intents by defining them above, then also adding them to the request
    handler chain below.
    """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("IntentRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        intent_name = ask_utils.get_intent_name(handler_input)
        speak_output = "You just triggered " + intent_name + "."

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )


class CatchAllExceptionHandler(AbstractExceptionHandler):
    """Generic error handling to capture any syntax or routing errors. If you receive an error
    stating the request handler chain is not found, you have not implemented a handler for
    the intent being invoked or included it in the skill builder below.
    """
    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        logger.error(exception, exc_info=True)

        speak_output = "Sorry, I had trouble doing what you asked. Please try again."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

# The SkillBuilder object acts as the entry point for your skill, routing all request and response
# payloads to the handlers above. Make sure any new handlers or interceptors you've
# defined are included below. The order matters - they're processed top to bottom.


sb = SkillBuilder()

sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CaptureNameIntentHandler())
sb.add_request_handler(CaptureInitialQuestionIntentHandler())
sb.add_request_handler(YesIntentHandler())
sb.add_request_handler(CapturePartyIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
sb.add_request_handler(IntentReflectorHandler()) # make sure IntentReflectorHandler is last so it doesn't override your custom intent handlers

sb.add_exception_handler(CatchAllExceptionHandler())

lambda_handler = sb.lambda_handler()