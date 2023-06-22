

    
#************** Buyer Ratio Dataset**********************************************************
#3rd ans 
import numpy as np

x1 = np.array([50,550])
x1
x2 = np.array([142,351])
x2
x3 = np.array([131,48])
x3
x4 = np.array([70,350]) 
x4

import pandas as pd

x1=pd.DataFrame(x1)
x2=pd.DataFrame(x2)
x3=pd.DataFrame(x3)
x4=pd.DataFrame(x4)

df = pd.concat([x1,x2,x3,x4],axis=1)
df
df.columns=["East","West","North","south"]
df

from scipy import stats
Fcalc, pvalue = stats.f_oneway(df["East"],df["West"],df["North"],df["south"])

alpha = 0.05
if pvalue <alpha:
    print("H0 is rejected and H1 is accepted")
else:
    print("H1 is rejected and H0 is accepted")    
    
#****************for customer order form dataset*******************************************************
#4th ans
import numpy as np

x1 = np.array([29,271])
x1
x2 = np.array([33,267])
x2
x3 = np.array([31,269])
x3
x4 = np.array([20,280]) 
x4

import pandas as pd

x1=pd.DataFrame(x1)
x2=pd.DataFrame(x2)
x3=pd.DataFrame(x3)
x4=pd.DataFrame(x4)

df = pd.concat([x1,x2,x3,x4],axis=1)
df
df.columns=["Phillipines","Indonesia","Malta","India"]
df

from scipy import stats
Fcalc, pvalue = stats.f_oneway(df["Phillipines"],df["Indonesia"],df["Malta"],df["India"])

alpha = 0.05
if pvalue <alpha:
    print("H0 is rejected and H1 is accepted")
else:
    print("H1 is rejected and H0 is accepted")    

























    