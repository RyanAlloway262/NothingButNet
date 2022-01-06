# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 10:33:02 2020

@author: kipfe
"""
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
import json
import pandas as pd
import requests
import numpy as np
from sklearn.metrics import classification_report,confusion_matrix
import xlwt 
from xlwt import Workbook 
from openpyxl import load_workbook

winPctTrain = []
ptPct = []
goalRating = []
scoreFirst = []
leadFirst = []
outShoot = []
teamScore = []
teamID = []
teamFullName = []

wb = Workbook() 
sheet1 = wb.add_sheet('Sheet 1') 
sheet2 = wb.add_sheet('Sheet 2') 
sheet3 = wb.add_sheet('Sheet 3') 
sheet4 = wb.add_sheet('Sheet 4') 

def team_Info(season):
    if (season == 20152016 or season == 20162017):
        for x in range(1, 11):
            r = requests.get("https://statsapi.web.nhl.com//api//v1/teams//" + str(x) + "?season=" + str(season))
            obj = json.loads(r.text)
            team = obj["teams"]
            name = team[0]["name"]
            ID = team[0]["id"]
            teamFullName.append(name)
            teamID.append(ID)
            
        for x in range(12, 27):
            r = requests.get("https://statsapi.web.nhl.com//api//v1/teams//" + str(x) + "?season=" + str(season))
            obj = json.loads(r.text)
            team = obj["teams"]
            name = team[0]["name"]
            ID = team[0]["id"]
            teamFullName.append(name)
            teamID.append(ID)
            
        for x in range(28, 31):
            r = requests.get("https://statsapi.web.nhl.com//api//v1/teams//" + str(x) + "?season=" + str(season))
            obj = json.loads(r.text)
            team = obj["teams"]
            name = team[0]["name"]
            ID = team[0]["id"]
            teamFullName.append(name)
            teamID.append(ID)
            
        for x in range(52, 54):
            r = requests.get("https://statsapi.web.nhl.com//api//v1/teams//" + str(x) + "?season=" + str(season))
            obj = json.loads(r.text)
            team = obj["teams"]
            name = team[0]["name"]
            ID = team[0]["id"]
            teamFullName.append(name)
            teamID.append(ID)
    
    else:
        for x in range(1, 11):
            r = requests.get("https://statsapi.web.nhl.com//api//v1/teams//" + str(x) + "?season=" + str(season))
            obj = json.loads(r.text)
            team = obj["teams"]
            name = team[0]["name"]
            ID = team[0]["id"]
            teamFullName.append(name)
            teamID.append(ID)
            
        for x in range(12, 27):
            r = requests.get("https://statsapi.web.nhl.com//api//v1/teams//" + str(x) + "?season=" + str(season))
            obj = json.loads(r.text)
            team = obj["teams"]
            name = team[0]["name"]
            ID = team[0]["id"]
            teamFullName.append(name)
            teamID.append(ID)
            
        for x in range(28, 31):
            r = requests.get("https://statsapi.web.nhl.com//api//v1/teams//" + str(x) + "?season=" + str(season))
            obj = json.loads(r.text)
            team = obj["teams"]
            name = team[0]["name"]
            ID = team[0]["id"]
            teamFullName.append(name)
            teamID.append(ID)
            
        for x in range(52, 55):
            r = requests.get("https://statsapi.web.nhl.com//api//v1/teams//" + str(x) + "?season=" + str(season))
            obj = json.loads(r.text)
            team = obj["teams"]
            name = team[0]["name"]
            ID = team[0]["id"]
            teamFullName.append(name)
            teamID.append(ID)


def W_Pct(season): # Gets every teams win percentage
    if (season == 20102011):
        for x in range(1, 31):
            r = requests.get("https://statsapi.web.nhl.com//api//v1/teams//" + str(x) + "?expand=team.stats&season=" + str(season))
            obj = json.loads(r.text)
            team = obj["teams"]
            teamStats = team[0]['teamStats'][0]['splits'][0]['stat']
            teamWin = teamStats['wins']
            teamGP = teamStats['gamesPlayed']
            winPct = teamWin / teamGP
            winPctTrain.append(winPct)
            
    elif (season == 20112012 or season == 20122013 or season == 20132014):
        for x in range(1, 11):
            r = requests.get("https://statsapi.web.nhl.com//api//v1/teams//" + str(x) + "?expand=team.stats&season=" + str(season))
            obj = json.loads(r.text)
            team = obj["teams"]
            teamStats = team[0]['teamStats'][0]['splits'][0]['stat']
            teamWin = teamStats['wins']
            teamGP = teamStats['gamesPlayed']
            winPct = teamWin / teamGP
            winPctTrain.append(winPct)
        for x in range(12, 31):
            r = requests.get("https://statsapi.web.nhl.com//api//v1/teams//" + str(x) + "?expand=team.stats&season=" + str(season))
            obj = json.loads(r.text)
            team = obj["teams"]
            teamStats = team[0]['teamStats'][0]['splits'][0]['stat']
            teamWin = teamStats['wins']
            teamGP = teamStats['gamesPlayed']
            winPct = teamWin / teamGP
            winPctTrain.append(winPct)
        
        r = requests.get("https://statsapi.web.nhl.com//api//v1/teams//" + 52 + "?expand=team.stats&season=" + str(season))         # Thrashers (11) --> Jets (52)
        obj = json.loads(r.text)
        team = obj["teams"]
        teamStats = team[0]['teamStats'][0]['splits'][0]['stat']
        teamWin = teamStats['wins']
        teamGP = teamStats['gamesPlayed']
        winPct = teamWin / teamGP
        winPctTrain.append(winPct)
    
    elif (season == 20142015 or season == 20152016 or season == 20162017): # Phoneix Coyotes (27) --> Arizona Coyotes (53)
        for x in range(1, 11):
            r = requests.get("https://statsapi.web.nhl.com//api//v1/teams//" + str(x) + "?expand=team.stats&season=" + str(season))
            obj = json.loads(r.text)
            team = obj["teams"]
            teamStats = team[0]['teamStats'][0]['splits'][0]['stat']
            teamWin = teamStats['wins']
            teamGP = teamStats['gamesPlayed']
            winPct = teamWin / teamGP
            winPctTrain.append(winPct)
        
        for x in range(12, 27):
            r = requests.get("https://statsapi.web.nhl.com//api//v1/teams//" + str(x) + "?expand=team.stats&season=" + str(season))
            obj = json.loads(r.text)
            team = obj["teams"]
            teamStats = team[0]['teamStats'][0]['splits'][0]['stat']
            teamWin = teamStats['wins']
            teamGP = teamStats['gamesPlayed']
            winPct = teamWin / teamGP
            winPctTrain.append(winPct)
            
        for x in range(28, 31):
            r = requests.get("https://statsapi.web.nhl.com//api//v1/teams//" + str(x) + "?expand=team.stats&season=" + str(season))
            obj = json.loads(r.text)
            team = obj["teams"]
            teamStats = team[0]['teamStats'][0]['splits'][0]['stat']
            teamWin = teamStats['wins']
            teamGP = teamStats['gamesPlayed']
            winPct = teamWin / teamGP
            winPctTrain.append(winPct)
            
        for x in range(52, 54):
            r = requests.get("https://statsapi.web.nhl.com//api//v1/teams//" + str(x) + "?expand=team.stats&season=" + str(season))
            obj = json.loads(r.text)
            team = obj["teams"]
            teamStats = team[0]['teamStats'][0]['splits'][0]['stat']
            teamWin = teamStats['wins']
            teamGP = teamStats['gamesPlayed']
            winPct = teamWin / teamGP
            winPctTrain.append(winPct)
    else:
        for x in range(1, 11):
            r = requests.get("https://statsapi.web.nhl.com//api//v1/teams//" + str(x) + "?expand=team.stats&season=" + str(season))
            obj = json.loads(r.text)
            team = obj["teams"]
            teamStats = team[0]['teamStats'][0]['splits'][0]['stat']
            teamWin = teamStats['wins']
            teamGP = teamStats['gamesPlayed']
            winPct = teamWin / teamGP
            winPctTrain.append(winPct)
            
        for x in range(12, 27):
            r = requests.get("https://statsapi.web.nhl.com//api//v1/teams//" + str(x) + "?expand=team.stats&season=" + str(season))
            obj = json.loads(r.text)
            team = obj["teams"]
            teamStats = team[0]['teamStats'][0]['splits'][0]['stat']
            teamWin = teamStats['wins']
            teamGP = teamStats['gamesPlayed']
            winPct = teamWin / teamGP
            winPctTrain.append(winPct)
            
        for x in range(28, 31):
            r = requests.get("https://statsapi.web.nhl.com//api//v1/teams//" + str(x) + "?expand=team.stats&season=" + str(season))
            obj = json.loads(r.text)
            team = obj["teams"]
            teamStats = team[0]['teamStats'][0]['splits'][0]['stat']
            teamWin = teamStats['wins']
            teamGP = teamStats['gamesPlayed']
            winPct = teamWin / teamGP
            winPctTrain.append(winPct)
            
        for x in range(52, 55):
            r = requests.get("https://statsapi.web.nhl.com//api//v1/teams//" + str(x) + "?expand=team.stats&season=" + str(season))
            obj = json.loads(r.text)
            team = obj["teams"]
            teamStats = team[0]['teamStats'][0]['splits'][0]['stat']
            teamWin = teamStats['wins']
            teamGP = teamStats['gamesPlayed']
            winPct = teamWin / teamGP
            winPctTrain.append(winPct);
    
    return(winPctTrain)

def P_Pct(season): # Get every teams point percentage
    if (season == 20102011):
        for x in range(12, 31):
            r = requests.get("https://statsapi.web.nhl.com//api//v1/teams//" + str(x) + "?expand=team.stats&season=" + str(season))
            obj = json.loads(r.text)
            team = obj["teams"]
            teamStats = team[0]['teamStats'][0]['splits'][0]['stat']
            ptPcg = teamStats['ptPctg']
            ptPct.append(ptPcg)
    elif (season == 20112012 or season == 20122013 or season == 20132014):
        for x in range(1, 11):
            r = requests.get("https://statsapi.web.nhl.com//api//v1/teams//" + str(x) + "?expand=team.stats&season=" + str(season))
            obj = json.loads(r.text)
            team = obj["teams"]
            teamStats = team[0]['teamStats'][0]['splits'][0]['stat']
            ptPcg = teamStats['ptPctg']
            ptPct.append(ptPcg)
    
        for x in range(12, 31):
            r = requests.get("https://statsapi.web.nhl.com//api//v1/teams//" + str(x) + "?expand=team.stats&season=" + str(season))
            obj = json.loads(r.text)
            team = obj["teams"]
            teamStats = team[0]['teamStats'][0]['splits'][0]['stat']
            ptPcg = teamStats['ptPctg']
            ptPct.append(ptPcg)
        
        r = requests.get("https://statsapi.web.nhl.com//api//v1/teams//" + 52 + "?expand=team.stats&season=" + str(season))
        obj = json.loads(r.text)
        team = obj["teams"]
        teamStats = team[0]['teamStats'][0]['splits'][0]['stat']
        ptPcg = teamStats['ptPctg']
        ptPct.append(ptPcg)
            
    elif (season == 20142015 or season == 20152016 or season == 20162017): # Phoneix Coyotes (27) --> Arizona Coyotes (53)
        for x in range(1, 11):
            r = requests.get("https://statsapi.web.nhl.com//api//v1/teams//" + str(x) + "?expand=team.stats&season=" + str(season))
            obj = json.loads(r.text)
            team = obj["teams"]
            teamStats = team[0]['teamStats'][0]['splits'][0]['stat']
            ptPcg = teamStats['ptPctg']
            ptPct.append(ptPcg)
    
        for x in range(12, 27):
            r = requests.get("https://statsapi.web.nhl.com//api//v1/teams//" + str(x) + "?expand=team.stats&season=" + str(season))
            obj = json.loads(r.text)
            team = obj["teams"]
            teamStats = team[0]['teamStats'][0]['splits'][0]['stat']
            ptPcg = teamStats['ptPctg']
            ptPct.append(ptPcg)
            
        for x in range(28, 31):
            r = requests.get("https://statsapi.web.nhl.com//api//v1/teams//" + str(x) + "?expand=team.stats&season=" + str(season))
            obj = json.loads(r.text)
            team = obj["teams"]
            teamStats = team[0]['teamStats'][0]['splits'][0]['stat']
            ptPcg = teamStats['ptPctg']
            ptPct.append(ptPcg)
            
        for x in range(52, 54):
            r = requests.get("https://statsapi.web.nhl.com//api//v1/teams//" + str(x) + "?expand=team.stats&season=" + str(season))
            obj = json.loads(r.text)
            team = obj["teams"]
            teamStats = team[0]['teamStats'][0]['splits'][0]['stat']
            ptPcg = teamStats['ptPctg']
            ptPct.append(ptPcg)
    else:
        for x in range(1, 11):
            r = requests.get("https://statsapi.web.nhl.com//api//v1/teams//" + str(x) + "?expand=team.stats&season=" + str(season))
            obj = json.loads(r.text)
            team = obj["teams"]
            teamStats = team[0]['teamStats'][0]['splits'][0]['stat']
            ptPcg = teamStats['ptPctg']
            ptPct.append(ptPcg)
    
        for x in range(12, 27):
            r = requests.get("https://statsapi.web.nhl.com//api//v1/teams//" + str(x) + "?expand=team.stats&season=" + str(season))
            obj = json.loads(r.text)
            team = obj["teams"]
            teamStats = team[0]['teamStats'][0]['splits'][0]['stat']
            ptPcg = teamStats['ptPctg']
            ptPct.append(ptPcg)
            
        for x in range(28, 31):
            r = requests.get("https://statsapi.web.nhl.com//api//v1/teams//" + str(x) + "?expand=team.stats&season=" + str(season))
            obj = json.loads(r.text)
            team = obj["teams"]
            teamStats = team[0]['teamStats'][0]['splits'][0]['stat']
            ptPcg = teamStats['ptPctg']
            ptPct.append(ptPcg)
            
        for x in range(52, 55):
            r = requests.get("https://statsapi.web.nhl.com//api//v1/teams//" + str(x) + "?expand=team.stats&season=" + str(season))
            obj = json.loads(r.text)
            team = obj["teams"]
            teamStats = team[0]['teamStats'][0]['splits'][0]['stat']
            ptPcg = teamStats['ptPctg']
            ptPct.append(ptPcg)
    
    return(ptPct)

def goal_rating(season): # Get every teams' goals for - goals against per game 
    if (season == 20102011):
        for x in range(1, 31):
            r = requests.get("https://statsapi.web.nhl.com//api//v1/teams//" + str(x) + "?expand=team.stats&season=" + str(season))
            obj = json.loads(r.text)
            team = obj["teams"]
            teamStats = team[0]['teamStats'][0]['splits'][0]['stat']
            goalsFor = teamStats['goalsPerGame']
            goalsAgainst = teamStats['goalsAgainstPerGame']
            goalScore = goalsFor - goalsAgainst;
            goalRating.append(goalScore)
        
    elif (season == 20112012 or season == 20122013 or season == 20132014):
        for x in range(1, 11):
            r = requests.get("https://statsapi.web.nhl.com//api//v1/teams//" + str(x) + "?expand=team.stats&season=" + str(season))
            obj = json.loads(r.text)
            team = obj["teams"]
            teamStats = team[0]['teamStats'][0]['splits'][0]['stat']
            goalsFor = teamStats['goalsPerGame']
            goalsAgainst = teamStats['goalsAgainstPerGame']
            goalScore = goalsFor - goalsAgainst;
            goalRating.append(goalScore)
    
            
        for x in range(12, 31):
            r = requests.get("https://statsapi.web.nhl.com//api//v1/teams//" + str(x) + "?expand=team.stats&season=" + str(season))
            obj = json.loads(r.text)
            team = obj["teams"]
            teamStats = team[0]['teamStats'][0]['splits'][0]['stat']
            goalsFor = teamStats['goalsPerGame']
            goalsAgainst = teamStats['goalsAgainstPerGame']
            goalScore = goalsFor - goalsAgainst;
            goalRating.append(goalScore)
            
        r = requests.get("https://statsapi.web.nhl.com//api//v1/teams//" + 52 + "?expand=team.stats&season=" + str(season))
        obj = json.loads(r.text)
        team = obj["teams"]
        teamStats = team[0]['teamStats'][0]['splits'][0]['stat']
        goalsFor = teamStats['goalsPerGame']
        goalsAgainst = teamStats['goalsAgainstPerGame']
        goalScore = goalsFor - goalsAgainst;
        goalRating.append(goalScore)
            
    elif (season == 20142015 or season == 20152016 or season == 20162017): # Phoneix Coyotes (27) --> Arizona Coyotes (53)
        for x in range(1, 11):
            r = requests.get("https://statsapi.web.nhl.com//api//v1/teams//" + str(x) + "?expand=team.stats&season=" + str(season))
            obj = json.loads(r.text)
            team = obj["teams"]
            teamStats = team[0]['teamStats'][0]['splits'][0]['stat']
            goalsFor = teamStats['goalsPerGame']
            goalsAgainst = teamStats['goalsAgainstPerGame']
            goalScore = goalsFor - goalsAgainst;
            goalRating.append(goalScore)
    
            
        for x in range(12, 27):
            r = requests.get("https://statsapi.web.nhl.com//api//v1/teams//" + str(x) + "?expand=team.stats&season=" + str(season))
            obj = json.loads(r.text)
            team = obj["teams"]
            teamStats = team[0]['teamStats'][0]['splits'][0]['stat']
            goalsFor = teamStats['goalsPerGame']
            goalsAgainst = teamStats['goalsAgainstPerGame']
            goalScore = goalsFor - goalsAgainst;
            goalRating.append(goalScore)
            
        for x in range(28, 31):
            r = requests.get("https://statsapi.web.nhl.com//api//v1/teams//" + str(x) + "?expand=team.stats&season=" + str(season))
            obj = json.loads(r.text)
            team = obj["teams"]
            teamStats = team[0]['teamStats'][0]['splits'][0]['stat']
            goalsFor = teamStats['goalsPerGame']
            goalsAgainst = teamStats['goalsAgainstPerGame']
            goalScore = goalsFor - goalsAgainst;
            goalRating.append(goalScore)
            
        for x in range(52, 54):
            r = requests.get("https://statsapi.web.nhl.com//api//v1/teams//" + str(x) + "?expand=team.stats&season=" + str(season))
            obj = json.loads(r.text)
            team = obj["teams"]
            teamStats = team[0]['teamStats'][0]['splits'][0]['stat']
            goalsFor = teamStats['goalsPerGame']
            goalsAgainst = teamStats['goalsAgainstPerGame']
            goalScore = goalsFor - goalsAgainst;
            goalRating.append(goalScore)
            
    else:
        for x in range(1, 11):
            r = requests.get("https://statsapi.web.nhl.com//api//v1/teams//" + str(x) + "?expand=team.stats&season=" + str(season))
            obj = json.loads(r.text)
            team = obj["teams"]
            teamStats = team[0]['teamStats'][0]['splits'][0]['stat']
            goalsFor = teamStats['goalsPerGame']
            goalsAgainst = teamStats['goalsAgainstPerGame']
            goalScore = goalsFor - goalsAgainst;
            goalRating.append(goalScore)
    
            
        for x in range(12, 27):
            r = requests.get("https://statsapi.web.nhl.com//api//v1/teams//" + str(x) + "?expand=team.stats&season=" + str(season))
            obj = json.loads(r.text)
            team = obj["teams"]
            teamStats = team[0]['teamStats'][0]['splits'][0]['stat']
            goalsFor = teamStats['goalsPerGame']
            goalsAgainst = teamStats['goalsAgainstPerGame']
            goalScore = goalsFor - goalsAgainst;
            goalRating.append(goalScore)
            
        for x in range(28, 31):
            r = requests.get("https://statsapi.web.nhl.com//api//v1/teams//" + str(x) + "?expand=team.stats&season=" + str(season))
            obj = json.loads(r.text)
            team = obj["teams"]
            teamStats = team[0]['teamStats'][0]['splits'][0]['stat']
            goalsFor = teamStats['goalsPerGame']
            goalsAgainst = teamStats['goalsAgainstPerGame']
            goalScore = goalsFor - goalsAgainst;
            goalRating.append(goalScore)
            
        for x in range(52, 55):
            r = requests.get("https://statsapi.web.nhl.com//api//v1/teams//" + str(x) + "?expand=team.stats&season=" + str(season))
            obj = json.loads(r.text)
            team = obj["teams"]
            teamStats = team[0]['teamStats'][0]['splits'][0]['stat']
            goalsFor = teamStats['goalsPerGame']
            goalsAgainst = teamStats['goalsAgainstPerGame']
            goalScore = goalsFor - goalsAgainst;
            goalRating.append(goalScore)
    
    return(goalRating)

def score_first(season):    # Get every teams' win percentage when scoring first - opponent scores first 
    if (season == 20102011):
        for x in range(1, 31):  # 1 -10
            r = requests.get("https://statsapi.web.nhl.com//api//v1/teams//" + str(x) + "?expand=team.stats&season=" + str(season))
            obj = json.loads(r.text)
            team = obj["teams"]
            teamStats = team[0]['teamStats'][0]['splits'][0]['stat']
            winScoreFirst = teamStats['winScoreFirst'] * .4
            winOppScoreFirst = teamStats['winOppScoreFirst'] * .6
            score_first_score = winScoreFirst + winOppScoreFirst
            scoreFirst.append(score_first_score)
            
    elif (season == 20112012 or season == 20122013 or season == 20132014):
        for x in range(1, 11):  # 1 -10
            r = requests.get("https://statsapi.web.nhl.com//api//v1/teams//" + str(x) + "?expand=team.stats&season=" + str(season))
            obj = json.loads(r.text)
            team = obj["teams"]
            teamStats = team[0]['teamStats'][0]['splits'][0]['stat']
            winScoreFirst = teamStats['winScoreFirst'] * .4
            winOppScoreFirst = teamStats['winOppScoreFirst'] * .6
            score_first_score = winScoreFirst + winOppScoreFirst
            scoreFirst.append(score_first_score)
            
        for x in range(12, 31):
            r = requests.get("https://statsapi.web.nhl.com//api//v1/teams//" + str(x) + "?expand=team.stats&season=" + str(season))
            obj = json.loads(r.text)
            team = obj["teams"]
            teamStats = team[0]['teamStats'][0]['splits'][0]['stat']
            winScoreFirst = teamStats['winScoreFirst'] * .4
            winOppScoreFirst = teamStats['winOppScoreFirst'] * .6
            score_first_score = winScoreFirst + winOppScoreFirst
            scoreFirst.append(score_first_score)
            
        r = requests.get("https://statsapi.web.nhl.com//api//v1/teams//" + 52 + "?expand=team.stats&season=" + str(season))
        obj = json.loads(r.text)
        team = obj["teams"]
        teamStats = team[0]['teamStats'][0]['splits'][0]['stat']
        winScoreFirst = teamStats['winScoreFirst'] * .4
        winOppScoreFirst = teamStats['winOppScoreFirst'] * .6
        score_first_score = winScoreFirst + winOppScoreFirst
        scoreFirst.append(score_first_score)
            
    elif (season == 20142015 or season == 20152016 or season == 20162017): # Phoneix Coyotes (27) --> Arizona Coyotes (53)
        for x in range(1, 11):  # 1 -10
            r = requests.get("https://statsapi.web.nhl.com//api//v1/teams//" + str(x) + "?expand=team.stats&season=" + str(season))
            obj = json.loads(r.text)
            team = obj["teams"]
            teamStats = team[0]['teamStats'][0]['splits'][0]['stat']
            winScoreFirst = teamStats['winScoreFirst'] * .4
            winOppScoreFirst = teamStats['winOppScoreFirst'] * .6
            score_first_score = winScoreFirst + winOppScoreFirst
            scoreFirst.append(score_first_score)
            
        for x in range(12, 27):
            r = requests.get("https://statsapi.web.nhl.com//api//v1/teams//" + str(x) + "?expand=team.stats&season=" + str(season))
            obj = json.loads(r.text)
            team = obj["teams"]
            teamStats = team[0]['teamStats'][0]['splits'][0]['stat']
            winScoreFirst = teamStats['winScoreFirst'] * .4
            winOppScoreFirst = teamStats['winOppScoreFirst'] * .6
            score_first_score = winScoreFirst + winOppScoreFirst
            scoreFirst.append(score_first_score)
            
        for x in range(28, 31):
            r = requests.get("https://statsapi.web.nhl.com//api//v1/teams//" + str(x) + "?expand=team.stats&season=" + str(season))
            obj = json.loads(r.text)
            team = obj["teams"]
            teamStats = team[0]['teamStats'][0]['splits'][0]['stat']
            winScoreFirst = teamStats['winScoreFirst'] * .4
            winOppScoreFirst = teamStats['winOppScoreFirst'] * .6
            score_first_score = winScoreFirst + winOppScoreFirst
            scoreFirst.append(score_first_score)
            
        for x in range(52, 54):
            r = requests.get("https://statsapi.web.nhl.com//api//v1/teams//" + str(x) + "?expand=team.stats&season=" + str(season))
            obj = json.loads(r.text)
            team = obj["teams"]
            teamStats = team[0]['teamStats'][0]['splits'][0]['stat']
            winScoreFirst = teamStats['winScoreFirst'] * .4
            winOppScoreFirst = teamStats['winOppScoreFirst'] * .6
            score_first_score = winScoreFirst + winOppScoreFirst
            scoreFirst.append(score_first_score)
            
    else:   
        for x in range(1, 11):  # 1 -10
            r = requests.get("https://statsapi.web.nhl.com//api//v1/teams//" + str(x) + "?expand=team.stats&season=" + str(season))
            obj = json.loads(r.text)
            team = obj["teams"]
            teamStats = team[0]['teamStats'][0]['splits'][0]['stat']
            winScoreFirst = teamStats['winScoreFirst'] * .4
            winOppScoreFirst = teamStats['winOppScoreFirst'] * .6
            score_first_score = winScoreFirst + winOppScoreFirst
            scoreFirst.append(score_first_score)
            
        for x in range(12, 27):
            r = requests.get("https://statsapi.web.nhl.com//api//v1/teams//" + str(x) + "?expand=team.stats&season=" + str(season))
            obj = json.loads(r.text)
            team = obj["teams"]
            teamStats = team[0]['teamStats'][0]['splits'][0]['stat']
            winScoreFirst = teamStats['winScoreFirst'] * .4
            winOppScoreFirst = teamStats['winOppScoreFirst'] * .6
            score_first_score = winScoreFirst + winOppScoreFirst
            scoreFirst.append(score_first_score)
            
        for x in range(28, 31):
            r = requests.get("https://statsapi.web.nhl.com//api//v1/teams//" + str(x) + "?expand=team.stats&season=" + str(season))
            obj = json.loads(r.text)
            team = obj["teams"]
            teamStats = team[0]['teamStats'][0]['splits'][0]['stat']
            winScoreFirst = teamStats['winScoreFirst'] * .4
            winOppScoreFirst = teamStats['winOppScoreFirst'] * .6
            score_first_score = winScoreFirst + winOppScoreFirst
            scoreFirst.append(score_first_score)
            
        for x in range(52, 55):
            r = requests.get("https://statsapi.web.nhl.com//api//v1/teams//" + str(x) + "?expand=team.stats&season=" + str(season))
            obj = json.loads(r.text)
            team = obj["teams"]
            teamStats = team[0]['teamStats'][0]['splits'][0]['stat']
            winScoreFirst = teamStats['winScoreFirst'] * .4
            winOppScoreFirst = teamStats['winOppScoreFirst'] * .6
            score_first_score = winScoreFirst + winOppScoreFirst
            scoreFirst.append(score_first_score)
    
    return(scoreFirst)

def lead_first(season):     # get every teams' win percentage when leading in the first period - leading in second period
    if (season == 20102011):
        for x in range(1, 31):  # 1 - 10
            r = requests.get("https://statsapi.web.nhl.com//api//v1/teams//" + str(x) + "?expand=team.stats&season=" + str(season))
            obj = json.loads(r.text)
            team = obj["teams"]
            teamStats = team[0]['teamStats'][0]['splits'][0]['stat']
            winLeadFirst = teamStats['winLeadFirstPer'] * .4
            winLeadSecond = teamStats['winLeadSecondPer'] * .6
            lead_first_score = winLeadFirst + winLeadSecond
            leadFirst.append(lead_first_score)
            
    elif (season == 20112012 or season == 20122013 or season == 20132014):
        for x in range(1, 11):  # 1 - 10
            r = requests.get("https://statsapi.web.nhl.com//api//v1/teams//" + str(x) + "?expand=team.stats&season=" + str(season))
            obj = json.loads(r.text)
            team = obj["teams"]
            teamStats = team[0]['teamStats'][0]['splits'][0]['stat']
            winLeadFirst = teamStats['winLeadFirstPer'] * .4
            winLeadSecond = teamStats['winLeadSecondPer'] * .6
            lead_first_score = winLeadFirst + winLeadSecond
            leadFirst.append(lead_first_score)
            
        for x in range(12, 31):
            r = requests.get("https://statsapi.web.nhl.com//api//v1/teams//" + str(x) + "?expand=team.stats&season=" + str(season))
            obj = json.loads(r.text)
            team = obj["teams"]
            teamStats = team[0]['teamStats'][0]['splits'][0]['stat']
            winLeadFirst = teamStats['winLeadFirstPer'] * .4
            winLeadSecond = teamStats['winLeadSecondPer'] * .6
            lead_first_score = winLeadFirst + winLeadSecond
            leadFirst.append(lead_first_score)
            
        r = requests.get("https://statsapi.web.nhl.com//api//v1/teams//" + 52 + "?expand=team.stats&season=" + str(season))
        obj = json.loads(r.text)
        team = obj["teams"]
        teamStats = team[0]['teamStats'][0]['splits'][0]['stat']
        winLeadFirst = teamStats['winLeadFirstPer'] * .4
        winLeadSecond = teamStats['winLeadSecondPer'] * .6
        lead_first_score = winLeadFirst + winLeadSecond
        leadFirst.append(lead_first_score)
            
    elif (season == 20142015 or season == 20152016 or season == 20162017): # Phoneix Coyotes (27) --> Arizona Coyotes (53)
        for x in range(1, 11):  # 1 - 10
            r = requests.get("https://statsapi.web.nhl.com//api//v1/teams//" + str(x) + "?expand=team.stats&season=" + str(season))
            obj = json.loads(r.text)
            team = obj["teams"]
            teamStats = team[0]['teamStats'][0]['splits'][0]['stat']
            winLeadFirst = teamStats['winLeadFirstPer'] * .4
            winLeadSecond = teamStats['winLeadSecondPer'] * .6
            lead_first_score = winLeadFirst + winLeadSecond
            leadFirst.append(lead_first_score)
            
        for x in range(12, 27):
            r = requests.get("https://statsapi.web.nhl.com//api//v1/teams//" + str(x) + "?expand=team.stats&season=" + str(season))
            obj = json.loads(r.text)
            team = obj["teams"]
            teamStats = team[0]['teamStats'][0]['splits'][0]['stat']
            winLeadFirst = teamStats['winLeadFirstPer'] * .4
            winLeadSecond = teamStats['winLeadSecondPer'] * .6
            lead_first_score = winLeadFirst + winLeadSecond
            leadFirst.append(lead_first_score)
            
        for x in range(28, 31):
            r = requests.get("https://statsapi.web.nhl.com//api//v1/teams//" + str(x) + "?expand=team.stats&season=" + str(season))
            obj = json.loads(r.text)
            team = obj["teams"]
            teamStats = team[0]['teamStats'][0]['splits'][0]['stat']
            winLeadFirst = teamStats['winLeadFirstPer'] * .4
            winLeadSecond = teamStats['winLeadSecondPer'] * .6
            lead_first_score = winLeadFirst + winLeadSecond
            leadFirst.append(lead_first_score)
            
        for x in range(52, 54):
            r = requests.get("https://statsapi.web.nhl.com//api//v1/teams//" + str(x) + "?expand=team.stats&season=" + str(season))
            obj = json.loads(r.text)
            team = obj["teams"]
            teamStats = team[0]['teamStats'][0]['splits'][0]['stat']
            winLeadFirst = teamStats['winLeadFirstPer'] * .4
            winLeadSecond = teamStats['winLeadSecondPer'] * .6
            lead_first_score = winLeadFirst + winLeadSecond
            leadFirst.append(lead_first_score)
            
    else:
        for x in range(1, 11):  # 1 - 10
            r = requests.get("https://statsapi.web.nhl.com//api//v1/teams//" + str(x) + "?expand=team.stats&season=" + str(season))
            obj = json.loads(r.text)
            team = obj["teams"]
            teamStats = team[0]['teamStats'][0]['splits'][0]['stat']
            winLeadFirst = teamStats['winLeadFirstPer'] * .4
            winLeadSecond = teamStats['winLeadSecondPer'] * .6
            lead_first_score = winLeadFirst + winLeadSecond
            leadFirst.append(lead_first_score)
            
        for x in range(12, 27):
            r = requests.get("https://statsapi.web.nhl.com//api//v1/teams//" + str(x) + "?expand=team.stats&season=" + str(season))
            obj = json.loads(r.text)
            team = obj["teams"]
            teamStats = team[0]['teamStats'][0]['splits'][0]['stat']
            winLeadFirst = teamStats['winLeadFirstPer'] * .4
            winLeadSecond = teamStats['winLeadSecondPer'] * .6
            lead_first_score = winLeadFirst + winLeadSecond
            leadFirst.append(lead_first_score)
            
        for x in range(28, 31):
            r = requests.get("https://statsapi.web.nhl.com//api//v1/teams//" + str(x) + "?expand=team.stats&season=" + str(season))
            obj = json.loads(r.text)
            team = obj["teams"]
            teamStats = team[0]['teamStats'][0]['splits'][0]['stat']
            winLeadFirst = teamStats['winLeadFirstPer'] * .4
            winLeadSecond = teamStats['winLeadSecondPer'] * .6
            lead_first_score = winLeadFirst + winLeadSecond
            leadFirst.append(lead_first_score)
            
        for x in range(52, 55):
            r = requests.get("https://statsapi.web.nhl.com//api//v1/teams//" + str(x) + "?expand=team.stats&season=" + str(season))
            obj = json.loads(r.text)
            team = obj["teams"]
            teamStats = team[0]['teamStats'][0]['splits'][0]['stat']
            winLeadFirst = teamStats['winLeadFirstPer'] * .4
            winLeadSecond = teamStats['winLeadSecondPer'] * .6
            lead_first_score = winLeadFirst + winLeadSecond
            leadFirst.append(lead_first_score)
    
    return(leadFirst)

def out_shoot(season):      # Get every teams wins percentage when outshooting the opponent - being outshot by the opponent
    if (season == 20102011):
        for x in range(1, 31):  # 1 - 10
                r = requests.get("https://statsapi.web.nhl.com//api//v1/teams//" + str(x) + "?expand=team.stats&season=" + str(season))
                obj = json.loads(r.text)
                team = obj["teams"]
                teamStats = team[0]['teamStats'][0]['splits'][0]['stat']
                winOutshootOpp = teamStats['winOutshootOpp'] * .4
                winOutshotByOpp = teamStats['winOutshotByOpp'] * .6
                out_shoot_score = winOutshootOpp + winOutshotByOpp
                outShoot.append(out_shoot_score)
                
    elif (season == 20112012 or season == 20122013 or season == 20132014):
        for x in range(1, 11):  # 1 - 10
                r = requests.get("https://statsapi.web.nhl.com//api//v1/teams//" + str(x) + "?expand=team.stats&season=" + str(season))
                obj = json.loads(r.text)
                team = obj["teams"]
                teamStats = team[0]['teamStats'][0]['splits'][0]['stat']
                winOutshootOpp = teamStats['winOutshootOpp'] * .4
                winOutshotByOpp = teamStats['winOutshotByOpp'] * .6
                out_shoot_score = winOutshootOpp + winOutshotByOpp
                outShoot.append(out_shoot_score)
            
        for x in range(12, 31):
            r = requests.get("https://statsapi.web.nhl.com//api//v1/teams//" + str(x) + "?expand=team.stats&season=" + str(season))
            obj = json.loads(r.text)
            team = obj["teams"]
            teamStats = team[0]['teamStats'][0]['splits'][0]['stat']
            winOutshootOpp = teamStats['winOutshootOpp'] * .4
            winOutshotByOpp = teamStats['winOutshotByOpp'] * .6
            out_shoot_score = winOutshootOpp + winOutshotByOpp
            outShoot.append(out_shoot_score)
            
        r = requests.get("https://statsapi.web.nhl.com//api//v1/teams//" + 52 + "?expand=team.stats&season=" + str(season))
        obj = json.loads(r.text)
        team = obj["teams"]
        teamStats = team[0]['teamStats'][0]['splits'][0]['stat']
        winOutshootOpp = teamStats['winOutshootOpp'] * .4
        winOutshotByOpp = teamStats['winOutshotByOpp'] * .6
        out_shoot_score = winOutshootOpp + winOutshotByOpp
        outShoot.append(out_shoot_score)
            
    elif (season == 20142015 or season == 20152016 or season == 20162017): # Phoneix Coyotes (27) --> Arizona Coyotes (53)
        for x in range(1, 11):  # 1 - 10
                r = requests.get("https://statsapi.web.nhl.com//api//v1/teams//" + str(x) + "?expand=team.stats&season=" + str(season))
                obj = json.loads(r.text)
                team = obj["teams"]
                teamStats = team[0]['teamStats'][0]['splits'][0]['stat']
                winOutshootOpp = teamStats['winOutshootOpp'] * .4
                winOutshotByOpp = teamStats['winOutshotByOpp'] * .6
                out_shoot_score = winOutshootOpp + winOutshotByOpp
                outShoot.append(out_shoot_score)
            
        for x in range(12, 27):
            r = requests.get("https://statsapi.web.nhl.com//api//v1/teams//" + str(x) + "?expand=team.stats&season=" + str(season))
            obj = json.loads(r.text)
            team = obj["teams"]
            teamStats = team[0]['teamStats'][0]['splits'][0]['stat']
            winOutshootOpp = teamStats['winOutshootOpp'] * .4
            winOutshotByOpp = teamStats['winOutshotByOpp'] * .6
            out_shoot_score = winOutshootOpp + winOutshotByOpp
            outShoot.append(out_shoot_score)
            
        for x in range(28, 31):
            r = requests.get("https://statsapi.web.nhl.com//api//v1/teams//" + str(x) + "?expand=team.stats&season=" + str(season))
            obj = json.loads(r.text)
            team = obj["teams"]
            teamStats = team[0]['teamStats'][0]['splits'][0]['stat']
            winOutshootOpp = teamStats['winOutshootOpp'] * .4
            winOutshotByOpp = teamStats['winOutshotByOpp'] * .6
            out_shoot_score = winOutshootOpp + winOutshotByOpp
            outShoot.append(out_shoot_score)
            
        for x in range(52, 54):
            r = requests.get("https://statsapi.web.nhl.com//api//v1/teams//" + str(x) + "?expand=team.stats&season=" + str(season))
            obj = json.loads(r.text)
            team = obj["teams"]
            teamStats = team[0]['teamStats'][0]['splits'][0]['stat']
            winOutshootOpp = teamStats['winOutshootOpp'] * .4
            winOutshotByOpp = teamStats['winOutshotByOpp'] * .6
            out_shoot_score = winOutshootOpp + winOutshotByOpp
            outShoot.append(out_shoot_score)
    else:    
        for x in range(1, 11):  # 1 - 10
                r = requests.get("https://statsapi.web.nhl.com//api//v1/teams//" + str(x) + "?expand=team.stats&season=" + str(season))
                obj = json.loads(r.text)
                team = obj["teams"]
                teamStats = team[0]['teamStats'][0]['splits'][0]['stat']
                winOutshootOpp = teamStats['winOutshootOpp'] * .4
                winOutshotByOpp = teamStats['winOutshotByOpp'] * .6
                out_shoot_score = winOutshootOpp + winOutshotByOpp
                outShoot.append(out_shoot_score)
            
        for x in range(12, 27):
            r = requests.get("https://statsapi.web.nhl.com//api//v1/teams//" + str(x) + "?expand=team.stats&season=" + str(season))
            obj = json.loads(r.text)
            team = obj["teams"]
            teamStats = team[0]['teamStats'][0]['splits'][0]['stat']
            winOutshootOpp = teamStats['winOutshootOpp'] * .4
            winOutshotByOpp = teamStats['winOutshotByOpp'] * .6
            out_shoot_score = winOutshootOpp + winOutshotByOpp
            outShoot.append(out_shoot_score)
            
        for x in range(28, 31):
            r = requests.get("https://statsapi.web.nhl.com//api//v1/teams//" + str(x) + "?expand=team.stats&season=" + str(season))
            obj = json.loads(r.text)
            team = obj["teams"]
            teamStats = team[0]['teamStats'][0]['splits'][0]['stat']
            winOutshootOpp = teamStats['winOutshootOpp'] * .4
            winOutshotByOpp = teamStats['winOutshotByOpp'] * .6
            out_shoot_score = winOutshootOpp + winOutshotByOpp
            outShoot.append(out_shoot_score)
            
        for x in range(52, 55):
            r = requests.get("https://statsapi.web.nhl.com//api//v1/teams//" + str(x) + "?expand=team.stats&season=" + str(season))
            obj = json.loads(r.text)
            team = obj["teams"]
            teamStats = team[0]['teamStats'][0]['splits'][0]['stat']
            winOutshootOpp = teamStats['winOutshootOpp'] * .4
            winOutshotByOpp = teamStats['winOutshotByOpp'] * .6
            out_shoot_score = winOutshootOpp + winOutshotByOpp
            outShoot.append(out_shoot_score)
    
    return(outShoot)

def team_score(season):
    if (season == 20102011 or season == 20112012 or season == 20122013 or season == 20132014 or season == 20142015 or season == 20152016 or season == 20162017):
        for x in range(0, 30):
            team_Score = (float(winPctTrain[x]) +  (float(ptPct[x])) + float(goalRating[x]) + float(scoreFirst[x]) + float(leadFirst[x]) + float(outShoot[x]))
            teamScore.append(team_Score)
            
    else:
        for x in range(0, 31):
            team_Score = (float(winPctTrain[x]) +  (float(ptPct[x])) + float(goalRating[x]) + float(scoreFirst[x]) + float(leadFirst[x]) + float(outShoot[x]))
            teamScore.append(team_Score)
    
    return teamScore



    
def dataWriter():
    winPctTrain.clear()
    ptPct.clear()
    goalRating.clear()
    scoreFirst.clear()
    leadFirst.clear()
    outShoot.clear()
    teamScore.clear()
    teamID.clear()
    teamFullName.clear()

    W_Pct(20152016)
    P_Pct(20152016)
    goal_rating(20152016)
    score_first(20152016)
    lead_first(20152016)
    out_shoot(20152016)
    team_score(20152016)
    team_Info(20152016)
    
    sheet1.write(0,0,"Season: 2015 - 2016")
    sheet1.write(1,0,"Team Name")
    sheet1.write(1,1,"Team ID")
    sheet1.write(1,2,"Winning Percentage")
    sheet1.write(1,3,"Point Percentage")
    sheet1.write(1,4,"Goal Rating")
    sheet1.write(1,5,"Score First Score")
    sheet1.write(1,6,"Lead First Score")
    sheet1.write(1,7,"Out Shoot Score")
    sheet1.write(1,8,"Overall Team Score")
    
    for x in range(0, 30):
        sheet1.write(x+2,0, teamFullName[x])
        sheet1.write(x+2,1, teamID[x])
        sheet1.write(x+2,2, winPctTrain[x])
        sheet1.write(x+2,3, ptPct[x])
        sheet1.write(x+2,4, goalRating[x])
        sheet1.write(x+2,5, scoreFirst[x])
        sheet1.write(x+2,6, leadFirst[x])
        sheet1.write(x+2,7, outShoot[x])
        sheet1.write(x+2,8, teamScore[x])
    
    W_Pct(20162017)
    P_Pct(20162017)
    goal_rating(20162017)
    score_first(20162017)
    lead_first(20162017)
    out_shoot(20162017)
    team_score(20162017)
    team_Info(20162017)
    
    sheet2.write(0,0,"Season: 2016 - 2017")
    sheet2.write(1,0,"Team Name")
    sheet2.write(1,1,"Team ID")
    sheet2.write(1,2,"Winning Percentage")
    sheet2.write(1,3,"Point Percentage")
    sheet2.write(1,4,"Goal Rating")
    sheet2.write(1,5,"Score First Score")
    sheet2.write(1,6,"Lead First Score")
    sheet2.write(1,7,"Out Shoot Score")
    sheet2.write(1,8,"Overall Team Score")
    
    for x in range(0, 30):
        sheet2.write(x+2,0, teamFullName[x])
        sheet2.write(x+2,1, teamID[x])
        sheet2.write(x+2,2, winPctTrain[x])
        sheet2.write(x+2,3, ptPct[x])
        sheet2.write(x+2,4, goalRating[x])
        sheet2.write(x+2,5, scoreFirst[x])
        sheet2.write(x+2,6, leadFirst[x])
        sheet2.write(x+2,7, outShoot[x])
        sheet2.write(x+2,8, teamScore[x])
        
    print("Done")
        
    W_Pct(20172018)
    P_Pct(20172018)
    goal_rating(20172018)
    score_first(20172018)
    lead_first(20172018)
    out_shoot(20172018)
    team_score(20172018)
    team_Info(20172018)
    
    sheet3.write(0,0,"Season: 2017 - 2018")
    sheet3.write(1,0,"Team Name")
    sheet3.write(1,1,"Team ID")
    sheet3.write(1,2,"Winning Percentage")
    sheet3.write(1,3,"Point Percentage")
    sheet3.write(1,4,"Goal Rating")
    sheet3.write(1,5,"Score First Score")
    sheet3.write(1,6,"Lead First Score")
    sheet3.write(1,7,"Out Shoot Score")
    sheet3.write(1,8,"Overall Team Score")
    
    for x in range(0, 31):
        sheet3.write(x+2,0, teamFullName[x])
        sheet3.write(x+2,1, teamID[x])
        sheet3.write(x+2,2, winPctTrain[x])
        sheet3.write(x+2,3, ptPct[x])
        sheet3.write(x+2,4, goalRating[x])
        sheet3.write(x+2,5, scoreFirst[x])
        sheet3.write(x+2,6, leadFirst[x])
        sheet3.write(x+2,7, outShoot[x])
        sheet3.write(x+2,8, teamScore[x])
    
    print("Done")
        
    W_Pct(20182019)
    P_Pct(20182019)
    goal_rating(20182019)
    score_first(20182019)
    lead_first(20182019)
    out_shoot(20182019)
    team_score(20182019)
    team_Info(20182019)
    
    sheet4.write(0,0,"Season: 2018 - 2019")
    sheet4.write(1,0,"Team Name")
    sheet4.write(1,1,"Team ID")
    sheet4.write(1,2,"Winning Percentage")
    sheet4.write(1,3,"Point Percentage")
    sheet4.write(1,4,"Goal Rating")
    sheet4.write(1,5,"Score First Score")
    sheet4.write(1,6,"Lead First Score")
    sheet4.write(1,7,"Out Shoot Score")
    sheet4.write(1,8,"Overall Team Score")
    
    for x in range(0, 31):
        sheet4.write(x+2,0, teamFullName[x])
        sheet4.write(x+2,1, teamID[x])
        sheet4.write(x+2,2, winPctTrain[x])
        sheet4.write(x+2,3, ptPct[x])
        sheet4.write(x+2,4, goalRating[x])
        sheet4.write(x+2,5, scoreFirst[x])
        sheet4.write(x+2,6, leadFirst[x])
        sheet4.write(x+2,7, outShoot[x])
        sheet4.write(x+2,8, teamScore[x])
        
    wb.save('teamscore.xls')

        
    

dataWriter()

"""
print(len(winPctTrain))
print(len(ptPct))
print(len(goalRating))
print(len(scoreFirst))
print(len(leadFirst))
print(len(outShoot))
print(len(teamFullName))
print(len(teamID))


winPctTrain = []
ptPct = []
goalRating = []
scoreFirst = []
leadFirst = []
outShoot = []
teamScore = []
teamID = []
teamFullName = []
"""
    
 

