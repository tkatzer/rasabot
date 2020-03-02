from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionHelloWorld(Action):

     def name(self) -> Text:
         return "write_database"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


        name = tracker.get_slot("Name_Interessent")
        email = tracker.get_slot("E-Mail_Interessent")
        termin = tracker.get_slot("Treffen_Datum")

        dispatcher.utter_message(text="blabla {}:{}".format(name,email))

        return []
