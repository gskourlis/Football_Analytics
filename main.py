import pandas as pd


url = 'https://fbref.com/en/comps/Big5/stats/players/Big-5-European-Leagues-Stats'

df = pd.read_html(url, attrs = {'id':'stats_standard'})

df = df[0]

df = df[df.columns.drop(list(df.filter(regex = 'Per 90')))]

df = df.droplevel(0, axis =1)

df = df[df['Pos'].str.contains('FW')]
df = df[df['Min'].astype(int)>400]

df[['90s', 'Gls', 'Ast', 'G+A', 'xG', 'xAG', 'PrgC', 'PrgP', 'PrgR']].head(10)

#make sure that the columns are of the correct type
df[['90s', 'xG', 'xAG']] = df[['90s', 'xG', 'xAG']].astype(float)
df[['Gls', 'Ast', 'G+A', 'PrgC', 'PrgP', 'PrgR']] = df[['Gls', 'Ast', 'G+A', 'PrgC', 'PrgP', 'PrgR']].astype(int)