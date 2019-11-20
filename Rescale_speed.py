# delete speed
import re

def Deletedir(path):
   shutil.rmtree(path)


def Rescale_speed(quartier_id):

        AlreadyDone = []
        for Q in quartier_id :
            x_path = os.path.join(TestP, Q)
            
            split = Q.split('_')

            if split[4] == "rotated" :
                Dir = split[7]
                Vit = split[9]
                Rot = split[5]
            else :
                Dir = split[5]
                Vit = split[7]
                Rot = 0
            
            if (Dir,Rot) in AlreadyDone:
            Deletedir(x_path)

            else:
            #  os.path.join(self.path, id_name,"Y","pollutionMap") + ".png"
                im_path = os.path.join(x_path, "Y", "pollutionMap.png")
                image_vit = cv2.imread(im_path)
                speed = image_vit * 1.5/float(Vit)
                cv2.imwrite(im_path, speed)
                AlreadyDone.append((Dir,Rot))    




if __name__=if __name__ == "__main__":

        TrainP = "/content/drive/My Drive/Air-D/Unet-5/dataset_images/train"
        TestP = "/content/drive/My Drive/Air-D/Unet-5/dataset_images/test"

        quartier_id  = next(os.walk(TestP))[1]


  
