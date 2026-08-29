import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
data = pd.read_csv("matches.csv")

# Count the number of wins for each team
wins = data["winner"].value_counts()
print("===== IPL TEAM WINS =====")
print(wins)

# Create a bar chart
wins.plot(kind="bar")

plt.title("IPL Team Wins")
plt.xlabel("Team")
plt.ylabel("Number of Wins")
plt.show()