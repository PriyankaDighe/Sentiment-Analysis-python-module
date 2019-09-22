import rv_exists_zomato
from flask import request

def review(city,res,uname):
   
    dictdata={}
    dictdata=rv_exists_zomato.exists(city,res,uname)
    return dictdata
