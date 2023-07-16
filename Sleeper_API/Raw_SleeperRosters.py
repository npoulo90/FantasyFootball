import requests
import pandas as pd
import json
import base
from Raw_SleeperLeague import League
        
class Rosters(League):              
    def __init__(self, user_name, year, **kwargs):        
        self.user_name = user_name
        self.year = year

        
    def get_rosters(self):
        league_id = base.sleeper(self.user_name, self.year).get_league_id()
        roster_url = "https://api.sleeper.app/v1/league/" + str(league_id)  + "/rosters"      
        return base.makecall(roster_url)._call()



# class Rosters(League):              # Inherit from League class
#     def __init__(self, user_name: str(), year: str()): # Initialize with league_id and year
#         super().__init__(user_name, year)        # Inherit from League class
#         league_id = super().get_league_id()  # Get league_id from League class
        
        
#     def get_rosters(self):
#         league_id = super().get_league_id()  # Get league_id from League class
#         url = "https://api.sleeper.app/v1/league/" + league_id + "/rosters"
#         rosters = pd.DataFrame.from_dict(requests.get(url).json())
#         return rosters