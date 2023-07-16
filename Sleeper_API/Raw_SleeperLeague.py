import pandas as pd
import requests
import base

''' -------------- Sleeper API League Class ----------------
Base class for Sleeper API	
	- Created 7.7.2023

------------- Description ------------------
	Used to call user_id and league_id 
	from Sleeper API.  This class is
	inherited by other classes to
	make API calls.
 
 Future Enhancements:
	- Add error handling
 
------------------End Description------------------ '''



class League():               
    def __init__ (self, user_name: str(), year: str(), **kwargs): # Initialize with user_name and year
        self.user_name = user_name
        self.year = year       # Inherit from User class
    
    def get_all_users(self):
        # base_url = base_url = "https://api.sleeper.app/v1/user/" + self.user_name + "/leagues/nfl/" + self.year
        # league_id = pd.DataFrame.from_dict(base.makecall(base_url)._call())['league_id'][0]
        league_id = base.sleeper(self.user_name, self.year).get_league_id()
        all_users_url = "https://api.sleeper.app/v1/league/" + str(league_id) + "/users"
        all_users =  base.makecall(all_users_url)._call() # requests.get(all_users_url).json()
        return pd.DataFrame.from_dict(all_users)

# class get_league_id(self):
    # league_id = pd.DataFrame.from_dict(super()._call())
    # # league_id = league_id['league_id'][0]
    # return league_id
        
# class Rosters(League):              # Inherit from League class
#     def __init__(self, user_name: str(), year: str()): # Initialize with league_id and year
#         super().__init__(user_name, year)        # Inherit from League class
#         league_id = super().get_league_id()  # Get league_id from League class
        

#     def get_rosters(self):
#         league_id = super().get_league_id()  # Get league_id from League class
#         url = "https://api.sleeper.app/v1/league/" + league_id + "/rosters"
#         rosters = pd.DataFrame.from_dict(requests.get(url).json())
#         return rosters
        
        
 

    
    

