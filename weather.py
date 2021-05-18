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
      a.append(data[i]['humidity'])
      a.append(data[i]['pressure'])
      a.append(data[i]['temperature'])
      a.append(data[i]['light'])
      a.append(data[i]['_id'])
      a.append(data[i]['date'])
      a.append(data[i]['rain'])
      NewData.append(a)

with open('data.csv', 'w') as f:

    # using csv.writer method from CSV package
    write = csv.writer(f)
    write.writerows(NewData)

def calcul_distance(n_releve,i_champ):
    total = 0
    for i in range(len(n_releve)-3):
        total += abs(m.pow(n_releve[i],2)-m.pow(i_champ[i],2))
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

#Code appartenant a Swan Sauvegrain
def a_plu(indiv, bdd):
    """Retourne True si de la pluie a été enregistrée dans l'heure suivant
    le relevé indiv et False sinon.
    """
    date_indiv = indiv[5]
    date_fin = date_indiv + datetime.timedelta(hours=1)
    for releve in bdd:
        date_releve = releve[5]
        if date_releve >= date_indiv:
            if date_releve < date_fin:
                if releve[6] > 0:
                    return True
    return False

#return 0 si clear, 1 sinon
def return_c_or_r(num,list_releve):
    return a_plu(list_releve[num],list_releve)

#retourne l'inverse
def inverse(distance):
    if distance==0:
        return 0
    return 1/distance


#n_releve : champignon a tester
#data_releve : liste de champignon
#N = N
#Show = affiche l'information ou non
def KNN(n_releve,data_releve,N,show):
    list_dist=[]
    list_k=[]
    for i in range(len(data_releve)):
        list_dist.append([calcul_distance(n_releve,data_releve[i]),i])
    list_dist.sort()
    list_comestibility =[]
    for i in range(N):
        if(show):
            print("Voisin n°"+str(list_dist[i][1])+" distance :"+str(list_dist[i][0])+" classe:"+str(return_c_or_r(list_dist[i][1],data_releve)))
        list_comestibility.append(return_c_or_r(list_dist[i][1],data_releve))

    return [list_comestibility]

