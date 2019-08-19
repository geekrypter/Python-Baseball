import os
import glob
import pandas as pd
game_files=glob.glob(os.path.join(os.getcwd(),'games','*.EVE'))
game_files.sort()
game_frames=[]
for game_file in game_files:
	game_frame=pd.read_csv(game_file,names=['type', 'multi2', 'multi3', 'multi4', 'multi5', 'multi6', 'event'])
	game_frames.append(game_frame)
games=pd.concat(game_frames)
games.loc[games['multi5']=='??',['multi5']]=''
identifiers=games['multi2'].str.extract(r'(.LS(\d{4})\d{5})')
identifiers=identifiers.fillna(method='ffill')
identifiers.columns=['game_id','year']
games=pd.concat([games,identifiers],axis=1,sort=False)
games=games.fillna(' ')
games.loc[:,'type'] = pd.Categorical(games.loc[:,'type'])
print(games.head())