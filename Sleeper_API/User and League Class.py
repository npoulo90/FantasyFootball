import pandas as pd
import requests

class User:
    def __init__(self, name, user_name, years):
        self.name = name
        user_name: str 
        years = []
        
    def get_user(self, user_name):
        url = "https://api.sleeper.app/v1/user/" + user_name
        user = pd.DataFrame.from_dict(requests.get(url).json(), orient='index').T
        return user
    
    def get_user_id(self, user_name):
        url = "https://api.sleeper.app/v1/user/" + user_name
        user = pd.DataFrame.from_dict(requests.get(url).json(), orient='index').T
        return user['user_id']
    
    leagues = pd.DataFrame.from_dict(requests.get(url).json(), orient='index').T
    user_id = get_user['user_id'][0]
    
    def get_leagues(self, user_id, year):
        url = "https://api.sleeper.app/v1/user/" + user_id + "/leagues/nfl/" + str(year)
        leagues = pd.DataFrame.from_dict(requests.get(url).json()[0], orient='index').T
        return leagues