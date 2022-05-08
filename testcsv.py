
import matplotlib.pyplot as plt
import csv

# Import the necessary modules
import matplotlib.pyplot as plt
import pandas as pd
  
  
# Initialize the lists for X and Y
data = pd.read_csv(r'C:/Users/user/scopeX/web scraping/stats.csv')
  
df = pd.DataFrame(data)
print(df)
X = list(df.iloc[:, 0])
Y = list(df.iloc[:, 4])#.replace("$",""))
  
# Plot the data using bar() method
plt.bar(X, Y, color='g')
plt.title("Stats of whales")
plt.xlabel("wallet address")
plt.xticks(rotation=90)
plt.ylabel("Number of value usd")
  
# Show the plot
plt.show()