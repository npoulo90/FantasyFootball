import pandas as pd
import requests
import base



class League(makecall):                 # Inherit from User class
    def __init__ (self, user_name: str(), year: str()): # Initialize with user_name and year
        self.user_name = user_name
        self.year = year       # Inherit from User class
        self.base_url = "https://api.sleeper.app/v1/user/" + self.user_name + "/leagues/nfl/" + self.year
        
    def get_user_leagues(self):
        return self._call(self.base_url)
            

### Sleeper League Class ###
# class League(base):                 # Inherit from User class
#     def __init__ (self, user_name: str(), year: str()): # Initialize with user_name and year
#         self.user_name = user_name
#         self.year = year       # Inherit from User class
        
#     def get_user_leagues(self):
#         # league_url = "https://api.sleeper.app/v1/user/" + super().get_user_id() + "/leagues/nfl/" + self.year
#         return super().get_user_id()
        
#     def get_league_id(self):
#         return league_id

        
        
# # class Rosters(League):              # Inherit from League class
# #     def __init__(self, user_name: str(), year: str()): # Initialize with league_id and year
# #         super().__init__(user_name, year)        # Inherit from League class
# #         league_id = super().get_league_id()  # Get league_id from League class
        
        
#     def get_rosters(self):
#         league_id = super().get_league_id()  # Get league_id from League class
#         url = "https://api.sleeper.app/v1/league/" + league_id + "/rosters"
#         rosters = pd.DataFrame.from_dict(requests.get(url).json())
#         return rosters
        
        
 

    
    

