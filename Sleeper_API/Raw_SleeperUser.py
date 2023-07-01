#Create an api call using this url curl "https://api.sleeper.app/v1/user/<username>"
#Replace <username> with your poulos
#Load the data into a dataframe called user

import pandas as pd
import requests

class User:
    def __init__(self, user_name):
        self.user_name = user_name

    def get_user(self):
        url = "https://api.sleeper.app/v1/user/" + self.user_name
        user = pd.DataFrame.from_dict(requests.get(url).json(), orient='index').T
        return user
    
    def get_user_id(self):
        df = rsu.User('poulos').get_user()
        df['user_id'][0] 
        
