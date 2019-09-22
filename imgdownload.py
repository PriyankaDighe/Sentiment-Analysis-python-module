

import urllib.request
import os
import ocrextract
import review_reg_test
import rv_exists_zomato
import csv


def imgsave(url,path):
    #url="https://s3.ap-south-1.amazonaws.com/hinge.two.dev/taskApplicationImages/taskImageuvj2UkiYKx1512817532731.webp"
    #dirpath="E:\\sampleimages\\FinalRv\\"
    fileinput="E:\\sampleimages\\FinalRv\\"+path
    index=path.find('.webp')
    path2=path[:index]
    fileoutput="E:\\sampleimages\\FinalRv\\"+path2+".png"
    urllib.request.urlretrieve(url,fileinput)
    print(fileoutput,fileinput)
    command="C:\\Users\\priyankadighe\\Downloads\\libwebp\\libwebp-0.6.1-windows-x64\\bin\\dwebp.exe "+fileinput+" -o "+fileoutput
    os.system(command)

city=input("Enter City name")
res=input("Enter Restaurant name")
uname=input("Enter user name")
fw=open(r'E:\sampleimages\FinalRv\links.csv',"r")
reader = csv.reader(fw,delimiter=',')
for row in reader:
    for word in row:
        s=word.rfind('/')
        fi=word.find('.webp')
        word2=word[s+1:fi+5]
        # print(word,word2)
        if word and word2:
            strz=word2+","
            print(strz)
            fw3=open(r'E:\sampleimages\FinalRv\picname.csv',"a")
            fw3.write(strz)
            fw3.close()
            imgsave(word,word2)
            
ocrextract.extractreview()
url=rv_exists_zomato.exists(city,res,uname)
review_reg_test.reg_rv(url)
