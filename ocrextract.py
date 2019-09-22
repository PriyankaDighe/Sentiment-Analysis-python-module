import requests
import json
import csv

def ocr_space_file(filename, overlay=False, api_key='135596f5b588957', language='eng'):

    payload = {'isOverlayRequired': overlay,
               'apikey': api_key,
               'language': language,
               }
    with open(r'%s'%filename, 'rb') as f:
        r = requests.post('https://api.ocr.space/parse/image',
                          files={filename: f},
                          data=payload,
                          )
    return r.content.decode()


def ocr_space_url(url, overlay=False, api_key='135596f5b588957', language='eng'):

    payload = {'url': url,
               'isOverlayRequired': overlay,
               'apikey': api_key,
               'language': language,
               }
    r = requests.post('https://api.ocr.space/parse/image',
                      data=payload,
                      )
    return r.content.decode()

def extracttext(word,fw):
    #print("Extract text")
    index=word.find('.webp')
    path=word[:index]
    print(path)
    filenm="E:\sampleimages\FinalRv\\"+path+".png"
    print(filenm)
    #filenm=r'E:\\sampleimages\\FinalRv\\'+path+".png"
    
    test_file =ocr_space_file(filename=filenm)
    test_file=json.loads(test_file)
    #print(test_file)
    #print(type(test_file))
    try:
        datadict=test_file["ParsedResults"]
        #print(datadict[0])
        strdata=json.dumps(datadict[0])
        #print(type(strdata))
        #list1=test_file["ParsedResults"]
        #print (list1)
        #str1=','.join(map(str,list1))
        i=strdata.find("ParsedText")
        j=strdata.find("ErrorMessage")
        #print(str1)
        str2=strdata[i+14:j-4]
        str3=str2.replace("\\r\\n"," ")
        word=path+".png"
        strprint=word+","+str3+"\n";
        print(strprint)
        fw.write(strprint)
        #print(count)
        #count=count+1;
        fw.close()
    
    except:
        print("caught")
    

def extractreview():
    with open(r'E:\sampleimages\FinalRv\picname.csv','r') as f:
            
        reader = csv.reader(f,delimiter=',')
        for row in reader:
            for word in row:
                print("word is",word)
                fw=open(r'E:\sampleimages\FinalRv\reviewtxt.csv',"a")
                #print("calling extract text")
                if word:
                    extracttext(word,fw)
            
