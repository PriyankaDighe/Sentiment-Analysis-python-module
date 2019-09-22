import json
import os
import sys
#import sent_analysis

from Naked.toolshed.shell import execute_js,muterun_js


def search_rev(uname):
    with open(r'E:\nodeprogs\node2\log.txt', encoding='utf-8') as data_file:
        output_text={}
        data = json.dumps(data_file.read())
        listdata=data.split("\n")
        l=listdata[0]
        #print(l)
        #uname=sys.argv[1]
        #x=l.lower().find(uname.lower())
        x=l.lower().find(uname.lower())
        if x==-1:
            found=0
        else:
            found=1
        x2=l.find("userImage",x)
        user=l[x:x2-8]
        output_text['username']=user
        x3=l.find("text",x)
        x4=l.find("replyDate",x)
        rvdata=l[x3+7:x4-8]
        output_text['review']=rvdata
        output_text['found']=found
        return output_text
        #sent_analysis.sent(rvdata)

#success = execute_js(r'E:\nodeprogs\node2\index.js')
#search_rev("Shamshad Sheikh")


    
