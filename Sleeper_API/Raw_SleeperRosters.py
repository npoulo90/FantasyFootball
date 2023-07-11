import requests
import pandas as pd
import json
from base import makecall
from Raw_SleeperLeague import League


class Rosters(League,makecall):              # Inherit from League class
    def __init__(self, user_name: str(), year: str()): # Initialize with league_id and year
        super().__init__(user_name, year)        # Inherit from League class
        self.user_name = user_name
        self.year = year
               # Inherit from League class

    def get_rosters(self):
        league_id = super().__init__.get_league_id()
        roster_url = "https://api.sleeper.app/v1/league/" + str(league_id) + "/rosters"
        return super(roster_url).__init__._call()




# class Rosters(League):              # Inherit from League class
#     def __init__(self, user_name: str(), year: str()): # Initialize with league_id and year
#         super().__init__(user_name, year)        # Inherit from League class
#         league_id = super().get_league_id()  # Get league_id from League class
        
        
#     def get_rosters(self):
#         league_id = super().get_league_id()  # Get league_id from League class
#         url = "https://api.sleeper.app/v1/league/" + league_id + "/rosters"
#         rosters = pd.DataFrame.from_dict(requests.get(url).json())
#         return rosters