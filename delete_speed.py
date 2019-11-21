import numpy as np
import math
import os,errno
import glob
import pathlib
import shutil


quartier_id  = next(os.walk(TrainP))[1]
print(quartier_id, len (quartier_id))

for p in quartier_id:
  spd = os.path.join(TrainP,p,"X","speed.png")
  if os.path.exists(spd) : 
      os.remove(spd)
      print(" file {} remove ".format(spd))
  else:
    continue


