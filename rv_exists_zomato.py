import requests
import json

#city="pune"
#restaurant_name="JOEYS"
#uname="Gayatri Jadhav"
url=""
def exists(city,restaurant_name,uname):
    user_review=""
    
    payload={'q':city}
    r = requests.get('https://developers.zomato.com/api/v2.1/cities',headers={"user-key":"b53653988fd9002ea1fb657a04dfdd3e"},params=payload)
    data=json.loads(r.text)
    cityid=data['location_suggestions'][0]['id']
    
    payload={'entity_type':'city','entity_id':cityid,'q':restaurant_name}
    
    r = requests.get('https://developers.zomato.com/api/v2.1/search',headers={"user-key":"b53653988fd9002ea1fb657a04dfdd3e"},params=payload)
    data=json.loads(r.text)
    
    resdt=data["restaurants"][0]["restaurant"]
    url=resdt['url']
    resid=(resdt["R"]["res_id"])
    
    payload2={'res_id':resid}
    
    r2 = requests.get("https://api.zomato.com/v1/reviews.json/{0}/user?count=0&apikey=b53653988fd9002ea1fb657a04dfdd3e".format(resid))
    
    r2dt=json.loads(r2.text)
    
    list_reviews=r2dt['userReviews']
    
    for x in list_reviews:
        if (x['review']['userName']==uname):
            rv=x['review']
            #for i in rv:
                #print (i,":",rv[i])
    rv['url']=url
    return rv
            #user_review=rv['reviewText']
            
            
