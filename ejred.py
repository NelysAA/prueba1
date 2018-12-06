#!/usr/bin/python3
# EjReduce

import sys

dbGlobal=0.0 
regsGlobal=0
dbMNC=0.0
regsMNC=0
mncAnt = None

for line in sys.stdin:
    DataIn = line.strip().split("\t")
    if len(DataIn) != 2:
        continue

    esteMNC, estedb  = DataIn
    x= int(estedb)
   if x < -144 or x > -44:
      continue;
  
   if mncAnt  and mncAnt != esteMNC:
       if regsMNC !=0:
           avgdbMNC=dbMNC/regsMNC
           print (mncAnt, "\t", avgdbMNC)
       else:
           print (mncAnt, "\t", 0.0)

      dbMNC = 0.0
      regsMNC = 0

   mncAnt = esteMNC
   dbMNC += x
   regsMNC += 1
   dbGlobal += x
   regsGlobal += 1

if mncAnt != None:
   if regsMNC != 0:
           avgdbMNC=dbMNC/regsMNC
           print (mncAnt, "\t",avgdbMNC)
       else:
           print (mncAnt, "\t",0.0)

if regsGlobal != 0:
           avgdbGlobal=dbGlobal/regsGlobal
           print ("Intensidad global: \t",avgdbGlobal)
       else:
           print ("Intensidad global: \t",0.0)