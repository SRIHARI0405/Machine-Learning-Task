# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 14:54:17 2022

@author: HP
"""

#1st answer
from scipy.stats import norm
nd = norm(45,8) #mean,sd
#probability that service manager cannot meet his commitment
1-nd.cdf(50)

####################################################################
#2nd answer
from scipy.stats import norm
nd = norm(38,6) #mean,sd
#statement - A answer
#probability of employes working older than 44
1-nd.cdf(44)
#probability of employes working beween age 38 and 44
nd.cdf(44)-nd.cdf(38)

#statement - B answer
nd.cdf(30)

####################################################################
#4th answer
from scipy.stats import norm
nd = norm(100,20)#mean , sd
#the below are considered for probability calculation because these options are only symmetrical

nd.cdf(119.8)-nd.cdf(80.2)
nd.cdf(151.5)-nd.cdf(48.5)
nd.cdf(109.9)-nd.cdf(90.1)

####################################################################
#5th answer
#A
from scipy import stats
from scipy.stats import norm
stats.norm.interval(0.95, 540, 225)
#c Probability of Division 1 making a loss P(X<0)
stats.norm.cdf(0,5,3)
# Probability of Division 2 making a loss P(X<0)
stats.norm.cdf(0,7,4)


####################################################################

    















