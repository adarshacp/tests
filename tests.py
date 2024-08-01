#importing libraries
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
#reading a dataframe
df=pd.read_csv('D:/5th sem/practical/mtcars.csv')

#creating histogram
mpg=df['mpg']
plt.hist(mpg,bins='auto',color='k',edgecolor='c')
plt.xlabel('Miles per gallon (mpg)');plt.ylabel('Frequency')
plt.title('Frequency Distribution of mpg')
plt.show()

#creating scatterplot
weight=df['wt']
iv=range(len(df))
plt.scatter(iv,mpg,color='k',label='mpg')
plt.scatter(iv,weight,color='b',label='wt')
plt.title("Relationship b/w Weigth and MPG")
plt.legend()
plt.show()

#creating a barchart
c=df['am'].value_counts()
co=['r','g']
plt.bar(c.index,c.values,color=co,width=0.3)
plt.xticks([0,1],['0-Automatic','1-Manual'])
plt.xlabel("Tranmisson Type");plt.ylabel("No of Cars")
plt.title("Frequency distribution of transmission type of cars")
plt.show()
