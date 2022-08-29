import pandas as pd
import matplotlib.pyplot as plt
# import needed libraries

df = pd.read_excel('blushes-toh.xlsx')
# read the excel data

episodes = list(df['Episode'])
episodes.remove('Colors')
# define the episodes and remove the colors

char_with_colors = {}

char_total_series_blushes = {}

for index, name in enumerate(df.columns):
    if index != 0:
        blush_counts = []
        
        for count in list(df[name]):
            if type(count) != str:
                char_total_series_blushes[name] = char_total_series_blushes.get(name, 0) + count
            else:
                char_with_colors.update({name:count})
# count blushes of each character

plt.pie(list(char_total_series_blushes.values()), labels = list(char_total_series_blushes.keys()), autopct='%1.1f%%', colors = list(char_with_colors.values()))
# graph blushes with percentages and character names

plt.title("Percentage of Total Blushes a Character Blushes in The Owl House")
# add graph labels

plt.show()
# show the graph