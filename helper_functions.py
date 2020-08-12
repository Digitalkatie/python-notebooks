import numpy as np
import os
import matplotlib.pyplot as plt
import math
import seaborn as sns
import pandas as pd
from collections import Counter

path_videogames = os.path.join(os.getcwd(), 'datasets', 'vgsales.csv')
videogames = pd.read_csv(path_videogames, delimiter = ',')

def get_vgs_proportion():
    #Proportion of sold videogames for each Nintendo platform per year
    proportion_videogames = videogames[['Platform', 'Global_Sales', 'Year', 'Publisher']]
    #Get the years and platforms to loop through them
    years = sorted(proportion_videogames.Year.unique())
    years = [x for x in years if (not np.isnan(x) and x>=2005 and x<2017)] #Delete NaNs and select from 2005
    platforms = proportion_videogames.Platform.unique()
    #Array for storing the data
    prop_videogames = pd.DataFrame(index = years, columns = platforms)
    #Calculating the proportion of each platform per year
    for year in years:
        #print(year)
        #Get the videogames in a specific year
        vgs_in_year = proportion_videogames.loc[(proportion_videogames['Year']==year) & (proportion_videogames['Publisher']=='Nintendo')]
        num_vgs = len(vgs_in_year.index)
        for platform in platforms:
            num_vgs_in_plf = len(vgs_in_year.loc[vgs_in_year['Platform']==platform].index)
            proportion = 0
            if(not num_vgs ==0):
                proportion = num_vgs_in_plf/num_vgs
            prop_videogames.at[year, platform] = proportion
    #Save it in a dataframe. Use this for the exercise
    prop_videogames = prop_videogames.loc[:,(prop_videogames!=0).any(axis=0)] #Delete videogames with 0 sales
    return prop_videogames