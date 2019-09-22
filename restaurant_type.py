'''
Created on Jan 7, 2018

@author: priyankadighe
'''
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def res_type(url):
    nvg=0
    driver = webdriver.Chrome("C:\Chrome Driver\chromedriver")
    driver.get(url)
    time.sleep(3)
    
    wait = WebDriverWait(driver, 30)
    
    body = wait.until(EC.presence_of_element_located((By.XPATH,"/html/body")))
    #print(type(body.text))
    #print(body.text)
    
    x=body.text.find("Vegetarian Only")
    
    
    if x>0:
        print("Vegetarian restaurant")
        nvg=1
        
    driver.quit()
    return nvg

'''
Output:
Zomato Gold — An Exclusive Members Club. Coming Soon. • KNOW MORE
Products for Businesses We're hiring
Pune
Search
Log in Create an account
Get the App
Order Food
Book a Table
Home
India
Pune
Koregaon Park
Sautéed Stories
Temporarily Closed
All Photos
Food
Ambience
Sautéed Stories
Koregaon Park
  ·  Café, Casual Dining
4.1/5
772 votes
Bookmark
Been Here
Add a Review
Rate
Add to collection
Overview
Menu
Reviews (772)
Photos (1519)
PHONE NUMBER
Number not available
Cuisines
Cafe, Italian, Continental, Salad
Average Cost 
₹850 for two people (approx.) 
Exclusive of applicable taxes and charges, if any
Cash and Cards accepted
Address
Plot 5, Between Lane 5/6, North Main Road, Opposite Wellness Forever
Sautéed Stories address, Sautéed Stories location
Get Directions
More Info
Home Delivery
Wheelchair Accessible
Vegetarian Only
Table booking not available
No Alcohol Available
Board Games
Outdoor Seating
Pet Friendly
Live Sports Screening
Smoking Area
Featured in Collection
Veggie Friendly
Report Error
Claimed listing 
What people love here NEW
Food
Bbq Mushroom Pizza, Veggie Pizza, Honey Chilli Fries, Exotic Veg Pizza, Hot Chocolate, Picante Pizza, Iced Peach Tea
Service
Friendly Staff, Prompt Service
Look & Feel
Decor, Cozy Place, Cozy Ambience
Menu
+7 pages
Recommended Dishes
Dark Chocolate Mousse, Honey Chilli Fries, Speedy Spaghetti, Pizza Picante
Photos
+1515 photos
Add Photos
Reviews
TUHINA BHATTACHARYA and 771 others have reviewed this place
Popular 
14
All Reviews 
772
Delivery Reviews 
2
Blogs 
3
Date
 ↓
Poornima Daga
24 Reviews , 184 Followers
Follow
4 months ago
RATED
  The place is as eccentric as it's name. Quirky architecture, mellow vibe and really good food that does not shy away from healthy proportions. Would recommend for a laid back afternoon to cozy up with a book, catch up with your lot or perhaps even for a meet cute with a date.
Like
4
Comment
0
Share
Rutika Kulkarni
79 Reviews , 578 Followers
Follow
4 months ago
RATED
  Is it a bulb or is it a mocktail.?
.
.
A mocktail in a bulb - Quite innovative I must say!
.
.
Mango Spicy Margarita @sauteedstories , Pune
.
.
Sautéed Stories has a very different and innovative way of doing mocktails.. .
.
#vegetarian #vegetarianfood #vegetariansofig #sauteed #sauteedstories #pune #punefoodie #punebhukkad #punekar #koregaonpark #mangospicymargarita #mangolovers #dailyigers #instafoodie #loveformocktails #healthylifestyle #nomnom #instalike #instashare #followme #followforlike #followforfollow #tagsforlikes
Like
4
Comment
0
Share
Harshil Dawda
115 Reviews , 327 Followers
Follow
4 months ago










RATED
  Average place offering below average food.

We were a group of 7 with a few kids to add to the chaos in the already packed restaurant. Since this was an after dinner meet, we could not order too many things on the menu.

But we did order a few things, and oh, how much we had to repent for it. We ordered mac n cheese, barbecued mushroom pizza and ratatouille. The mac n cheese was the worst we could have ever had, with the taste of uncooked flour apparent to everyone who tried it. It also had sweet corn! Rubbish. We returned it and got the same dish with a few modifications. I would really think they would have made us a fresh dish, but there was nothing we could do about it. The ratatouille was average and hardly had anything to appreciate. The pizza was alright.

We also ordered a ton of shakes, salted caramel, hazelnut frappe, cold coffee, Oreo shake and what not. All the shakes were decent, and I specially liked my salted caramel shake. Dessert was a massive... read more
— with Tarun Jain, Varun Marlecha and Kalpesh Jain
Like
0
Comment
0
Share
Kunaljain
29 Reviews , 657 Followers
Follow
4 months ago
RATED
  One of the very few places in koregaon park serve good pasta.
The concept is unique.
You can really have alcohol at very cheap rate here. Really loved the concept.
Pasta both white and red are really delicious.
Like
1
Comment
0
Share
Pavan Undare
19 Reviews , 336 Followers
Follow
4 months ago







RATED
  If you had to choose between losing weight and Chocolate....
Would you like it dark,white or with milk ? 🍫
..
This heavenly exquisite Frozon Hot Chocolate had me...!
Honey Chilli Fries and Cheese Chilli Fries ; These are the Best fries i had till date. It had perfect balance of honey and chilli. Which made it taste perfect. And Cheese chilli fries were yum 😋 Must Try
Liked where place is centrally located so that one can drop by while crossing the Koregaon Park. The only issue is parking which is difficult to hunt. The ambiance and music 🎶is Old school. Special treat for vegetarians as they serve only "VEG". Their food 5/5. The one in pic is "Classic Margarita Pizza". Thin crust with tomatos , chilli sauce and cheese and topped with basil just like other pizza.
"Pink Sauce Pasta" last but not least my favourite. Pasta was damn tasty. The taste of sauce was so perfectly blended and mouth watering.
PS : Due to weak light... read more
Like
1
Comment
0
Share
Vicky Shah
36 Reviews , 64 Followers
Follow
5 months ago
RATED
  A good place to spend your evening with good food. I ordered a pasta Alfredo which was tasty lots of veggies. Also ordered a Tex-Mex Rice which was decent enough in taste. Only problem was the price against the quantity which I felt did not go well but overall its a good place to hang out. Would recommend to have a good pasta in Koregaon Park.
Like
0
Comment
0
Share
Zoya Iqbal
58 Reviews , 64 Followers
Follow
5 months ago
RATED
  Nice place to hangout! Tried the nachos, cheese garlic bread and speedy spaghetti and must say all the dishes were very good.
However the main highlight was the blueberry cheesecake. It was one of the best cheesecakes I've ever eaten!! It was light, fresh and had just the right amount of sweetness.

A must try in Koregaon Park!

Like
3
Comment
0
Share
Nidhi Nair
18 Reviews , 19 Followers
Follow
5 months ago
RATED
  When you have shopped a lot and want something awesome to end your day with, Sautéed stories is the place you should visit. We weren't extremely hungry so, we ordered a Veg lasagne, watermelon cooler and a frappuccino.
The ambience was just perfect with tasty food and mocktails. Loved it and would definitely visit again.
Like
1
Comment
0
Share
Pooja Mehta
67 Reviews , 790 Followers
Follow
5 months ago
RATED
  Budget:1000rs for two
Food:for starters -Honey chilli fries : they where very saucy ,perfect sweet,sour and spicy,loved it .
Burger - Jalpenos potato burger : potato patty with some jalpenos and lots of red sauce , very tasty.
Pizza -Classic cheese pizza:A thin crust with tomato chili sauce and chesse topped with some basil,just like some other pizza .
Dessert : Dark chocolate mouse : A cup of dark choclate topped with some almonds and strwaberry jelly , just perfect .
Ambience : the place is a bit small than expected.Good music was on all the time .The staff was quite polite.Eventhough It was on main street it was bit difficult to find because it had no board.They need to work on their ambience a bit.
Overall a very awesome place.
A must visit if u r looking for something in KP.
Also they gave us a complementary dessert it was a basket with a layer of caramel and chocolate ,one of the tastiest things i had here,i dont remember the name of it though.
Like
4
Comment
0
Share
Aashish
21 Reviews , 407 Followers
Follow
5 months ago
RATED
  A small hangout place with some flashy out of the box decor which may suit better for the night times..!
Definitely not a dining place but a perfect place to seduce the taste buds of Pure vegeterian as the place serves only veg..
long VEGGIE menu with lots of variety but the only thing that let us down were the flies they were too troublesome..
Jalapeno dynamites was smthng worth tasting and even the exotica veg pizza was crunchy with thin crust..chili fries taste didnt meet the expectatns..!
But all in all experience was good would be visiting again to look out for the evng lights..!
Like
0
Comment
0
Share
LOAD MORE 4
SPONSORED & POPULAR
4.2
The Earth Cafe
KOREGAON PARK, PUNE
Hop In for lip-smacking delicacies!Call to book
4.0
Culture - पुणे
FC ROAD, PUNE
Your Favourite Neighbourhood Bar|Book a Table Now
3.8
Penthouze
MUNDHWA, PUNE
Click now to know about our exciting events!
4.3
Elephant & Co.
KALYANI NAGAR, PUNE
Book A Table And Get Amazing Offers On Drinks
3.9
Hakuna Matata
JM ROAD, PUNE
The Best Pizzas On JM Road! Walk-in now!
4.2
Midtown Bar & Lounge
VIMAN NAGAR, PUNE
Pune's favorite pregame bar. Click for happy hours
4.2
1BHK Superbar
BANER, PUNE
Not just a Party Place, But an EXPERIENCE!
3.7
Spice Factory
KHARADI, PUNE
Come dine with us under the stars! Reserve now!
3.7
Addah - The O Hotel
THE O HOTEL, KOREGAON PARK, PUNE
Have a meal in the stars! Book your table.
3.9
Agent Jack's Bar
KOREGAON PARK, PUNE
Amazing Food & Affordable Drinks! Call Now!
3.6
Pashah
KOREGAON PARK, PUNE
Your one stop Mughlai destination in Pune!Call Now
3.6
The Bar Stock Exchange
KOREGAON PARK, PUNE
Most Popular Place Near You!
Nearby restaurants
4.0
The Belgian Waffle Co.
Koregaon Park, Pune
3.5
Street Side Cafe
Koregaon Park, Pune
3.1
Subway
Koregaon Park, Pune
3.9
Sandwich Express
Koregaon Park, Pune
Get the Zomato app
See menus and photos for nearby restaurants and bookmark your favorite places on the go
Text App Link
Get Restaurant Widget
Are you a food blogger?
Add a Zomato spoonback to your blog. ›
Related to Sautéed Stories, Koregaon Park
Restaurants in Pune, Pune Restaurants, Koregaon Park restaurants, Best Koregaon Park restaurants, KP, Kalyani, Sassoon Rd restaurants, Café in Pune, Café near me, Café in Koregaon Park, Casual Dining in Pune, Casual Dining near me, Casual Dining in Koregaon Park, New Year Parties in Pune, Christmas' Special in Pune
Restaurants around Koregaon Park
Bund Garden Road restaurants, Dhole Patil Road restaurants, Kalyani Nagar restaurants, Sassoon Road restaurants
Frequent searches leading to this page
sauteed stories kp, 1, sauteed stories menu, sauteed stories, sautéed stories menu
English
About Zomato
About Us
Culture
Blog
Careers
Contact
For Foodies
Code of Conduct
Community
Verified Users
Blogger Help
Developers
Mobile Apps
For Restaurants
Add a Restaurant
Claim your Listing
Business App
Business Owner Guidelines
Business Blog
Restaurant Widgets
Products for Businesses
Advertise
Order
Book
Trace
Countries
Australia
Brasil
Canada
Chile
Czech Republic
India
Indonesia
Ireland
Italy
Lebanon
Malaysia
New Zealand
Philippines
Poland
Portugal
Qatar
Singapore
Slovakia
South Africa
Sri Lanka
Turkey
UAE
United Kingdom
United States
Privacy Terms API Policy CSR Security Sitemap
By continuing past this page, you agree to our Terms of Service, Cookie Policy, Privacy Policy and Content Policies. All trademarks are properties of their respective owners. © 2008-2018 - Zomato™ Media Pvt Ltd. All rights reserved.
Quick Searches
Delivery
Pocket-Friendly Delivery
Breakfast
Lunch
Dinner
Drinks & Nightlife
Cafés
Chinese
North Indian
Desserts & Bakes
Buffet Places
818
Vegetarian restaurant
'''
