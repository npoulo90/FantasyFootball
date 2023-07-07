import pandas as pd
import requests
import Raw_SleeperUser




class League:
    def __init__(self, user_id: str(), year: int()):
        self.user_id = user_id
        self.year = year
        
    def get_leagues(self):
        url = "https://api.sleeper.app/v1/user/" + self.user_id + "/leagues/nfl/" + str(self.year)
        leagues = pd.DataFrame.from_dict(requests.get(url).json()[0], orient='index').T
        return leagues
    
    def get_league_id(self):
        return self.get_leagues()['league_id'][0]

#create a descriptor for league_id in the dataframe returned by get_leagues
    @property
    def league_id(self):
        return self.get_leagues()['league_id'][0] 
    
    #how do I pass the league_id value from the dataframe returned by get_leagues() method to another method called get_rosters()?
    def get_rosters(self):
        
        url = "https://api.sleeper.app/v1/league/" + self.league_id + "/rosters"
        rosters = pd.DataFrame.from_dict(requests.get(url).json())
        return rosters
