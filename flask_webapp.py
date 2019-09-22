from flask import Flask, jsonify
#from itertools import chain
#from collections import defaultdict
import review_reg_test
#from Naked.toolshed.shell import execute_js,muterun_js
from flask import request
import trialcall
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

if __name__ == '__main__':
    app.run(debug=True)