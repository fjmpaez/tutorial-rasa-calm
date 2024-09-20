# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions
import random
# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher

MIN_TRANSFER_AMOUNT = 50.0


class ActionGetBalance(Action):

    def name(self) -> Text:
        return "action_balance"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        balance = random.uniform(0.5, 5.0) * 1000.0  # Simulate a balance

        return [SlotSet(key="balance", value=balance)]


class ActionLastTransactions(Action):

    def name(self) -> Text:
        return "action_last_transactions"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Request last transactions
        last_transactions = "\n06/03/2024 |  -60.45 EUR | Gasolina\n06/03/2024 | -189.34 EUR | Restaurante con amigos\n02/03/2024 | -250.34 EUR | Compra en Grandes Almacenes"

        return [SlotSet(key="last_transactions", value=last_transactions)]


def validate_account_number(account_number: str) -> bool:
    return not account_number.startswith("9")


class ActionTransfer(Action):

    def name(self) -> Text:
        return "action_transfer"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Make the transfer...

        return []
