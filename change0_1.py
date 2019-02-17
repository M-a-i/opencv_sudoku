import numpy as py
import os
import PIL.Image as Image 
def changeImgFile(imgDir,num):
    #imgFileList=os.listdir(imgDir)
    #print(imgFileList)
    #imgNumber=len(imgFileList)
    #for i in range(imgNumber):
        #imgName=imgFileList[i]
        #print(imgName)
    imgName='%s.pgm'%str(num)
    imgBig=Image.open(imgDir+'/'+imgName)
    imgNormal=imgBig.resize((32,32))
    digitImg=imgNormal.convert('L')
    digit_mat=digitImg.load()
    fr=open('/home/mai/test/mydigits/%s.txt'%str(num),'w')
    for i in range(32):
        for j in range(32):
            if digit_mat[j,i]!=255:
                fr.write('1')
            else:
                fr.write('0')
        fr.write('\n')
    fr.close()

if __name__=='__main__':
    imgDir='/home/mai/img'
    changeImgFile(imgDir)