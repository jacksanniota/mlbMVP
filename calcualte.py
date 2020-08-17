import statsapi
import pandas as pd
from io import StringIO 

def toDf(string):
    string = StringIO(string)
    string = pd.read_csv(string, sep='\n')
    print(string)
    # string = string.set_index('Name')
    return string

def getStats(statType):
    return statsapi.league_leaders(leaderCategories=statType, season=2020, playerPool='all', limit=100)


def getHomeruns():
    homerunLeaders = getStats('homeruns')
    print(homerunLeaders)
    homerunAvg = getAvg(homerunLeaders)
    


def getAvg(leaders):
    average = 0
    print(leaders)
    # for player in leaders.keys():
    #     # print(leaders)
    #     print(player)
        # print(leaders[player])
        # average += leaders[player]['value']
    # print(average)

getHomeruns()

# for col in hrLeaders.columns:
#     print(col)
# print(hrLeaders.head())
