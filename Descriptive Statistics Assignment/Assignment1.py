##Q7 solution
import pandas as pd
df = pd.read_csv("D:\\Assignments DS\\1\\Q7.csv")
df
df[["Points","Score","Weigh"]].describe()
df[["Points","Score","Weigh"]].var()
df[["Points","Score","Weigh"]].median()
range = df[["Points","Score","Weigh"]].max()-df[["Points","Score","Weigh"]].min()
df[["Points","Score","Weigh"]].mode()

##Q9_a
import pandas as pd
df = pd.read_csv("D:\\Assignments DS\\1\\Q9_a.csv")
df
    
df.dtypes
df["speed"].skew()
df["speed"].kurt()

df["dist"].skew()
df["dist"].kurt()

##Q9_b
import pandas as pd
df = pd.read_csv("D:\\Assignments DS\\1\\Q9_b.csv")
df
df.dtypes
df["SP"].skew()
df["SP"].kurt()

df["WT"].skew()
df["WT"].kurt()

##Q11
from scipy import stats
from scipy.stats import norm
stats.norm.interval(0.94,200,30/(2000**0.5))
stats.norm.interval(0.98,200,30/(2000**0.5))
stats.norm.interval(0.96,200,30/(2000**0.5))


##Q12 solution
import numpy as np
import pandas as pd

d1 = {"marks":[34,36,36,38,38,39,39,40,40,41,41,41,41,42,42,45,49,56]}
df = pd.DataFrame(d1)
df.describe()
df.median()
df.var()

##Q20 solution
import pandas as pd
from scipy.stats import norm
df = pd.read_csv("D:\\Assignments DS\\1\\Cars.csv")
df

df["MPG"].mean()
m = df["MPG"].mean()
df["MPG"].std()
sd = df["MPG"].std()

nd = norm(m,sd)
#a.	P(MPG>38)
1- nd.cdf(38)
#b.	P(MPG<40)
nd.cdf(40)-nd.pdf(40)
#c.   P(20<MPG<50)
nd.cdf(50) - nd.cdf(20)

##Q21_a
import pandas as pd
df = pd.read_csv("D:\\Assignments DS\\1\\Cars.csv")
df
#Ho : Data is normally distributed
#H1 : Data is not normally distributed
from scipy.stats import shapiro
stat,p = shapiro(df["MPG"])
print(stat)
print("p value",p)
alpha = 0.05
if (p<alpha):
    print("Ho is rejected, H1 is accepted")
else:
    print("Ho is accepted, H1 is rejected")

#Q21_b
import pandas as pd
df = pd.read_csv("D:\\Assignments DS\\1\\wc-at.csv")
df
#Ho : Data is normally distributed
#H1 : Data is not normally distributed
from scipy.stats import shapiro
stat,p = shapiro(df["Waist"])
print(stat)
print("p value",p)
alpha = 0.05
if (p<alpha):
    print("Ho is rejected, H1 is accepted")
else:
    print("Ho is accepted, H1 is rejected")
    
stat,p = shapiro(df["AT"])
print(stat)
print("p value",p)
alpha = 0.05
if (p<alpha):
    print("Ho is rejected, H1 is accepted")
else:
    print("Ho is accepted, H1 is rejected")
    

##Q22
import scipy.stats as stats
stats.norm.ppf(0.95).round(4)

import scipy.stats as stats
stats.norm.ppf(0.97).round(4)

import scipy.stats as stats
stats.norm.ppf(0.80).round(4)

##Q23
import scipy.stats as stats
stats.t.ppf(q=0.975,df=24).round(4)

import scipy.stats as stats
stats.t.ppf(q=0.98,df=24).round(4)

import scipy.stats as stats
stats.t.ppf(q=0.995,df=24).round(4)










