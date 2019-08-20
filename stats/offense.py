import pandas as pd
import matplotlib.pyplot as plt
from data import games
plays = games[games['type']=='play']
plays.columns = ['type', 'inning', 'team', 'player', 'count', 'pitches', 'event', 'game_id', 'year']
hits = plays.loc[plays['event'].str.contains('^(?:S(?!B)|D|T|HR)'),['inning','event']]
hits.loc[:,'inning'] = pd.to_numeric(hits.loc[:,'inning'])
replacements = {r'^S(.*)': 'single', r'^D(.*)': 'double', r'^T(.*)': 'triple', r'^HR(.*)': 'hr'}
hit_type = hits['event'].replace(replacements,regex=True)
hits=hits.assign(hit_type=hit_type)
hits = hits.groupby(['inning','hit_type']).size().reset_index(name='count')
hits['hit_type'] = pd.Categorical(hits['hit_type'],['single', 'double', 'triple','hr'])
hits = hits.sort_values(['inning','hit_type'])
hits = hits.pivot(index='inning', columns='hit_type', values='count')
hits.plot.bar(stacked=True)
plt.show()