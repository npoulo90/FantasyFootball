import datetime as dt
import requests
import pandas as pd

''' -------------- Sleeper API Base Class ----------------
Base class for Sleeper API	
	- Created 7.7.2023

------------- Description ------------------
	Used to call user_id and league_id 
	from Sleeper API.  This class is
	inherited by other classes to
	make API calls.
 
 Future Enhancements:
	Create a new class that is inherited
	for the purpose of making API calls
	based on the URL being passed in.
	This will allow for a templated
	process to make API calls.
 
------------------End Description------------------ '''
class sleeper(object):
	def	__init__(self, user_name: str(), year: str(None)):
		self.user_name = user_name
		self.year = year
		self.user_url = "https://api.sleeper.app/v1/user/" + user_name
		self.user_id = requests.get(self.user_url).json()['user_id']
		
	def get_user_id(self):
		return self.user_id
  
	def get_league_id(self):
		league_url = "https://api.sleeper.app/v1/user/" + self.user_id + "/leagues/nfl/" + self.year
		return requests.get(league_url).json()[0]['league_id']

## ---------- The section below can potentially be 
# used to create a templated process to make 
# api calls based on the URL being passed in-------- ##

# class makecall:
#     def __init__(self, url: str()):
#         self.url = url
        
#     def _call(self):
#         try:
#             results = requests.get(self.url).json()
#             return results
#         except:
#             print("Error: " + str(e))
#             return 

## ------------End Section ----------------- ##
        
        