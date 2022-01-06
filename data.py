from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
import json
import pandas as pd
import requests
import numpy as np
from sklearn.metrics import classification_report,confusion_matrix

winPctTrain = []
ptPct = []
goalRating = []
scoreFirst = []
leadFirst = []
outShoot = []
teamScore = []
prediction = []
teamID = []
teamFullName = []

def trainFunction(teamID, season):
    r = requests.get("https://statsapi.web.nhl.com//api//v1/teams//" + str(teamID) + "//stats?season=" + str(season))
    obj = json.loads(r.text)
    splitStats = obj["stats"][0]["splits"]
    stats = splitStats[0]["stat"]
    fWP = stats["faceOffWinPercentage"]        # Face off win percentage
    
    # Season win percentage 
    wins = stats["wins"]
    gamesP = stats["gamesPlayed"]
    wP = wins / gamesP
    
    pP = stats["ptPctg"]                # Season point percentage
    
    # Goal rating
    goalsFor = stats['goalsPerGame']
    goalsAgainst = stats['goalsAgainstPerGame']
    gS = goalsFor - goalsAgainst;
    
    # scoreFirst
    scFirstWP = stats["winScoreFirst"] * .4
    oppScFirstWP = stats["winOppScoreFirst"] * .6
    sF = scFirstWP + oppScFirstWP
    
    # leadFirst
    winLeadFirst = stats['winLeadFirstPer'] * .4
    winLeadSecond = stats['winLeadSecondPer'] * .6
    lF = winLeadFirst + winLeadSecond
    
    # outShoot
    winOutshootOpp = stats['winOutshootOpp'] * .4
    winOutshotByOpp = stats['winOutshotByOpp'] * .6
    oS = winOutshootOpp + winOutshotByOpp
    
    # teamSeasonScore
    tS = (((float(gS) + float(sF) + float(lF) + float(oS)) / 4) + ((float(pP)) / 100))
    

    dataset = []
    dataset.append(fWP)
    dataset.append(wP)
    dataset.append(pP)
    dataset.append(gS)
    dataset.append(sF)
    dataset.append(lF)
    dataset.append(oS)
    dataset.append(tS)
    
    return dataset
    
            

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
            winPctTrain.append(winPct)
    
    return(winPctTrain)

def t_W_Pct(id, season):
    r = requests.get("https://statsapi.web.nhl.com//api//v1/teams//" + str(id) + "?expand=team.stats&season=" + str(season))
    obj = json.loads(r.text)
    team = obj["teams"]
    teamStats = team[0]['teamStats'][0]['splits'][0]['stat']
    teamWin = teamStats['wins']
    teamGP = teamStats['gamesPlayed']
    winPct = teamWin / teamGP
    return winPct

def P_Pct(season): # Get every teams point percentage
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

def t_P_Pct(id, season):
    r = requests.get("https://statsapi.web.nhl.com//api//v1/teams//" + str(id) + "?expand=team.stats&season=" + str(season))
    obj = json.loads(r.text)
    team = obj["teams"]
    teamStats = team[0]['teamStats'][0]['splits'][0]['stat']
    ptPcg = teamStats['ptPctg']
    return ptPcg


    
def goal_rating(season): # Get every teams' goals for - goals against per game 
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

def t_goal_rating(id, season):
    r = requests.get("https://statsapi.web.nhl.com//api//v1/teams//" + str(id) + "?expand=team.stats&season=" + str(season))
    obj = json.loads(r.text)
    team = obj["teams"]
    teamStats = team[0]['teamStats'][0]['splits'][0]['stat']
    goalsFor = teamStats['goalsPerGame']
    goalsAgainst = teamStats['goalsAgainstPerGame']
    goalScore = goalsFor - goalsAgainst;
    return goalScore
    
def score_first(season):    # Get every teams' win percentage when scoring first - opponent scores first 
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

def t_score_first(id, season):
    r = requests.get("https://statsapi.web.nhl.com//api//v1/teams//" + str(id) + "?expand=team.stats&season=" + str(season))
    obj = json.loads(r.text)
    team = obj["teams"]
    teamStats = team[0]['teamStats'][0]['splits'][0]['stat']
    winScoreFirst = teamStats['winScoreFirst'] * .4
    winOppScoreFirst = teamStats['winOppScoreFirst'] * .6
    score_first_score = winScoreFirst + winOppScoreFirst
    return score_first_score
    
def lead_first(season):     # get every teams' win percentage when leading in the first period - leading in second period
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

def t_lead_first(id, season):
    r = requests.get("https://statsapi.web.nhl.com//api//v1/teams//" + str(id) + "?expand=team.stats&season=" + str(season))
    obj = json.loads(r.text)
    team = obj["teams"]
    teamStats = team[0]['teamStats'][0]['splits'][0]['stat']
    winLeadFirst = teamStats['winLeadFirstPer'] * .4
    winLeadSecond = teamStats['winLeadSecondPer'] * .6
    lead_first_score = winLeadFirst + winLeadSecond
    return lead_first_score
    
def out_shoot(season):      # Get every teams wins percentage when outshooting the opponent - being outshot by the opponent
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

def t_out_shoot(id, season):
    r = requests.get("https://statsapi.web.nhl.com//api//v1/teams//" + str(id) + "?expand=team.stats&season=" + str(season))
    obj = json.loads(r.text)
    team = obj["teams"]
    teamStats = team[0]['teamStats'][0]['splits'][0]['stat']
    winOutshootOpp = teamStats['winOutshootOpp'] * .4
    winOutshotByOpp = teamStats['winOutshotByOpp'] * .6
    out_shoot_score = winOutshootOpp + winOutshotByOpp
    return out_shoot_score
    
def team_score(id):
    team_Score = (float(winPctTrain[id]) +  (float(ptPct[id])) + float(goalRating[id]) + float(scoreFirst[id]) + float(leadFirst[id]) + float(outShoot[id]))
    return team_Score
        
def game_prediction(id1, id2, season):
    prevSeason = season - 1
    fullSeason = int(str(prevSeason) + str(season))
    team_Info(fullSeason)
    nameA = str(teamFullName[id1 - 1])
    nameB = str(teamFullName[id2 - 1])
    
    team1SS = []
    team1GS = []
    team2SS = []
    team2GS = []
    
    aScore = []
    bScore = []
    


    gameStats = open('gameStatsJSON.json',)
    obj = json.load(gameStats)
    for x in obj:
        gameid = str(x["game_id"])
        actualID = gameid[0:4]
        hID = x["home_team_id"]
        aID = x["away_team_id"]
        if(int(actualID) == season and hID == id1 and aID == id2):
            team1SS.append(x["teamSeasonScore"])
            team1GS.append(x["gameScore"])
        elif(int(actualID) == season and hID == id2 and aID == id1):
            team2SS.append(x["teamSeasonScore"])
            team2GS.append(x["gameScore"])

            
    if (team1GS[0] != 0):
        team1AvgGS = np.mean(team1GS)
        team2AvgGS = np.mean(team2GS)
        
        if (team1AvgGS > team2AvgGS):
            winner = nameA
        elif (team2AvgGS > team1AvgGS):
            winner = nameB
        else:
            if(team1SS[0] > team2SS[0]):
                winner = nameA
            elif(team2SS[0] > team1SS[0]):
                winner = nameB
            
        data = {'Season': fullSeason, 'Team A': nameA, 'Team B': nameB, 'Team A Game Scores': team1GS, 'Team B Game Scores': team2GS, 'Team A Average Game Score': team1AvgGS, 'Team B Average Game Score': team2AvgGS, 'Team A Season Score': team1SS[0], 'Team B Season Score': team2SS[0], 'Winner': winner}

    else:
        print( "These two teams have not played in the specified season")
        print("Predicting Winner")
        for x in obj:
            gameid = str(x["game_id"])
            actualID = gameid[0:4]
            hID = x["home_team_id"]
            aID = x["away_team_id"]
            if(int(actualID) == season and (hID == id1 or aID == id1)):
                aScore.append(x["teamSeasonScore"])
            elif(int(actualID) == season and (hID == id2 or aID == id2)):
                bScore.append(x["teamSeasonScore"])
        if(aScore[0] > bScore[0]):
            winner = nameA
        elif(bScore[0] > aScore[0]):
            winner = nameB
        data = {'Season': fullSeason, 'Team A': nameA, 'Team B': nameB, 'Team A Season Score': aScore[0], 'Team B Season Score': bScore[0], 'Winner': winner}
        
    return data
        
        

        

"""
if (season == 20152016 or season == 20162017):
        for x in range(1, 11):
            r = requests.get("https://statsapi.web.nhl.com//api//v1/teams//" + str(x) + "?season=" + str(season))
            obj = json.loads(r.text)
            team = obj["teams"]

            
        for x in range(12, 27):
            r = requests.get("https://statsapi.web.nhl.com//api//v1/teams//" + str(x) + "?season=" + str(season))
            obj = json.loads(r.text)
            team = obj["teams"]

            
        for x in range(28, 31):
            r = requests.get("https://statsapi.web.nhl.com//api//v1/teams//" + str(x) + "?season=" + str(season))
            obj = json.loads(r.text)
            team = obj["teams"]

            
        for x in range(52, 54):
            r = requests.get("https://statsapi.web.nhl.com//api//v1/teams//" + str(x) + "?season=" + str(season))
            obj = json.loads(r.text)
            team = obj["teams"]

    
    else:
        for x in range(1, 11):
            r = requests.get("https://statsapi.web.nhl.com//api//v1/teams//" + str(x) + "?season=" + str(season))
            obj = json.loads(r.text)
            team = obj["teams"]

            
        for x in range(12, 27):
            r = requests.get("https://statsapi.web.nhl.com//api//v1/teams//" + str(x) + "?season=" + str(season))
            obj = json.loads(r.text)
            team = obj["teams"]

            
        for x in range(28, 31):
            r = requests.get("https://statsapi.web.nhl.com//api//v1/teams//" + str(x) + "?season=" + str(season))
            obj = json.loads(r.text)
            team = obj["teams"]

            
        for x in range(52, 55):
            r = requests.get("https://statsapi.web.nhl.com//api//v1/teams//" + str(x) + "?season=" + str(season))
            obj = json.loads(r.text)
            team = obj["teams"]
"""