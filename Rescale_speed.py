## Imports
import sys
import random
import math
import os,errno
import glob
import pathlib
import shutil
import numpy as np
import copy
import cv2


# delete speed


# new_path = "/content/drive/My Drive/Air-D/Unet-5/dataset_images" 

TrainP ="C:\\Work\Air-D\\pour_marouane\\dataset_images\\dataset_images"

quartier_id  = next(os.walk(TrainP))[1]
print(len(quartier_id) )


# def delete_speed(quartier_id) :
#         for p in quartier_id:
#             spd = os.path.join(TrainP,p,"X","speed.png")
#             if os.path.exists(spd) : 
#                  os.remove(spd)
#                  print(" file {} remove ".format(spd))
#             else:
#                 continue


def Deletedir(path):
   shutil.rmtree(path)

# AlreadyDone = []

delete_speed(quartier_id)

for Q in quartier_id:
      
     x_path = os.path.join(TrainP, Q)
     split = Q.split('_')
     name_quartier = split[3]


     if split[4] == "rotated" :
        Dir = split[7]
        Vit = split[9]
        Rot = split[5]
     else :
        Dir = split[5]
        Vit = split[7]
        Rot = 0
     
     if (name_quartier, Dir, Rot) in AlreadyDone:

        Deletedir(x_path)
        print(" Remove ... {}".format(Q))

     else:
        im_path = os.path.join(x_path, "Y", "pollutionMap")
        
        try:

            if os.path.exists(im_path+".png"):
                  image_vit = cv2.imread(im_path+".png",cv2.IMREAD_GRAYSCALE)

                  cv2.imshow(Q,image_vit)
                  print(" ")

                  speed = image_vit * float(Vit)/1.5
                  speed = np.around(speed)
                  speed = speed.astype(np.uint8)

                #   cv2.imshow('transformed',speed)
                  cv2.imwrite(im_path+".png", speed)
                  
                  print(" ")
                  if not cv2.imwrite(im_path+".png", speed):
                        raise Exception("Could not write image")

                  AlreadyDone.append((name_quartier,Dir,Rot))      
        except : 
            print(" image {} does not exist ".format(im_path))
