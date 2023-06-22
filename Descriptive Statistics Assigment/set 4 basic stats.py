# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 21:52:50 2022

@author: HP
"""
#3rd solution
from scipy import stats
from scipy.stats import norm

#finding of Z score for 45 & 55
#  n = 100, population mean= 50, population SD= 40
z1=(45-50)/(40/100**0.5)
z2=(55-50)/(40/100**0.5)
#probability of not having a investigation
no_investigation_prob = stats.norm.cdf(z2)-stats.norm.cdf(z1)
#probability of having a investigation
1-no_investigation_prob
