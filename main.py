import pandas as pd
import matplotlib.pyplot as plt
# import needed libraries

df = pd.read_excel('blushes-toh.xlsx')
# read the blushes table

episodes = list(df['Episode'])
# come up with the episode names
episodes.remove('Colors')
# remove the colors row from being graphed

characters = []
# define list of character (to be filled later)

char_num = len(df.columns) - 1
width = 0.5/char_num
# define bar width and number of characters

char_with_colors = {}
most_blushes = 0
# define most blushes and characters with their colors

def annotate_counts(x_positions, counts, float_amt):
    for index, pos in enumerate(x_positions):
        plt.annotate(str(counts[index]), (pos, counts[index] + float_amt), ha='center', color='grey')
        # go through the x positions, and annotate them with the episode names

for index, name in enumerate(df.columns):
    if index != 0:
        # check if not looping through the row with just names
        blush_counts = []
        
        for count in list(df[name]):
            if type(count) != str:
                blush_counts.append(count)
                if count > most_blushes:
                    most_blushes = count
                    # add blushes counts to the blush count
            else:
                char_with_colors.update({name:count})
                # update the character with the color with the name and count

        character_x_pos = [x + (width * index) for x in range(len(blush_counts))]
        # deinf the x position for the episode
        
        ax = plt.bar(character_x_pos, blush_counts, width, color = char_with_colors[name])
        # graph

xticks_pos = [(x + char_num / (char_num * 3.25)) for x in range(len(episodes))]
# add episode titles

plt.title("Number of Times a Character Blushes in Each Episode of The Owl House: Season 1")
plt.xlabel("Episode Title")
plt.ylabel("Number of Times a Character Blushes")
plt.xticks(xticks_pos, episodes, rotation="vertical")
# add graph labels

plt.subplots_adjust(bottom=len(max(episodes))/100 + 0.15, left = 0.1)
# adjust graph to make more readable.
plt.legend(list(char_with_colors.keys()))
# add legend
most_blushes += 1

plt.show()
# show graph