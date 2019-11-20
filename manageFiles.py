import numpy as np
import math
import os,errno
import glob
import pathlib
import shutil


""""""""
# author: Marou

""""""""

def CreateDir(path):
#define the name of the directory to be created
    print(" ")
    try:
       if not os.path.exists(path):
            os.makedirs(path)         
    except OSError:
         print ("Creation of the directory %s failed" % path)
     else:
         print ("Successfully created the directory %s " % path)


def MoveToDir(path1,path2):
     #Move a file from the directory d1 to d2
     shutil.move(path1, path2)

def Load(path_principale,newpath):
##create new quartier
    for j in range(1,13):
        path = os.path.join(newpath, "quartier_"+str(j))
        CreateDir(path)
# Training Ids
    train_ids = next(os.walk(path_principale))[1]
    for i in train_ids:
          id =int(i.split('_')[3])
          src = os.path.join(path_principale, str(i))
          dst =  os.path.join(newpath, "quartier_"+str(id))
          print(dst)
# move data to their correspondant quartier
          shutil.move(src, dst)

def getFolderSize(folder):
    total_size = os.path.getsize(folder)
    for item in os.listdir(folder):
        itempath = os.path.join(folder, item)
        if os.path.isfile(itempath):
            total_size += os.path.getsize(itempath)
        elif os.path.isdir(itempath):
            total_size += getFolderSize(itempath)
    return total_size

# if folder empty, delete it
def RemoveDir(path):
    #4096 is the size of an empty file in google drive
    [ os.rmdir(os.path.join(path, x)) for x in os.listdir(path) if getFolderSize(os.path.join(path, x)) <= 4096 ]


# how to use it

# if __name__ == "__main__":
#     path_principale = "/content/drive/My Drive/Air-D/Unet-5/dataset_images/"
#     newpath = "/content/drive/My Drive/Air-D/Unet-5/new_dataset_images"
#     Load(path_principale,newpath)
#     RemoveDir(newpath)