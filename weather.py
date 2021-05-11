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

print(NewData[0])
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
#
# def prediction(list_p_or_e):
#     ed = 0
#     po = 0
#     for i in range(len(list_p_or_e)):
#         if(list_p_or_e[i]=='e'):
#             ed+=1
#         elif(list_p_or_e[i]=='p'):
#             po+=1
#     if (ed == po):
#         print("uncertain(p: "+str(po)+",e: "+str(ed)+")")
#     elif( ed>po ):
#         print("edible(p: "+str(po)+",e: "+str(ed)+")")
#     else :
#         print("poisonous(p: "+str(po)+",e: "+str(ed)+")")

#return 0 si clear, 1 sinon
def return_c_or_r(num,list_champ):
    return list_champ[num][5]!=0

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

# def unNN(n_champ,d_champ,show):
#     return KNN(n_champ,d_champ,1,show)
#
# def return_comestibility(id_champ,data):
#     return data[id_champ][22]
#
# def return_l_comest(ids_champ,data):
#     true_comestibility=[]
#     print(ids_champ)
#     for id_champ in ids_champ:
#         print(id_champ)
#         true_comestibility.append(return_comestibility(id_champ,data))
#     return true_comestibility
#
# def return_classification(resultat,verite):
#     if (resultat==verite):
#         #positif
#         if (resultat=='e'):
#             return "vp"
#         else:
#             return "vn"
#     else:
#         #negatif
#         if (resultat=='e'):
#             return "fp"
#         else:
#             return "fn"
# def return_l_classification(resultats,verite):
#     classification = [0,0,0,0]
#     # vp,vn,fp,fn
#     state =[]
#     for i in range(len(resultats)):
#         state = return_classification(resultats[i],verite)
#         if state[0]=="v":
#             if state[1]=="p":
#                 classification[0] +=1
#             else:
#                 classification[1] += 1
#         else:
#             if state[1]=="p":
#                 classification[2] += 1
#             else:
#                 classification[3] += 1
#     return classification
#
#
# def CA(classif):
#     return( (classif[0]+classif[1])/sum(classif))
#
# def Confiance(classif):
#     return classif[0]/(classif[0]+classif[2])
#
# def Sensitivity(classif):
#     return classif[0]/(classif[0]+classif[3])
#
#
# #probleme où le programme est trop précis pour un jeu de données trop petit ? a voir asap
# def test_precision(data,test,K):
#     print("data="+str(len(data)))
#     temp=[]
#     result=[0,0,0,0]
#     result_temp=[0,0,0,0]
#
#     for i in range(len(test)):
#         temp = KNN(test[i][:-1],data,K,False)
#
#         result_temp = return_l_classification(temp[0],return_comestibility(i,test))
#         for i in range(len(result)):
#             result[i] += result_temp[i]
#
#     print("Majorité KNN ="+str(K))
#     print("CA: "+str(CA(result)))
#     print("Sensitivity: "+ str(Sensitivity(result)))
#     print("Confiance: "+str(Confiance(result)))
#     print("majorité total pondéré=")
#     print("edible="+str(temp[1][0]))
#     print("poisonous="+str(temp[1][1]))
#
#
#
# def menu():
#     ans = True
#     i = 0
#     while ans:
#         i = int(input(" 1 - Chargez un fichier(WIP) \n 2 - Faire 1-NN \n 3 - Faire K-NN \n 0 - Quitter le programme\n"))
#         if (i == 0):
#             return
#         elif (0<i and i<=3):
#             switch_menu(i)
#         else:
#             print("S'il vous plait entrez une option valide")
#
# def switch_menu(i):
#     global data
#     if(i==1):
#         print("WIP")
#     elif(i==2):
#         print("1-NN")
#         champignon = input("Entrez un individu à évaluer (valeurs séparées par des ',', comme dans le fichier chargé)\n")
#         # a faire
#         unNN(line_to_letter(champignon),data,True)
#         print("")
#     elif(i==3):
#         print("K-NN")
#         K = int(input("Entrez K\n"))
#         champignon = line_to_letter(input("Entrez un individu à évaluer (valeurs séparées par des ',', comme dans le fichier chargé)\n"))
#         KNN(champignon,data,K,True)
#         print("")
#
#
# def main():
#     global data
#     global test
#     # changez cette lignes pour changer le fichier de CSV
#     data = read_file("tp_mushrooms_dataset_150.csv")
#
#     # commentez menu et remplacez XX par le nombre de valeurs que vous voulez testez
#     menu()
#
#     ## decommentez si vous voulez testez la précision de l'algorythme
#
# ##    test= data[:XX]
# ##    data = data[XX:]
# ##    print()
# ##    test_precision(data,test,1)
# ##    print()
# ##    test_precision(data,test,5)
# ##    print()
# ##    test_precision(data,test,10)
#
# main()
#
