# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 11:44:03 2022

@author: HP
"""
#Ho : mue1 = mue2
#H1 : mue1 != mue2

import pandas as pd
df = pd.read_csv("D:\\Assignments DS\\3\\Cutlets.csv")
df.head()

from scipy import stats
Zcal, Pval = stats.ttest_ind(df['Unit A'],df['Unit B'])

alpha = 0.05

if Pval<alpha:
    print("Ho is rejected, H1 is accepted")
else:
    print("Ho is accepted, H1 is rejected")

###############################################################################
#Ho : mue1 = mue2 = mue3 = mue4
#H1 : any mue is not equal
import pandas as pd
df = pd.read_csv("D:\\Assignments DS\\3\\LabTAT.csv")
df.head()
import scipy.stats as stats
ftab,pval = stats.f_oneway(df['Laboratory 1'],df['Laboratory 2'],df['Laboratory 3'],df['Laboratory 4'])
alpha = 0.05

if Pval<alpha:
    print("Ho is rejected, H1 is accepted")
else:
    print("Ho is accepted, H1 is rejected")

###############################################################################


import pandas as pd
df = pd.read_csv("D:\\Assignments DS\\3\\Costomer+OrderForm.csv")
df.head()

df["Phillippines"].value_counts() #defective 29
def1 = [29]
df["Indonesia"].value_counts() #defective 33
def2 = [33]
df["Malta"].value_counts() #defective 31
def3 = [31]
df["India"].value_counts() #defective 20
def4 = [20]


import scipy.stats as stats
Fcalc, p = stats.f_oneway(def1,def2,def3,def4)

alpha = 0.05

if p < alpha:
    print("Ho is rejected and H1 is accepted")
else:
    print("H1 is rejected and H0 is accepted")







