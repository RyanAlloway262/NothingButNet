from data import trainFunction as tf
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.metrics import accuracy_score, precision_score, recall_score
import numpy as np
from sklearn.metrics import plot_confusion_matrix

#creates frame based on the data for the csv file
frame = pd.read_csv(r'game_stats.csv')

#creates x and y values for data train drops the game_id, game_id, won(T1F0', goals
#if these are not dropped you can not predict win or loss 
#2017300543
x = frame.drop(['game_id','won(T1F0)'], axis=1)
y = frame['won(T1F0)']

#creates the width and height for the new array
w, h = 14, 2;
predictx = [[0 for x in range(w)] for y in range(h)]

#splits the data for train and test 
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.05, stratify=y)

logistic_regression = LogisticRegression(solver='liblinear',max_iter=1000000)

def train():
    #creates logistic regression model and fits 
    logistic_regression.fit(x_train, y_train)
    
def prediction():
    
    result = logistic_regression.predict(x_test)
    
    accuracy = metrics.accuracy_score(y_test, result)
    precision = precision_score(y_test, result)
    recall = recall_score(y_test, result)

    #creates a plot for the confusion matrix
    plot_confusion_matrix(logistic_regression, x_test, y_test)

    #saves the plot as a png
    plt.savefig('confusionMatrixSeason.png')

    result = np.array(result)
    y_test1 = np.array(y_test)
    
    #writes to the text file for the results and the array
    resultFile = open("result.txt","w")
    y_testFile = open("y_test.txt","w")
        
    result = str(result)
    y_test1 = str(y_test1)
    
    resultFile.write(result)
    y_testFile.write(y_test1)
    
    #assigs the global variable to the accuracy
    global GBaccuracy 
    GBaccuracy = accuracy

    return(accuracy, precision, recall)

def predictionOfSeason(season, teamA, teamB):
    
    #gets the values for the dataset
    predictx[0] = tf(teamA, season)
    predictx[1] = tf(teamB, season)
    
    #inserts the unknown data into the array (teamA,teamB,HomeOrAway)
    #this gets the array to the correct size and data values of 
    #the model that was used to train the data
    predictx[0].insert(0, teamA)
    predictx[1].insert(0, teamB)
    
    predictx[0].insert(1, teamB)
    predictx[1].insert(1, teamA)
    
    predictx[0].insert(2, 1)
    predictx[1].insert(2, 0)
    
    
    #converts the list into the np array
    predict_x = np.array(predictx)
    predict = predict_x.astype(float)
    
    
    #predicts the model
    gamePrediction = logistic_regression.predict(predict)
    
    
    #returns the predicted result
    if(gamePrediction[0] == 1):
        return("TeamA Wins", GBaccuracy)
    if(gamePrediction[1] == 1):
        return("Team B Wins", GBaccuracy)
    if(gamePrediction[0] == 0 and gamePrediction[1] == 0):
        return("Results are inconclusive (Our model predicted 0 for both)", GBaccuracy)
    if(gamePrediction[0] == 1 and gamePrediction[1] == 1):
        return("Results are inconclusive (Our model predicted 1 for both)", GBaccuracy)

    
#train()
#print(prediction())
#print(predictionOfSeason(20152016, 1, 52))


