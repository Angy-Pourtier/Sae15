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

tab_event=np.array([])
f=open("sae.csv", "w")

evenement = "DATE ; SOURCE ; PORT ; DESTINATION ; FLAG ; SEQ ; ACK ; WIN ; OPTIONS ; LENGTH" 
f.write(evenement + "\n") 

characters = ":" 



for event in ress:
        if event.startswith('11:42'):
            seq = ""
            heure1 = ""
            nomip = ""
            port = ""
            flag = ""
            ack = ""
            win = ""
            options = ""
            length = ""
            txt=event.split(".")
            heure1=txt[0]
            
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
            #port
            if len(txt) > 1: 
                port1=txt[2].split(".")
                port=port1[-1]
            txt=event.split(" ")
            p2=txt[4]
            txt=event.split("[") 
            if len(txt) > 1: 
                flag1=txt[1].split("]") 
                flag=flag1[0]
            #seq
            txt=event.split(",")
            if len(txt) > 1:
                if txt[1].startswith(" seq"):
                    seq1=txt[1].split(" ") 
                    seq=seq1[2]
            #ack
            if len(txt) > 2: #
                if txt[2].startswith(" ack"):
                    ack1=txt[2].split(" ") 
                    ack=ack1[2] 
                
                if txt[1].startswith(" ack"): 
                    ack1=txt[1].split(" ")
                    ack=ack1[2]
                    
            if len(txt) > 3: 
                
                if txt[3].startswith(" win"): 
                    win1=txt[3].split(" ") 
                    win=win1[2] 
               
                if txt[2].startswith(" win"):
                    win1=txt[2].split(" ")
                    win=win1[2]
            
            txt=event.split("[") 
            if len(txt) > 2: 
                options1=txt[2].split("]") 
                options=options1[0]
            
            #length (avec option)
            txt=event.split("]") 
            if len(txt) > 2:
                    length1=txt[2].split(" ")
                    length=length1[2]
            #length (sans option)
            txt=event.split(",")
            if len(txt) > 3:
                if txt[3].startswith(" length"):

                    
                    length1=txt[3].split(" ") 
                    length=length1[2] 
                    length = length.replace(characters,"")
            if event.startswith("11:42:55.536521") :
                prog=0 
            evenement=heure1+";"+nomip+ ";" +port+ ";" + p2+ ";"+flag+ ";" +seq+ ";" +ack+ ";" +win+ ";" +options+ ";" +length
            tab1=heure1
            tab2=ack
            f.write(evenement + "\n") 
 
            
 
            if nomip=="190-0-175-100.gba.solunet.com.ar":
                a = a + 1
                
            if nomip=="BP-Linux8":
                b = b + 1
                
            if nomip=="mauves.univ-st-etienne.fr":
                c = c + 1
                
            if nomip=="ns1.lan.rt.":
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
                
            if nomip=="www.agloroanne.fr":
                k = k + 1 
            if nomip=="192.168.190.130":
                z = z + 1

x=["190-0-175-100.gba.solunet.com.ar","BP-Linux8","mauves.univ-st-etienne.fr","ns1.lan.rt.","par10s38-in-f3.1e100.net","par21s04-in-f4.1e100.net","par21s04-in-f4.1e100.net","par21s23-in-f10.1e100.net","par21s23-in-f3.1e100.net","www.agloroanne.fr","192.168.190.130"]
y = [a,b,c,d,e,m,g,h,i,k,z]
fig, ax = plt.subplots(figsize=(20, 10))

ax.set_yticks(np.arange(0, 4000, 250))
ax.set_title( "SOURCE", color="#000000", y=1.05)
fig.autofmt_xdate(rotation=45)

ax.bar(x, y)

fig.savefig("destinationbar.png", dpi=300, bbox_inches="tight")





x=["184.107.43.74","BP-Linux8.34862:","mauves.univ-st-etienne.fr","BP-Linux8.40678:","BP-Linux8.40682:","www.agloroanne.fr","BP-Linux8.53324:","BP-Linux8.53325:","BP-Linux8.53328:","BP-Linux8.53329:","192.168.190.130"]
y = [2000,827,251,383,400,1022,499,385,352,324,66]
fig, ax = plt.subplots(figsize=(20, 10))

ax.set_yticks(np.arange(0, 4000, 250))
ax.set_title( "DESTINATION", color="#000000", y=1.05)
fig.autofmt_xdate(rotation=45)

ax.bar(x, y)

                                                              
fig.savefig("sourcebar.png", dpi=300, bbox_inches="tight")


plt.show()            
f.close()

