import pandas as pd
import requests
        
#rewrite the class to be more general
class User:
   def __init__(self, user_name: str()):
    #    user_name = self.user_name
        self.user_name = user_name
        
#Rewrite a method call the url and return a dataframe
   def get_user(self):
       url = "https://api.sleeper.app/v1/user/" + self.user_name
       user = pd.DataFrame.from_dict(requests.get(url).json(), orient='index').T
       return user
       
       
       

        
