#print("Tund on alanud")
#hilinemine=input("Kas �pilane on hilinenud")
## "JAH"-a.upper(), "jah"-a.lower(),"Jah"-a.capitalize(),jAH
#if hilinemine.lower()=="jah":
#    print("�pilane ootab 30 min")
#print("�pilane astub klassi")

#arv=randint(0,100) #juhuslik t�isarv vahemikust 0...100

#print(arv)
#if arv%2==0:
#    print(arv,"on paaris arv")
#else:
#    print(arv,"on paaritu arv")
#print()

#from random import *
#protsent=randint(-100,500) #0-100 0-60-"2", 61-75-"3", 76-89-"4", 90-100-"5"

#print(protsent,"% testi tulemus")
#if protsent<0 or protsent>100:
#    tulemus="valed andmed"
#elif 0<protsent<60: #protsent>0 and protsen<60, protsent<60
#        tulemus="hinne 2"
#elif 60<=protsent<75:
#    tulemus="hinne 3"
#elif 75<=protsenti<90:
#    tulemus="hinne 4"
#else: #elif  90<=protsent<=100:
#    tulemus="hinne 5"
#print(tulemus)
#print()

##Juku l�hes kinnos
#nimi=input("Mis on teie nimi?").capitalize
#print("Tere,",nimi)
#if nimi=="Juku" :
#    print("sa l�hed kinno")
#    vanus=int(input("Kui vana sa oled?"))
#    if vanus<0 or vanus>100:
#        pilet="vale vanus"
#    elif vanus<6:
#        pilet="tasuta pilet"
#    elif vanus<=14:
#        pilet="lastepilet"
#    elif vanus<=65:
#        pilet="t�ispilet"
#    elif vanus<=100:
#        pilet="sooduspilet"
#    print(pilet) #ilus ja �ige vastus!"Vale vanus"on vaja osta..."
#else:
#    print("Juku ei l�he kinno")

   # from datetime import *
   # from random import *
   # #8 Poes
   # arve_nr= date.today()#datetime.now()
   # print(arve_nr)
   # tsekk="Arve: "+str(arve_nr)+"nToode Hind Kogus Summa n"
   # summa=0

   # toode="Piim"
   #hind=randint(50,10)/100
   #v=input("Toode: "+toode+" Hind: "+str(hind)+"/nKas tahad osta?").lower()
   #if v=="jah":
   #    mitu=int(input("Mitu? "))
   #    tsekk+=toode+" "+str(hind)+" "+str(mitu)+" "+str(mitu*hind)+"/n"
   #    summa+=mitu*hind
   #toode="Leib"
   #hind=randiot(600,1500)/100
   #v=input("Toode:"+toode+" Hind:"+str(hind)+"/nKas tahad osta?").lower()
   #if v=="jah":
   #    mitu=int(input("Mitu?"))
   #    tsekk+=toode+" "+str(hind)+" "+str(mitu)+" "+str(mitu*hind)+"/n"
   #    summa+=mitu*hind
   # tsekk+="Kokku maksta: "+str(summa)
   # print(tsekk)
   # raha=float(input("Maksa "+str(summa)))
   # if raha==summa:
   #     print("T�nan ostu eest!")
   # elif raha>summa:
   #     print("T�nan ostu eest! Tagasi "+str(raha-summa))
   #  else:
   #      print("Maksa veel"+str(summa-raha))


  #from datetime import *
  #from random import *
  ##8.2 Poes
  #arve_nr= date.today()#datetime.now()
  #print(arve_nr)
  #tsekk="Arve: "+str(arve_nr)+"nToode Hind Kogus Summa n"
  #summa=0
  #for toode in ["Piim","Leib","Komm"]:
  #    hind=randit(50,100)/100
  #    v=input("Toode: "+toode+" Hind: "+str(hind)+"/nKas tahad osta?").lower()
  #    if v=="jah":
  #        mitu=int(input("Mitu? "))
  #        tsekk+=toode+" "+str(hind)+" "+str(mitu)+" "+str(mitu*hind)+"/n"
  #        summa+=mitu*hind
  # tsekk+="Kokku maksta: "+str(summa)
  # print(tsekk)
  # while True:
  #     raha=float(input("Maksa "+str(summa)))
  #     if raha==summa:
  #         print("T�nan ostu eest!")
  #         break
  #     elif raha>summa:
  #         print("T�nan ostu eest! Tagasi")(raha-summa)
  #         break
  #     else:
  #         summa==raha
  #         print("T�nan ostu eest! Tagasi "+str(summa))

#from datetime import *
#from random import *
##11
#ta=date.today().year()
#print(ta)
#sp=date(int(input("S�nniaastat: ")),int(input("S�nnikuu: ")),int(input("S�nnip�ev: "))).year
#if (ta-sp)%5==0:
#    print("Jubell")
#else:
#    print("Tavaline sunnip�ev")

##14
#math=int(input("Bussu math: "))
#i=int(input("Inimeste arv: "))
#ba=round(i/math) #2,3->2
#if i%math!=0:
#    ba+=1
#vb=i%aht
#print("Kokku on vaja {0} bussi ja viimasel s�idavad {1} inimest".format(ba,vb))



#�lesanded
#1
#for
#r=0
#for i in range(15):
#    arv=float(input("Sisesta {0}.arv".format(i+1)))
#    if arv==int(arv):
#        r+=1
#print("T�isarvude arv on "+str(r))
##While True
#r=0
#while True:
#    i+=1
#    arv=float(input("Sisesta {0}.arv".format(i)))
#    if arv==int(arv):
#        r+=1
#    if i==15: break
#print("T�isarvude arv on "+str(r))
	
#15 
#for j in range(0,10,1):
#	for i in range(0,10,1):
#		print(f"{i}",end=" ")
#	print()

