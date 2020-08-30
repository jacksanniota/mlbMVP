import statsapi
import pandas as pd
import numpy as np
from io import StringIO 
from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup

playerNames = set()

def toDf(string):
    string = StringIO(string)
    string = pd.read_csv(string, sep='\n')
    print(string)
    # string = string.set_index('Name')
    return string

def getStats(statType):
    # stats = [{'name': 'Aaron Judge', 'teamName': 'New York Yankees', 'value': '9'}, {'name': 'Fernando Tatis Jr.', 'teamName': 'San Diego Padres', 'value': '9'}, {'name': 'Mike Trout', 'teamName': 'Los Angeles Angels', 'value': '9'}, {'name': 'Mookie Betts', 'teamName': 'Los Angeles Dodgers', 'value': '8'}, {'name': 'Nick Castellanos', 'teamName': 'Cincinnati Reds', 'value': '8'}, {'name': 'Matt Olson', 'teamName': 'Oakland Athletics', 'value': '8'}, {'name': 'J.T. Realmuto', 'teamName': 'Philadelphia Phillies', 'value': '8'}, {'name': 'Teoscar Hernandez', 'teamName': 'Toronto Blue Jays', 'value': '7'}, {'name': 'Eloy Jimenez', 'teamName': 'Chicago White Sox', 'value': '7'}, {'name': 'Brandon Lowe', 'teamName': 'Tampa Bay Rays', 'value': '7'}, {'name': 'Anthony Santander', 'teamName': 'Baltimore Orioles', 'value': '7'}, {'name': 'Nolan Arenado', 'teamName': 'Colorado Rockies', 'value': '6'}, {'name': 'Kole Calhoun', 'teamName': 'Arizona Diamondbacks', 'value': '6'}, {'name': 'Matt Chapman', 'teamName': 'Oakland Athletics', 'value': '6'}, {'name': 'Nelson Cruz', 'teamName': 'Minnesota Twins', 'value': '6'}, {'name': 'Max Kepler', 'teamName': 'Minnesota Twins', 'value': '6'}, {'name': 'Colin Moran', 'teamName': 'Pittsburgh Pirates', 'value': '6'}, {'name': 'Mitch Moreland', 'teamName': 'Boston Red Sox', 'value': '6'}, {'name': 'Anthony Rendon', 'teamName': 'Los Angeles Angels', 'value': '6'}, {'name': 'Eddie Rosario', 'teamName': 'Minnesota Twins', 'value': '6'}, {'name': 'Rio Ruiz', 'teamName': 'Baltimore Orioles', 'value': '6'}, {'name': 'Dominic Smith', 'teamName': 'New York Mets', 'value': '6'}, {'name': 'Juan Soto', 'teamName': 'Washington Nationals', 'value': '6'}, {'name': 'Trevor Story', 'teamName': 'Colorado Rockies', 'value': '6'}, {'name': 'Bo Bichette', 'teamName': 'Toronto Blue Jays', 'value': '5'}, {'name': 'Cavan Biggio', 'teamName': 'Toronto Blue Jays', 'value': '5'}, {'name': 'Byron Buxton', 'teamName': 'Minnesota Twins', 'value': '5'}, {'name': 'Maikel Franco', 'teamName': 'Kansas City Royals', 'value': '5'}, {'name': 'Joey Gallo', 'teamName': 'Texas Rangers', 'value': '5'}, {'name': 'Yuli Gurriel', 'teamName': 'Houston Astros', 'value': '5'}, {'name': 'Keston Hiura', 'teamName': 'Milwaukee Brewers', 'value': '5'}, {'name': 'JaCoby Jones', 'teamName': 'Detroit Tigers', 'value': '5'}, {'name': 'Manny Machado', 'teamName': 'San Diego Padres', 'value': '5'}, {'name': 'Whit Merrifield', 'teamName': 'Kansas City Royals', 'value': '5'}, {'name': 'Max Muncy', 'teamName': 'Los Angeles Dodgers', 'value': '5'}, {'name': 'Wil Myers', 'teamName': 'San Diego Padres', 'value': '5'}, {'name': 'Renato Nunez', 'teamName': 'Baltimore Orioles', 'value': '5'}, {'name': 'Marcell Ozuna', 'teamName': 'Atlanta Braves', 'value': '5'}, {'name': 'AJ Pollock', 'teamName': 'Los Angeles Dodgers', 'value': '5'}, {'name': 'Jose Ramirez', 'teamName': 'Cleveland Indians', 'value': '5'}, {'name': 'Franmil Reyes', 'teamName': 'Cleveland Indians', 'value': '5'}, {'name': 'Anthony Rizzo', 'teamName': 'Chicago Cubs', 'value': '5'}, {'name': 'Corey Seager', 'teamName': 'Los Angeles Dodgers', 'value': '5'}, {'name': 'Pedro Severino', 'teamName': 'Baltimore Orioles', 'value': '5'}, {'name': 'Jorge Soler', 'teamName': 'Kansas City Royals', 'value': '5'}, {'name': 'Alex Verdugo', 'teamName': 'Boston Red Sox', 'value': '5'}, {'name': 'Luke Voit', 'teamName': 'New York Yankees', 'value': '5'}, {'name': 'Jesse Winker', 'teamName': 'Cincinnati Reds', 'value': '5'}, {'name': 'Mike Yastrzemski', 'teamName': 'San Francisco Giants', 'value': '5'}, {'name': 'Christian Yelich', 'teamName': 'Milwaukee Brewers', 'value': '5'}, {'name': 'Jose Abreu', 'teamName': 'Chicago White Sox', 'value': '4'}, {'name': 'Ronald Acuna Jr.', 'teamName': 'Atlanta Braves', 'value': '4'}, {'name': 'Jesus Aguilar', 'teamName': 'Miami Marlins', 'value': '4'}, {'name': 'Brian Anderson', 'teamName': 'Miami Marlins', 'value': '4'}, {'name': 'Cody Bellinger', 'teamName': 'Los Angeles Dodgers', 'value': '4'}, {'name': 'Xander Bogaerts', 'teamName': 'Boston Red Sox', 'value': '4'}, {'name': 'Alex Bregman', 'teamName': 'Houston Astros', 'value': '4'}, {'name': 'Asdrubal Cabrera', 'teamName': 'Washington Nationals', 'value': '4'}, {'name': 'Miguel Cabrera', 'teamName': 'Detroit Tigers', 'value': '4'}, {'name': 'C.J. Cron', 'teamName': 'Detroit Tigers', 'value': '4'}, {'name': 'Wilmer Flores', 'teamName': 'San Francisco Giants', 'value': '4'}, {'name': 'Freddy Galvis', 'teamName': 'Cincinnati Reds', 'value': '4'}, {'name': 'Niko Goodrum', 'teamName': 'Detroit Tigers', 'value': '4'}, {'name': 'Brian Goodwin', 'teamName': 'Los Angeles Angels', 'value': '4'}, {'name': 'Trent Grisham', 'teamName': 'San Diego Padres', 'value': '4'}, {'name': 'Bryce Harper', 'teamName': 'Philadelphia Phillies', 'value': '4'}, {'name': 'Eric Hosmer', 'teamName': 'San Diego Padres', 'value': '4'}, {'name': 'Kyle Lewis', 'teamName': 'Seattle Mariners', 'value': '4'}, {'name': 'Francisco Lindor', 'teamName': 'Cleveland Indians', 'value': '4'}, {'name': 'Yoan Moncada', 'teamName': 'Chicago White Sox', 'value': '4'}, {'name': 'Dylan Moore', 'teamName': 'Seattle Mariners', 'value': '4'}, {'name': 'Shohei Ohtani', 'teamName': 'Los Angeles Angels', 'value': '4'}, {'name': 'Salvador Perez', 'teamName': 'Kansas City Royals', 'value': '4'}, {'name': 'Stephen Piscotty', 'teamName': 'Oakland Athletics', 'value': '4'}, {'name': 'Hunter Renfroe', 'teamName': 'Tampa Bay Rays', 'value': '4'}, {'name': 'Gary Sanchez', 'teamName': 'New York Yankees', 'value': '4'}, {'name': 'Miguel Sano', 'teamName': 'Minnesota Twins', 'value': '4'}, {'name': 'Jonathan Schoop', 'teamName': 'Detroit Tigers', 'value': '4'}, {'name': 'Max Stassi', 'teamName': 'Los Angeles Angels', 'value': '4'}, {'name': 'Trea Turner', 'teamName': 'Washington Nationals', 'value': '4'}, {'name': 'Gio Urshela', 'teamName': 'New York Yankees', 'value': '4'}, {'name': 'Christian Vazquez', 'teamName': 'Boston Red Sox', 'value': '4'}, {'name': 'Pete Alonso', 'teamName': 'New York Mets', 'value': '3'}, {'name': 'Jose Altuve', 'teamName': 'Houston Astros', 'value': '3'}, {'name': 'Javier Baez', 'teamName': 'Chicago Cubs', 'value': '3'}, {'name': 'Charlie Blackmon', 'teamName': 'Colorado Rockies', 'value': '3'}, {'name': 'Mike Brosseau', 'teamName': 'Tampa Bay Rays', 'value': '3'}, {'name': 'Jay Bruce', 'teamName': 'Philadelphia Phillies', 'value': '3'}, {'name': 'Johan Camargo', 'teamName': 'Atlanta Braves', 'value': '3'}, {'name': 'Francisco Cervelli', 'teamName': 'Miami Marlins', 'value': '3'}, {'name': 'Shin-Soo Choo', 'teamName': 'Texas Rangers', 'value': '3'}, {'name': 'Michael Conforto', 'teamName': 'New York Mets', 'value': '3'}, {'name': 'J.D. Davis', 'teamName': 'New York Mets', 'value': '3'}, {'name': 'Adam Duvall', 'teamName': 'Atlanta Braves', 'value': '3'}, {'name': 'David Fletcher', 'teamName': 'Los Angeles Angels', 'value': '3'}, {'name': 'Adam Frazier', 'teamName': 'Pittsburgh Pirates', 'value': '3'}, {'name': 'Freddie Freeman', 'teamName': 'Atlanta Braves', 'value': '3'}, {'name': 'Leury Garcia', 'teamName': 'Chicago White Sox', 'value': '3'}, {'name': 'Brett Gardner', 'teamName': 'New York Yankees', 'value': '3'}, {'name': 'Didi Gregorius', 'teamName': 'Philadelphia Phillies', 'value': '3'}, {'name': 'Robbie Grossman', 'teamName': 'Oakland Athletics', 'value': '3'}, {'name': 'Vladimir Guerrero Jr.', 'teamName': 'Toronto Blue Jays', 'value': '3'}, {'name': 'Ian Happ', 'teamName': 'Chicago Cubs', 'value': '3'}, {'name': 'Ramon Laureano', 'teamName': 'Oakland Athletics', 'value': '3'}, {'name': 'Ryan McBroom', 'teamName': 'Kansas City Royals', 'value': '3'}, {'name': 'James McCann', 'teamName': 'Chicago White Sox', 'value': '3'}, {'name': 'Ryan McMahon', 'teamName': 'Colorado Rockies', 'value': '3'}, {'name': 'Daniel Murphy', 'teamName': 'Colorado Rockies', 'value': '3'}, {'name': 'Brandon Nimmo', 'teamName': 'New York Mets', 'value': '3'}, {'name': "Tyler O'Neill", 'teamName': 'St. Louis Cardinals', 'value': '3'}, {'name': 'Joc Pederson', 'teamName': 'Los Angeles Dodgers', 'value': '3'}, {'name': 'Albert Pujols', 'teamName': 'Los Angeles Angels', 'value': '3'}, {'name': 'Austin Riley', 'teamName': 'Atlanta Braves', 'value': '3'}, {'name': 'Edwin Rios', 'teamName': 'Los Angeles Dodgers', 'value': '3'}, {'name': 'Luis Robert', 'teamName': 'Chicago White Sox', 'value': '3'}, {'name': 'Kyle Schwarber', 'teamName': 'Chicago Cubs', 'value': '3'}, {'name': 'Kyle Seager', 'teamName': 'Seattle Mariners', 'value': '3'}, {'name': 'Jean Segura', 'teamName': 'Philadelphia Phillies', 'value': '3'}, {'name': 'Marcus Semien', 'teamName': 'Oakland Athletics', 'value': '3'}, {'name': 'Austin Slater', 'teamName': 'San Francisco Giants', 'value': '3'}, {'name': 'George Springer', 'teamName': 'Houston Astros', 'value': '3'}, {'name': 'Giancarlo Stanton', 'teamName': 'New York Yankees', 'value': '3'}, {'name': 'Rowdy Tellez', 'teamName': 'Toronto Blue Jays', 'value': '3'}, {'name': 'Yoshi Tsutsugo', 'teamName': 'Tampa Bay Rays', 'value': '3'}, {'name': 'Joey Votto', 'teamName': 'Cincinnati Reds', 'value': '3'}, {'name': "Travis d'Arnaud", 'teamName': 'Atlanta Braves', 'value': '3'}]
    stats = statsapi.league_leaders(leaderCategories=statType, season=2020, playerPool='all', limit=100)
    addPlayerNames(statType, stats)
    return stats


def getHomeruns():
    homerunWeights = {}
    homerunLeaders = getStats('homeruns')
    # print(homerunLeaders)
    homerunAvg = getAvg(homerunLeaders)
    for player in homerunLeaders:
        playerName = player['name']
        playerWeight = float(player['value']) / homerunAvg
        homerunWeights.update({playerName : playerWeight})
    return homerunWeights

def getRBIs():
    rbiWeights = {}
    rbiLeaders = getStats('runsBattedIn')
    # print(homerunLeaders)
    rbiAvg = getAvg(rbiLeaders)
    for player in rbiLeaders:
        playerName = player['name']
        playerWeight = float(player['value']) / rbiAvg
        rbiWeights.update({playerName : playerWeight})
    return rbiWeights

def getBattingAverage():
    battingAverageWeights = {}
    battingAverageLeaders = getStats('battingAverage')
    battingAverageLeaders = getCommonLeaders(battingAverageLeaders)
    battingAverageAvg = getAvg(battingAverageLeaders)
    for player in battingAverageLeaders:
        playerName = player['name']
        playerWeight = float(player['value']) / battingAverageAvg
        battingAverageWeights.update({playerName : playerWeight})
    return battingAverageWeights

def getSluggingPercentage():
    sluggingPercentageWeights = {}
    sluggingPercentageLeaders = getStats('sluggingPercentage')
    sluggingPercentageLeaders = getCommonLeaders(sluggingPercentageLeaders)
    sluggingPercentageAvg = getAvg(sluggingPercentageLeaders)
    for player in sluggingPercentageLeaders:
        playerName = player['name']
        playerWeight = float(player['value']) / sluggingPercentageAvg
        sluggingPercentageWeights.update({playerName : playerWeight})
    return sluggingPercentageWeights

def getOnBasePercentage():
    onBasePercentageWeights = {}
    onBasePercentageLeaders = getStats('onBasePercentage')
    onBasePercentageLeaders = getCommonLeaders(onBasePercentageLeaders)
    onBasePercentageAvg = getAvg(onBasePercentageLeaders)
    for player in onBasePercentageLeaders:
        playerName = player['name']
        playerWeight = float(player['value']) / onBasePercentageAvg
        onBasePercentageWeights.update({playerName : playerWeight})
    return onBasePercentageWeights

def getCommonLeaders(leaders):
    commonLeaders = []
    for player in leaders:
        playerName = player['name']
        if playerName in playerNames:
            commonLeaders.append(player)
    return commonLeaders

def addPlayerNames(statType, stats):
    if statType == 'homeruns' or statType == 'runsBattedIn':
        for player in stats:
            playerNames.add(player['name'])

    
def getAvg(leaders):
    average = 0
    for player in leaders:
        average += float(player['value'])
    return average/len(leaders)

def calculateMVPscores(weightLists):
    playersUsed = set()
    playerScores = {}
    for weightList in weightLists:
        # print(weightList)
        for player in weightList:
            if player in playersUsed:
                playerScores[player] += (weightList[player] * 0.2)
            else:
                playerScores[player] = (weightList[player] * 0.2)
                playersUsed.add(player)
    return playerScores



def main():
    playerWeights = {}
    homerunWeights = getHomeruns()
    # # print(homerunWeights)
    rbiWeights = getRBIs()
    # # print(rbiWeights)
    battingAverageWeights = getBattingAverage()
    # # print(battingAverageWeights)
    sluggingPercentageWeights = getSluggingPercentage()
    # # print(sluggingPercentageWeights)
    onBasePercentageWeights = getOnBasePercentage()
    weightLists = [homerunWeights, rbiWeights, battingAverageWeights, sluggingPercentageWeights, onBasePercentageWeights]
    mvpScores = calculateMVPscores(weightLists)
    mvpScores = sorted(mvpScores.items(), key=lambda x: x[1], reverse=True)
    # ranks = np.arange(1, len(mvpScores))
    df = pd.DataFrame(mvpScores, columns =['Name', 'Score'])
    df['Rank'] = np.arange(1, len(mvpScores) + 1)
    df = df.set_index('Rank')
    print(df.to_string())
    # print(onBasePercentageWeights)
    # statTypes = statsapi.meta('leagueLeaderTypes')
    # print(statTypes)


if __name__ == '__main__':
    main()
