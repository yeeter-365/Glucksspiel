# Round of 20 of "investment banking"
import random


Listofplayers = []
Listofmoney = [1000,1000,1000,1000]
currentbet = []

for player in range(1,5):
  Listofplayers.append(input("Player "+str(player)+" enter name: "))

while True:
  innerdex = 0
  for losers in Listofmoney:
      if len(Listofplayers) == 1:
          print(Listofplayers[0], "won!")
      elif 0 == int(losers):
          Listofmoney.pop(innerdex); Listofplayers.pop(innerdex)
      innerdex+=1
  if max(Listofmoney) >= 1000000:
     break
  for playerish in range(len(Listofmoney)):
    print(Listofplayers[playerish],"\nBank balance:",Listofmoney[playerish])
    while True:
      moneybetted = input("Money placed: ")
      if moneybetted.isdigit() and int(moneybetted) <= Listofmoney[playerish]:
        break; moneybetted = int(moneybetted)
    currentbet.append(moneybetted)
  Lost = random.randrange(len(Listofmoney)); print(Listofplayers[Lost], "Lost", currentbet[Lost])
  for winloss in range(len(Listofmoney)):
    if winloss == Lost:
      Listofmoney[Lost] -= int(currentbet[Lost])
    else:
      Listofmoney[winloss] += int(currentbet[winloss])
  currentbet = []
maxvalue = max(Listofmoney)
innerdexter = 0; winner=''
for x in Listofmoney:
    if x == maxvalue:
      print(Listofplayers[innerdexter], "won!")
    innerdexter+=1
