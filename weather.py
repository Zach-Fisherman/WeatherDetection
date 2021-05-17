import math as m
data = []
test = []

import json
import csv
import datetime
# b=''
# filea= open('weather_station.json','r')
# a= filea.readlines()
#
# for line in a:
#     b+=line[:-1]+",\n"
#
# # for i in range(len)
# #     b += data +',\n'
# #
# file = open("lol.json","w")
#
# file.write(b)

with open('lol.json') as f:
  data = json.load(f)


data = data['data']
for i in range(len(data)):
  data[i]['date'] = datetime.datetime.strptime(data[i]['date']['$date'][:-5],'%Y-%m-%dT%H:%M:%S.%f')

NewData = []

for i in range(len(data)):
    a = []
    if len(data[i])==7:
      a.append(data[i]['_id'])
      a.append(data[i]['humidity'])
      a.append(data[i]['pressure'])
      a.append(data[i]['temperature'])
      a.append(data[i]['light'])
      a.append(data[i]['date'])
      a.append(data[i]['rain'])
      NewData.append(a)

with open('data.csv', 'w') as f:

    # using csv.writer method from CSV package
    write = csv.writer(f)
    write.writerows(NewData)

def calcul_distance(n_champ,i_champ):
    total = 0
    for i in range(len(n_champ)-2):
        if (n_champ[i] != i_champ[i]):
            total += 1
    return m.sqrt(total)

def prediction_file(data):
    c = 0
    r = 0
    for i in range(len(data)):
        if(data[i][5]==0):
            c += 1
        else:
            r+=1
    if (c == r):
        print("uncertain(p: "+str(po)+",e: "+str(ed)+")")
    elif( c>r ):
        print("clear(c: "+str(c)+",r: "+str(r)+")")
    else :
        print("rainy(c: "+str(c)+",r: "+str(r)+")")

def prediction(list_r_or_v):
    ra = 0
    cl = 0
    for i in range(len(list_r_or_v)):
        if(list_r_or_v[i]=='r'):
            ra+=1
        elif(list_r_or_v[i]=='c'):
            cl+=1
    if (cl == ra):
        print("uncertain(p: "+str(ra)+",e: "+str(cl)+")")
    elif( cl>ra ):
        print("Clear(p: "+str(ra)+",e: "+str(cl)+")")
    else :
        print("Rainy(p: "+str(ra)+",e: "+str(cl)+")")

#return 0 si clear, 1 sinon
def return_c_or_r(num,list_champ):
    return list_champ[num][6]!=0

#retourne l'inverse
def inverse(distance):
    if distance==0:
        return 0
    return 1/distance

#n_champ : champignon a tester
#d_champ : liste de champignon
#N = N
#Show = affiche l'information ou non
def KNN(n_champ,d_champ,N,show):
    list_dist=[]
    list_k=[]
    for i in range(len(d_champ)):
        list_dist.append([calcul_distance(n_champ,d_champ[i]),i])
    list_dist.sort()
    list_comestibility =[]
    for i in range(N):
        if(show):
            print("Voisin n°"+str(list_dist[i][1])+" distance :"+str(list_dist[i][0])+" classe:"+str(return_c_or_r(list_dist[i][1],d_champ)))
        list_comestibility.append(return_c_or_r(list_dist[i][1],d_champ))

    #calcul total pondéré
    tpe = 0
    tpp = 0
    for i in range(N):
        a=return_c_or_r(list_dist[i][1],d_champ)
        if(a=="e"):
            tpe = inverse(list_dist[i][0])
        else:
            tpp = inverse(list_dist[i][0])

    if(show):
        prediction(list_comestibility)
        print("total pondere edible="+str(tpe))
        print("total pondere poisonous="+str(tpe))
    return [list_comestibility,[tpe,tpp]]

#Permet de calculer 1NN
def unNN(n_champ,d_champ,show):
    return KNN(n_champ,d_champ,1,show)

#input = date
#output = date dans une heure
def date_plus_hour(wDate):
    return wDate+datetime.timedelta(hours=1)

# renvoie la difference de temps absolue entre deux date
def difference_date(wDate1,wDate2):

    return datetime.timedelta(seconds=abs(wDate1-wDate2).total_seconds())

# wDate=  date de la donnée
# d_champ = donnée d'apprentissage
# return : une des données au plus proche d'une heure après wDate
def find_data_in_an_hour(wDate,d_champ):
    aMax = difference_date(wDate,d_champ[0][5])
    index =None
    for i in range(len(d_champ)):
        if(difference_date(wDate,d_champ[i][5])<aMin):
            aMax = difference_date(wDate,d_champ[i][5])
            index=i
    print(index)
    return d_champ[i]

