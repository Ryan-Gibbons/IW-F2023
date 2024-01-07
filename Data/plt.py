import pandas as pd ## for handling the dataframe
import matplotlib.pyplot as plt ## for visualization

df = pd.read_pickle('summarydata.pkl')

plt.errorbar(df['Weekday'], df['Max Ind. Word Similarity'], yerr=df['miwsstd'], fmt='o',
             color='Black', elinewidth=3,capthick=3,errorevery=1, alpha=1, ms=4, capsize = 5)
plt.bar(df['Weekday'], df['Max Ind. Word Similarity'],tick_label = df['Weekday'])
plt.xlabel('Weekday') ## Label on X axis
plt.ylabel('Max. Individual Word Similarity') ##Label on Y axis
plt.title('Maximum Individual Word Similarity between Clues & Answers, by Weekday')
plt.show()