import pandas as pd
import requests
from base import makecall

class League(makecall):                 # Inherit from User class
    def __init__ (self, user_name: str(), year: str()): # Initialize with user_name and year
        self.user_name = user_name
        self.year = year       # Inherit from User class
        self.base_url = "https://api.sleeper.app/v1/user/" + self.user_name + "/leagues/nfl/" + self.year
        super().__init__(self.base_url)        # Inherit from User class
        
    def get_user_leagues(self):
        return self._call()
    
    def get_all_users(self):
        league_id = pd.DataFrame.from_dict(super()._call())
        league_id = league_id['league_id'][0]
        all_users_url = "https://api.sleeper.app/v1/league/" + str(league_id) + "/users"
        all_users =  makecall(all_users_url)._call() # requests.get(all_users_url).json()
        return pd.DataFrame.from_dict(all_users)

class get_league_id(self):
    league_id = pd.DataFrame.from_dict(super()._call())
    league_id = league_id['league_id'][0]
    return league_id
        
# class Rosters(League):              # Inherit from League class
#     def __init__(self, user_name: str(), year: str()): # Initialize with league_id and year
#         super().__init__(user_name, year)        # Inherit from League class
#         league_id = super().get_league_id()  # Get league_id from League class
        

#     def get_rosters(self):
#         league_id = super().get_league_id()  # Get league_id from League class
#         url = "https://api.sleeper.app/v1/league/" + league_id + "/rosters"
#         rosters = pd.DataFrame.from_dict(requests.get(url).json())
#         return rosters
        
        
 

    
    

