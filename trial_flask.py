from flask import Flask, jsonify
import grun
from Naked.toolshed.shell import execute_js,muterun_js
import sent_analysis
from flask import request

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]

@app.route('/', methods=['GET'])
def get_tasks():
    args = request.args
    #print (args)
    uname=args['key1']
    dict={}
    fnd=0
    i=0
    while(fnd==0):
        success=execute_js(r'E:\nodeprogs\node2\index.js',str(i))
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