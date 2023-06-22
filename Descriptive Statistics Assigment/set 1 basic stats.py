# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 18:03:44 2022

@author: HP
"""

import pandas as pd
df = pd.DataFrame({
    "Name of Company": ["Allied Signal","Bankers Trust","General Mills","ITT Industries","J.P.Morgan & Co.","Lehman Brothers","Marriott","MCI","Merrill Lynch","Microsoft","Morgan Stanley","Sun Microsystems","Travelers","US Airways","Warner-Lambert"],
    
    "Measure X": [24.23,25.53,25.41,24.14,29.62,28.25,25.81,24.39,40.26,32.95,91.36,25.99,39.42,26.71,35.00],
}, index=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14])
df

df["Measure X"].mean()
df["Measure X"].std()
df["Measure X"].var()

import numpy as np
Q1 = np.percentile(df["Measure X"], 25)
Q1
Q2 = np.percentile(df["Measure X"], 50)
Q2
Q3 = np.percentile(df["Measure X"], 75)
Q3

df.boxplot("Measure X",vert=False)
