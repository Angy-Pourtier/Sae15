#VERY IMPORTANT: if you copy my programme don't forget to change the start and end date of the programme

#We import what we need

import numpy as np
import datetime
import os
import csv
import typing
import matplotlib.pyplot as plt
import numpy as np

a = int 
a = 0

b = int
b = 0

c = int
c = 0

d = int
d = 0

e = int
e = 0

m = int 
m=0

g = int
g = 0

h = int
h = 0

i = int
i = 0

k = int
k = 0

z = int
z = 0

try:
    with open("fichier.txt", encoding="utf8") as fh:
        res=fh.read()
except:
        print("Fichier inéxistant... %s", os.path.abspath('fichieratraiter.txt'))
ress=res.split('\n')

#We check if the file exists otherwise error

tab_event=np.array([])
f=open("sae.csv", "w") 

#This file will be the destination for information extractions with the permission "w" to write

evenement = "DATE ; SOURCE ; PORT ; DESTINATION ; FLAG ; SEQ ; ACK ; WIN ; OPTIONS ; LENGTH" 
f.write(evenement + "\n") #We name the collones

characters = ":" #define a variable with the character ":" for the following



for event in ress:
#I'm saying that for any event that starts with "11:42" I do what's in the loop
        if event.startswith('11:42'):  #WARNING: It is this date that you must change according to the information in your file
#Create variables and reset them to 0 
            seq = ""
            heure1 = ""
            nomip = ""
            port = ""
            flag = ""
            ack = ""
            win = ""
            options = ""
            length = ""
#For the date (first column)
            txt=event.split(".")
            heure1=txt[0]
#Source (2nd column)            
            txt=event.split(" ")
            p1=txt[2].split(".")
            
            
            if len(p1) == 2:
                nomip=p1[0]
            if len(p1) == 3:
                nomip=p1[0]+ "." +p1[1]
            if len(p1) == 4:
                nomip=p1[0]+ "." +p1[1]+ "." +p1[2] 
            if len(p1) == 5:
                nomip=p1[0]+ "." +p1[1]+ "." +p1[2]+ "." +p1[3]
            if len(p1) == 6:
                nomip=p1[0]+ "." +p1[1]+ "." +p1[2]+ "."+p1[3]+"."+ p1[4]
#Port (3rd column)
            if len(txt) > 1: 
                port1=txt[2].split(".")
                port=port1[-1]
#Destination (4th column)
            txt=event.split(" ")
            p2=txt[4]
#Flag (5th column)
            txt=event.split("[")    #I say I cut from the hook
            if len(txt) > 1: #I say that if there is more than one part from the hook I make..
                flag1=txt[1].split("]") #I tell him to take after the first hook and I cut at the second hook
                flag=flag1[0]  # because I take the left part of the second hook because that's what I'm looking for
#Seq (6th column)
            txt=event.split(",")  #I tell him to cut off at the comma
            if len(txt) > 1:
                if txt[1].startswith(" seq"): #I tell him that if the text [1] starts with "seq" then
                    seq1=txt[1].split(" ") #I tell him to cut at the space and take the text right after
                    seq=seq1[2]  #I have 2 parts between the split « , » and what I am looking for
#ACK (7th column)
            if len(txt) > 2: 
                if txt[2].startswith(" ack"):  #If the text [2] starts with "ack".
                    ack1=txt[2].split(" ")   #I cut at the space and take the text right after
                    ack=ack1[2]  #I have 2 parts between the split « , » and what I am looking for
                
                if txt[1].startswith(" ack"): 
                    ack1=txt[1].split(" ")
                    ack=ack1[2]
#WIN (8th column)
                    
            if len(txt) > 3: 
                
                if txt[3].startswith(" win"): 
                    win1=txt[3].split(" ") 
                    win=win1[2] #I take the text after the space because this is the part that will be found in the table
               #I tell him that if "ack" is not present then...
                if txt[2].startswith(" win"):
                    win1=txt[2].split(" ")
                    win=win1[2]
  
#OPTIONS (9th column)          
            txt=event.split("[")  #I tell him to cut from the hook
            if len(txt) > 2: 
                options1=txt[2].split("]")  #I start from the first "[" and the text [2] so that we get to what we want to recover
                options=options1[0]
            
            #length (with options option)
            txt=event.split("]") 
            if len(txt) > 2:    #I check the number of parts from split to hook
                    length1=txt[2].split(" ")
                    length=length1[2]
            #length (without option)
            txt=event.split(",")
            if len(txt) > 3:
                if txt[3].startswith(" length"):   #If it starts with "length" and we search the text [3] then ...                   
                    length1=txt[3].split(" ")  
                    length=length1[2] 
                    length = length.replace(characters,"") #I replace "characters" with " " to avoid the spreadsheet writing as a date
            if event.startswith("11:42:55.536521") :  #When the program reaches the last line of the text file then ...
#WARNING: It is this date that you must change according to the information in your file
                prog=0    #To tell him to stop spinning
            evenement=heure1+";"+nomip+ ";" +port+ ";" + p2+ ";"+flag+ ";" +seq+ ";" +ack+ ";" +win+ ";" +options+ ";" +length
            f.write(evenement + "\n") #I write "event" in the csv and return to the line
         


#En dessous se trouve le code si vous voulez continuer en créant deux graphique qui vous permettrons de savoir toute les sources et destination de ce fichier. Et n’oubliez pas de prendre en dessous de cette partie les deux lignes qui permettent de fermer les fichers .
#Here in these "if" each time it crosses an ip name it adds + 1 to it so that the order moves automatically and the graph updates itself if it changes

            if nomip=="190-0-175-100.gba.solunet.com.ar":
                a = a + 1
                
            if nomip=="BP-Linux8":
                b = b + 1
                
            if nomip=="mauves.univ-st-etienne.fr":
                c = c + 1
                
            if nomip=="ns1.lan.rt":
                d = d + 1
                
            if nomip=="par10s38-in-f3.1e100.net":
                e = e + 1
              
            if nomip== "par21s04-in-f4.1e100.net":
                m = m +1
                
            if nomip=="par21s17-in-f1.1e100.net":
                g = g + 1
                
            if nomip=="par21s23-in-f10.1e100.net":
                h = h + 1
                
            if nomip=="par21s23-in-f3.1e100.net":
                i = i + 1
                
            if nomip=="www.aggloroanne.fr":
                k = k + 1 
           
            if nomip=="192.168.190.130":
                z = z + 1


#Here I will enter if I want it to be on the x-axis and y-axis
x=["190-0-175-100.gba.solunet.com.ar","BP-Linux8","mauves.univ-st-etienne.fr","ns1.lan.rt.","par10s38-in-f3.1e100.net","par21s04-in-f4.1e100.net","par21s04-in-f4.1e100.net","par21s23-in-f10.1e100.net","par21s23-in-f3.1e100.net","www.agloroanne.fr", "192.168.190.130"]
y = [a,b,c,d,e,m,g,h,i,k,z]
fig, ax = plt.subplots(figsize=(20, 10))  #I initialise the size of the graph
#I tell him to order them to start the graph at 0 with 4000 height and separate it by 500         
ax.set_yticks(np.arange(0, 4000, 250))
ax.set_title( "SOURCE", color="#000000", y=1.05)
fig.autofmt_xdate(rotation=45)
#I put the text x of the abscissa with a rotation of 45 and I display the bars
ax.bar(x, y)
#And I save the graphic as a png for later
fig.savefig("destinationbar.png", dpi=300, bbox_inches="tight")





x=["184.107.43.74","BP-Linux8.34862:","mauves.univ-st-etienne.fr","BP-Linux8.40678:","BP-Linux8.40682:","www.agloroanne.fr","BP-Linux8.53324:","BP-Linux8.53325:","BP-Linux8.53328:","BP-Linux8.53329:", "192.168.190.130"]
y = [2000,827,251,383,400,1022,499,385,352,324,6]
fig, ax = plt.subplots(figsize=(20, 10))

ax.set_yticks(np.arange(0, 4000, 250))
ax.set_title( "DESTINATION", color="#000000", y=1.05)
fig.autofmt_xdate(rotation=45)

ax.bar(x, y)

                                                              
fig.savefig("sourcebar.png", dpi=300, bbox_inches="tight")



#Pour fermer les fichier
plt.show()            
f.close()
