import pandas as pd
import os.path 
from dataframe_chord import DataFrame

name_chords= ['C']
folder_chords = f'{os.path.abspath(os.path.dirname(__file__))}/Dataset/Main/C'
df = DataFrame(50,folder=folder_chords,chords=name_chords)
test_df = df.create_dataframe()
test_df.to_csv('chords_test_2.csv',index=False)