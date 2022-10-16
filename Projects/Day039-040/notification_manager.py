from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
import ast
import os


class NotificationManager:
    """
    This class is responsible for sending notifications with the deal flight details.
    """
    def __init__(self, running_locally=True):
        if running_locally:
            # Read in credential string and save as a dictionary
            with open('../../../../Dropbox/100DaysOfCodePRIVATE/Day39Creds.txt') as file:
                creds_str = file.read()
                creds = ast.literal_eval(creds_str)

                # Save tokens as variables
                self.ACCOUNT_SID = creds['ACCOUNT_SID']  # use live creds (not test)
                self.AUTH_TOKEN = creds['AUTH_TOKEN']
                self.PHONE_NUMBER = creds['TWILIO_NUMBER']
                self.MY_NUMBER = creds['TOMS_NUMBER']

    def send_message(self, message_text):
        """
        Sends an SMS if condition is met
        :param message_text: The message to be sent, notifying of bargain flights
        """
        client = Client(self.ACCOUNT_SID, self.AUTH_TOKEN)

        message = client.messages \
            .create(
                body=message_text,
                from_=self.PHONE_NUMBER,
                to=self.MY_NUMBER)

        print(message.status)

# todo test functionality of deploying to the cloud
