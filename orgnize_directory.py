import os
import shutil

currnet_path = os.path.dirname(os.path.realpath(__file__))
print('cureent dir: ',currnet_path)


for filename in os.listdir(currnet_path):
    #orgnize image into Image folder
    if filename.endswith(('.jpg','.png')):
        if not os.path.exists("Images"):
            os.mkdir('Images')
        shutil.copy(filename,"Images")
        os.remove(filename)
        print("image done")

    #orgnize Archive into Archive folder
    elif filename.endswith(('.jpg','.png')):
        if not os.path.exists("Archive"):
            os.mkdir('Archive')
        shutil.copy(filename,"Archive")
        os.remove(filename)
        print("image done")
    #orgnize image into Image folder
    elif filename.endswith(('.jpg','.png')):
        if not os.path.exists("Images"):
            os.mkdir('Images')
        shutil.copy(filename,"Images")
        os.remove(filename)
        print("image done")
    #orgnize image into Image folder
    elif filename.endswith(('.jpg','.png')):
        if not os.path.exists("Images"):
            os.mkdir('Images')
        shutil.copy(filename,"Images")
        os.remove(filename)
        print("image done")
    elif filename.endswith(('.jpg','.png')):
        if not os.path.exists("Images"):
            os.mkdir('Images')
        shutil.copy(filename,"Images")
        os.remove(filename)
        print("image done")
