import csv, json
with open('Batting.csv') as f:
    bdata = [{k: str(v) for k, v in row.items()}
        for row in csv.DictReader(f, skipinitialspace=True)]

n = 0 
hrc = 0
table = []
for row in bdata:
    if int(row['H']) >= 200 and int(row['BB']) >= 150:
        plyrs = {}
        yr = row['yearID']
        name = row['playerID']
        hr = row['HR']
        hits = row['H']
        so = row['SO']
        bb = row['BB']
        plyrs['Name'] = name
        plyrs['Year'] = yr
        plyrs['HR'] = hr
        plyrs['Hits'] = hits
        plyrs['BB'] = bb
        plyrs['SO'] = so
        table.append(plyrs)
        
    n += 1

print(len(table))
print(table)

with open('Pitching.csv') as p:
    pdata = [{k: str(v) for k, v in row.items()}
        for row in csv.DictReader(p, skipinitialspace=True)]
        
 n = 0 
cgc = 0 
table = []
for row in pdata:
    if int(row['CG']) >= 75:
        plyrs = {}
        yr = row['yearID']
        name = row['playerID']
        CG = row['CG']
        SHO = row['SHO']
        BB = row['BB']
        ERA = row['ERA']
        plyrs['Name'] = name
        plyrs['Year'] = yr
        plyrs['CG'] = CG
        plyrs['SHO'] = SHO
        plyrs['BB'] = BB
        plyrs['ERA'] = ERA
        table.append(plyrs)
        
    n += 1
print(len(table))
print(table)

import pandas as pd
all_hitting = pd.read_csv('Batting.csv',skipinitialspace = True) 
pitching = pd.read_csv('Pitching.csv',skipinitialspace = True)
all_hitting.describe()

import pandas as pd
import matplotlib.pyplot as plt
pitching = pd.read_csv('Pitching.csv') 
pitching.describe()

all_hitting = pd.read_csv('Batting.csv') 
hitting = all_hitting[['yearID','HR','BB','SO']]
all_pitching = pd.read_csv('Pitching.csv')
pitching = all_pitching[['yearID','WP','HBP','R']]
hitting.head(15)

yrs_hitting = hitting.groupby(['yearID'])
yrs_pitching = pitching.groupby(['yearID'])
yrs_pitching.sum()

yrs_pitching.sum().reset_index().to_csv('pitch_sub.csv')
yrs_hitting.sum().reset_index().to_csv('hit_sub.csv')

find = all_hitting[['playerID','yearID','HR','BB','SO']]
unique_in_hr = find.HR.unique()
print(unique_in_hr)

plt.hist(all_pitching.WP)

x = all_hitting.yearID
y = all_hitting.HR
y1 = all_hitting.SO
y2 = all_hitting.R
fig, sp = plt.subplots(3, gridspec_kw={'hspace': 1})
fig.suptitle('HR, Ks, Runs over Time')
sp[0].plot(x,y)
sp[1].plot(x,y1)
sp[2].plot(x,y2)

x = all_pitching.yearID
y = all_pitching.IPouts
y1 = all_pitching.CG
y2 = all_pitching.SHO
fig, sp = plt.subplots(3, gridspec_kw={'hspace': 1})
fig.suptitle('IP, CG, SHO Over Time')
sp[0].plot(x,y)
sp[1].plot(x,y1)
sp[2].plot(x,y2)

hit_sub = pd.read_csv('hit_sub.csv')
pitch_sub = pd.read_csv('pitch_sub.csv')
combo = hit_sub.merge(pitch_sub, on='yearID')
combo.describe()

pitch_sub2 = all_pitching[['yearID','IPouts','CG','SHO']]
combo2 = hit_sub.merge(pitch_sub2, on='yearID')
combo2.reset_index().to_csv('hit_pitch_combo2.csv')
pitch_sub2.head(10)











