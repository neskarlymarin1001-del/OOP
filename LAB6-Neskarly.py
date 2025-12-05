import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data01.csv")

# 1) Find the median of the median_house_value column and print it

median_mhv = df["median_house_value"].median()
print("The median of the median_house_value variable is: ", median_mhv)

# 2) Find the total rooms that are less than 500, then replace them with the median value of total_rooms
# 3) Print the housing_median_age less than 25, and print the rows

median_total_rooms = df["total_rooms"].median()

for x in df.index:
    if df.loc[x, "total_rooms"] < 500:
        df.loc[x, "total_rooms"] = median_total_rooms

    if df.loc[x, "housing_median_age"] < 25:
       print(df.loc[x])

#4) Draw any type of graph for any two relevant columns in the CSV file

df

df.plot()
plt.show()

df.plot(kind = 'scatter', x = 'median_house_value', y = 'total_rooms') 

plt.show() 
