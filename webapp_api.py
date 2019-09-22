from flask import Flask, jsonify
import review_reg_test
from Naked.toolshed.shell import execute_js,muterun_js
from flask import request
import trialcall
app = Flask(__name__)
import grun
import sent_analysis
#from itertools import chain
#from collections import defaultdict

'''
@app.route('/', methods=['GET'])
def get_tasks():
    args = request.args
    choice=args['key1']
    uname=args['key2']
    city=args['key3']
    res=args['key4']
    print(choice)
    if(choice=="zomato"):
        fn_zomato(uname,city,res)
    elif(choice=="gplay"):
        fn_gplay(uname)
   
'''  
@app.route('/zomato', methods=['GET'])
def fn_zomato():
    print("inside")
    args = request.args
    uname=args['key1']
    city=args['key2']
    res=args['key3']
    dictdata={}
    dictdata2={}
    dictdata=trialcall.review(city,res,uname)
    rvtxt=dictdata['reviewText']
    url=dictdata['url']
    print("going in")
    dictdata2=review_reg_test.reg_rv(url)
    print("back")
    if(dictdata2['sent_no']==1):
        dictdata2['sentiment']="Positive review"
    elif(dictdata2['sent_no']==0):
        dictdata2['sentiment']="Negative review"
    dictdata2.pop('sent_no', None)
    return jsonify({'output1':dictdata},{'output2':dictdata2})

@app.route('/gplay', methods=['GET'])
def fn_gplay():
    print("inside gplay")
    args = request.args
    uname=args['key1']
    appid=args['key2']
    dict={}
    fnd=0
    i=0
    while(fnd==0):
        node_arg=str(i)+"+"+appid
        print(type(node_arg))
        success=execute_js(r'E:\nodeprogs\node2\index.js',node_arg)
        print(success)
        i=i+1
        dict=grun.search_rev(uname)
        found=dict['found']
        if(found==1):
            fnd=1
            dict.pop('found', None)
            textdata=dict['review']
            
            sent_dict=sent_analysis.sent(textdata)
            if(sent_dict['sent_no']==1):
                dict['sentiment']="Positive review"
            elif(sent_dict['sent_no']==0):
                dict['sentiment']="Negative review"
            dict['additional data']=sent_dict['text']
            
        elif(found==0):
            fnd=0
    return jsonify({'output':dict})

if __name__ == '__main__':
    app.run(debug=True)