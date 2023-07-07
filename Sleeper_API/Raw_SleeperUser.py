import pandas as pd
import requests
            
class User:
    def __init__(self,  user_name: str()):
        self.user_name = user_name
        self.url = "https://api.sleeper.app/v1/user/" + self.user_name
        # self.get_user = requests.get(self.url).json()

    def get_user(self):
        return pd.DataFrame.from_dict(requests.get(self.url).json(), orient = 'index').T
    

       
       
       

        
