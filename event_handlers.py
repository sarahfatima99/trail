from json import JSONDecodeError
import json
from database import user_signup,user_signout,user_subscribe,no_database


class handlers:
    def __init__(self,payload):

             
        self.payload=payload

       


    def get_db_object(self):

        try:
            json_payload=json.loads(self.payload)
            print(json_payload)

        except JSONDecodeError:
            print( 'JSON not in correct format')
            nd=no_database()
            return nd

        try:
            event_name=json_payload['header']['name']

        except KeyError:
            print('event name not found') 
            nd=no_database()
            return nd   


        if event_name=='User_SignedUp':                 

            us=user_signup(json_payload)
            return us

        if event_name=='User_SignedOut':
            uo=user_signout(json_payload)
            return uo

        if event_name=='User_Subscribe':
            usub=user_subscribe(json_payload)
            return usub


        