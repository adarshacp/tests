#importing libraries and crearing an dataframe
import pandas as pd
da={
"mpg":[18,15,18,16,17],"cylinders":[8,8,6,4,8],"displacement":[307,350,318,
304,302],
"horsepower":[130,165,150,150,140],"weigth":[3504,3693,3436,3433,3449],
"acceleration":[12.0,11.5,11.0,12.0,10.5],"model year":[70,71,70,80,70],
"origin":[1,1,1,1,1],"carname":["cheverlot","buick","plymoth","amc","ford"]
}
df=pd.DataFrame(da)
#shows the statistical of data
sa=df.describe()
#getting the cylinders which quals=8
ei=df[df["cylinders"]==8]
#counting the number of cars manufactured in each-year
ye = df.groupby('model year')["model year"].count()
#printing the entire data
print("Satistical:\n",sa)
print("\n8 cylinders:\n",ei)
print("\nBy year:\n",ye)
