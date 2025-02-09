# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 10:55:56 2024

@author: Jalaj Gupta

I'll start by using the csv files generated, as fetching the data again
and again gets a tad bit annoying.

Once the thing is final, we can remove this block of code to read the final 
pandas dataframe generated in the ball_by_ball.py file to be the main source of
data.

#TODO:
#Actual graphing. 
#Additionally an automated system to type a player's name and 
#lookup the player numbers rather than creating a dictionary 
#would be ideal.

"""


import glob
import pandas as pd
#Plotly needs be > v 1.91 for offline to work
#from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
#import plotly.graph_objs as go

path = 'playerdata/*.csv'

def cumalative_runs(filedirectory):
    main_df = pd.DataFrame()
    
    for each in glob.iglob(filedirectory):
        df = pd.read_csv(each, index_col=None, header=0)
        filename = each.replace('playerdata/','')
        filename = filename.replace('.csv','')
        df['cumal_runs'] = df['mean_runs'].cumsum()
        df['batsman'] = filename
        df['total_innings'] = df['total_innings'].astype(float)
        main_df = main_df.append(df)
        
    main_df = main_df.drop('Unnamed: 0', axis=1)
    return main_df 

dataset = cumalative_runs(path)

#Getting a list of individual players
players = [each for each in dataset['batsman'].unique()]

# Creating the figure for the plot.
figure = {
    'data': [],
    'layout': {},
    'frames': []
}

