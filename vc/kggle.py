import pandas as pd

pd.set_option('display.max_columns' , 8)

df = pd.read_csv('winemag-data_first150k.csv')

print(df)