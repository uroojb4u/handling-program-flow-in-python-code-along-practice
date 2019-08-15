# --------------
import json
from collections import Counter
with open(path) as f:
    data = json.load(f)

# Code starts here
count_delivery=0
total=0
counter=0
batsmen=[]
batsman_sixes=[]
firstextras=[]
secondextras=[]
for i in data['innings'][0]['1st innings']['deliveries']: 
    for info in i.values():
        if (info['batsman'] == 'SC Ganguly'):
            count_delivery +=1
        if info['batsman']== 'BB McCullum':
            total += info['runs']['batsman']
        batsmen.append(info['batsman'])
        if info['runs']['batsman']==6:
            batsman_sixes.append(info['batsman'])
        if info['runs']['extras']>0:
            firstextras.append(info['runs']['extras'] )
        
print(count_delivery)
print(data['info']['player_of_match'][0])
print(total)
print ("batsmen in 1st inn:", set(batsmen))
print(Counter(batsman_sixes))
bowled_players=[]
for i in data['innings'][1]['2nd innings']['deliveries']:
    for info in i.values():
        if 'wicket' in info and info['wicket']['kind']=="bowled":
            bowled_players.append(info['batsman'])
        if info['runs']['extras']>0:
            secondextras.append(info['runs']['extras'] )
print(bowled_players)
difference= len(secondextras)-len(firstextras)
print(difference)


# Code ends here


