# import pandas as pd ## for handling the dataframe
# import matplotlib.pyplot as plt ## for visualization

# df = pd.read_pickle('questiondatanoblanks.pkl')

# plt.bar(df['Weekday'], df['Mean Word Similarity'], tick_label = df['Weekday'])
# plt.xlabel('Weekday') ## Label on X axis
# plt.ylabel('Mean Word Similarity') ##Label on Y axis
# plt.title('Mean Word Similarity for [?] Clues by Weekday')
# plt.show()
import pandas
tot = 0
for i in range(7):
    df = pandas.read_pickle(f'weekday{i}question.pkl')
    tot += df.shape[0]

print(tot)