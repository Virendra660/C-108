import random
import plotly_express as px

count=[]
diceresult=[]
for i in range(0,100):
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    diceresult.append(dice1+dice2)
    count.append(i)
print(count,diceresult)
fig=px.bar(x=diceresult,y=count)
fig.show()