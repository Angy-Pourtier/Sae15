import numpy as np
import datetime
import os
import csv
import typing
import matplotlib.pyplot as plt
import numpy as np

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
            f.write(evenement + "\n") 
f.close()