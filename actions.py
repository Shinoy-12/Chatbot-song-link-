# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action,Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
#
import mysql.connector
con=mysql.connector.connect(
        database='train',
        host='localhost',
        port='3306',
        user='root',
        passwd='shinoy123')

global cursor
class ActionHelloWorld(Action):

     def name(self):
         return "action_retrieve_songs"

     def run(self, dispatcher, tracker, domain) :
         group = tracker.get_slot('songs')
         cursor = con.cursor()
         if group=="sad":
             query = ("SELECT sad FROM songs")
             cursor.execute(query)
             for(sad) in cursor:
                 dispatcher.utter_message("this is your song:{}".format(sad))
         elif group=="english":
             query = ("SELECT english FROM songs")
             cursor.execute(query)
             for(english) in cursor:
                 dispatcher.utter_message("this is your song:{}".format(english))
         elif group == "drunk":
             query = ("SELECT drunk FROM songs")
             cursor.execute(query)
             for(drunk) in cursor:
                 dispatcher.utter_message("this is your song:{}".format(drunk))

         return []

class ActionFormInfo(FormAction):
    def name(self) -> Text:
        """Unique identifier of the form"""

        return "form_info"

    @staticmethod
    def required_slots(tracker: Tracker):
        """A list of required slots that the form has to fill"""

        return ["NAME", "COUNTRY"]

    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    )-> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""

        # utter submit template
        dispatcher.utter_message(responses="utter_submit", name=tracker.get_slot('NAME'),
                                 country=tracker.get_slot('COUNTRY'))
        return []

    def slot_mappings(self):
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {
            "name": [self.from_entity(entity="NAME", intent='name_is'),
                     self.from_text()],
            "country": [self.from_entity(entity="COUNTRY", intent="country_is"),
                        self.from_text()],
        }