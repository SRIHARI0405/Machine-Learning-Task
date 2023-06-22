# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 15:08:24 2022

@author: HP
"""
##5th answer
#Ho : p>=5% mozilla has morethan or equal to 5% of market share
#H1 : p<5% mozilla has less than 5% of market share
import numpy as np
n1 = 2000
n2 = 2000
alpha = 0.05

p1 = 0.047
p2 = 0.05
round(p1*100) 
round(p2*100) 

props = np.array([p1*100,p2*100])
samplesize = np.array([n1,n2])

from statsmodels.stats.proportion import proportions_ztest
stat, pva = proportions_ztest(props, samplesize)

if(pva<alpha): 
    print("Ho is rejected, H1 is accepted")
else:
    print("Ho is accepted, H1 is rejected")
    
