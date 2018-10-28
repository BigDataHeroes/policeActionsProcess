#!/usr/bin/python

#imports
import io
import pandas as pd
import os
import math
import numpy as np
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
inputF = sys.argv[1]
outputF = sys.argv[2]

# Metodos necesarios
def LimpiarBarrio(pBarrio):
  pBarrio=pBarrio.strip() 
  if (pBarrio[0].isdigit()):
    return pBarrio[4:]
  else:
    return pBarrio

#Visualizamos que tenemos
df = pd.read_csv(inputF,delimiter=';',dtype=str)

# generamos un .csv que sea facil de entender para el Tableau
mCsv="Barrio;Anyo;Intervenciones" +os.linesep

#generamos el texto que tendra el -csv a la vez que limpiamos los datos
vAnyo=2006  
for row in df.iterrows():
  if (not isinstance(row[1][0], float)):
    if (row[1][0].isdigit()):
      vAnyo=row[1][0]
    else:
      vIntervenciones = row[1][1]
      vNewLine =LimpiarBarrio(row[1][0])+";"+str(vAnyo)+";"+str(vIntervenciones)+os.linesep
      mCsv = mCsv +vNewLine

#Guardamos el .csv en el disco, en la zona ODS
f = open(outputF,'w')
f.write(mCsv)
f.close()


