#!/usr/bin/python3
#EjMap

import sys

for Line in sys.stdin:
    Data = Line.strip().split(",")
    if len(Data) == 19:
        imei,marca,mod,mos, exito,error,fecha,
        hora,mnc,tred,rb,lat,longi,db,
        tasaDn,tasaUp,tasaLoss,delay,jitter =Data
       print ("{0}\t{1}".format(mnc,db))
