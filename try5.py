import sys
import time
import telepot
import requests
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
from bs4 import BeautifulSoup
import urllib.request as ur


link = '' #global variable link defined to store different website links
cartype ='default'
count1 =0 #a global counter to control greeting 
carinfo = ['default', '0km', '0 years']
infolist = ['family','ford'] #a global list to store user selection information

# A function print out the car result listaccording to the user's selection
def resultpage(chat_id, infolist):
    # if loop to jump to different webpages
    if ("toyota" in infolist and "SUV" in infolist):
        link = "http://www.sgcarmart.com/used_cars/listing.php?ASL=1&MOD=toyota&PR1=0&PR2=&RGD=0&DP1=0&DP2=&CAT=&VEH=9"
    if ("toyota" in infolist and "MPV" in infolist):
        link = "http://www.stcars.sg/singapore-car/used-cars/search/toyota-keyword/mpv-type-10?originalKeywords=toyota"
    if ("toyota" in infolist and "sport" in infolist):
        link = "http://www.sgcarmart.com/used_cars/listing.php?ASL=1&MOD=toyota&PR1=0&PR2=&RGD=0&DP1=0&DP2=&CAT=&VEH=8"
    if ("toyota" in infolist and "hatchback" in infolist):
        link = "http://www.stcars.sg/singapore-car/used-cars/search/toyota-keyword/hatchback-type-11?originalKeywords=toyota"
    if ("nissan" in infolist and "SUV" in infolist):
        link = "http://www.sgcarmart.com/used_cars/listing.php?ASL=1&MOD=nissan&PR1=0&PR2=&RGD=0&DP1=0&DP2=&CAT=&VEH=9"
    if ("nissan" in infolist and "MPV" in infolist):
        link = "http://www.stcars.sg/singapore-car/used-cars/search/nissan-keyword/mpv-type-10?originalKeywords=nissan"
    if ("nissan" in infolist and "sport" in infolist):
        link = "http://www.stcars.sg/singapore-car/used-cars/search/nissan-keyword/sports-car-type-8?originalKeywords=nissan"
    if ("nissan" in infolist and "hatchback" in infolist):
        link = "http://www.stcars.sg/singapore-car/used-cars/search/nissan-keyword/hatchback-type-11?originalKeywords=nissan"
    if ("honda" in infolist and "SUV" in infolist):
        link = "http://www.sgcarmart.com/used_cars/listing.php?ASL=1&MOD=honda&PR1=0&PR2=&RGD=0&DP1=0&DP2=&CAT=&VEH=9"
    if ("honda" in infolist and "MPV" in infolist):
        link = "http://www.stcars.sg/singapore-car/used-cars/search/honda-keyword/mpv-type-10?originalKeywords=honda"
    if ("honda" in infolist and "sport" in infolist):
        link = "http://www.stcars.sg/singapore-car/used-cars/search/honda-keyword/sports-car-type-8?originalKeywords=honda"
    if ("honda" in infolist and "hatchback" in infolist):
        link = "http://www.stcars.sg/singapore-car/used-cars/search/honda-keyword/hatchback-type-11?originalKeywords=honda"
    if ("mitsubishi" in infolist and "SUV" in infolist):
        link = "http://www.sgcarmart.com/used_cars/listing.php?ASL=1&MOD=Mitsubishi&PR1=0&PR2=&RGD=0&DP1=0&DP2=&CAT=&VEH=9"
    if ("mitsubishi" in infolist and "MPV" in infolist):
        link = "http://www.stcars.sg/singapore-car/used-cars/search/mitsubishi-keyword/mpv-type-10?originalKeywords=mitsubishi"
    if ("mitsubishi" in infolist and "sport" in infolist):
        link = "http://www.stcars.sg/singapore-car/used-cars/search/mitsubishi-keyword/sports-car-type-8?originalKeywords=mitsubishi"
    if ("mitsubishi" in infolist and "hatchback" in infolist):
        link = "http://www.stcars.sg/singapore-car/used-cars/search/mitsubishi-keyword/hatchback-type-11?originalKeywords=mitsubishi"

    # parse basic information containing car name and type from the corresponding webpages
    r = requests.get(link)
    soup = BeautifulSoup(r.content,"html.parser")
    for i in soup.find_all("div", {'id':'content'}):
        for j in soup.find_all('div', {'id':'car_listing'}):
            for k in soup.find_all('div', {'class':'fl'}):
                ktext=k.text
                bot.sendMessage(chat_id, ktext) #send the result
                    
    r = requests.get(link)
    soup = BeautifulSoup(r.content,"html.parser")
    for div in soup.find_all('div', {'id':'contentblank'}):
        for p in div.find_all("strong"):
            ptext=p.text
            bot.sendMessage(chat_id, ptext) #send the result
            
#A function to parse car price information
def price(chat_id, infolist):
    if ("toyota" in infolist and "SUV" in infolist):
        link = "http://www.sgcarmart.com/used_cars/listing.php?ASL=1&MOD=toyota&PR1=0&PR2=&RGD=0&DP1=0&DP2=&CAT=&VEH=9"
    if ("toyota" in infolist and "MPV" in infolist):
        link = "http://www.stcars.sg/singapore-car/used-cars/search/toyota-keyword/mpv-type-10?originalKeywords=toyota"
    if ("toyota" in infolist and "sport" in infolist):
        link = "http://www.sgcarmart.com/used_cars/listing.php?ASL=1&MOD=toyota&PR1=0&PR2=&RGD=0&DP1=0&DP2=&CAT=&VEH=8"
    if ("toyota" in infolist and "hatchback" in infolist):
        link = "http://www.stcars.sg/singapore-car/used-cars/search/toyota-keyword/hatchback-type-11?originalKeywords=toyota"
    if ("nissan" in infolist and "SUV" in infolist):
        link = "http://www.sgcarmart.com/used_cars/listing.php?ASL=1&MOD=nissan&PR1=0&PR2=&RGD=0&DP1=0&DP2=&CAT=&VEH=9"
    if ("nissan" in infolist and "MPV" in infolist):
        link = "http://www.stcars.sg/singapore-car/used-cars/search/nissan-keyword/mpv-type-10?originalKeywords=nissan"
    if ("nissan" in infolist and "sport" in infolist):
        link = "http://www.stcars.sg/singapore-car/used-cars/search/nissan-keyword/sports-car-type-8?originalKeywords=nissan"
    if ("nissan" in infolist and "hatchback" in infolist):
        link = "http://www.stcars.sg/singapore-car/used-cars/search/nissan-keyword/hatchback-type-11?originalKeywords=nissan"
    if ("honda" in infolist and "SUV" in infolist):
        link = "http://www.sgcarmart.com/used_cars/listing.php?ASL=1&MOD=honda&PR1=0&PR2=&RGD=0&DP1=0&DP2=&CAT=&VEH=9"
    if ("honda" in infolist and "MPV" in infolist):
        link = "http://www.stcars.sg/singapore-car/used-cars/search/honda-keyword/mpv-type-10?originalKeywords=honda"
    if ("honda" in infolist and "sport" in infolist):
        link = "http://www.stcars.sg/singapore-car/used-cars/search/honda-keyword/sports-car-type-8?originalKeywords=honda"
    if ("honda" in infolist and "hatchback" in infolist):
        link = "http://www.stcars.sg/singapore-car/used-cars/search/honda-keyword/hatchback-type-11?originalKeywords=honda"
    if ("mitsubishi" in infolist and "SUV" in infolist):
        link = "http://www.sgcarmart.com/used_cars/listing.php?ASL=1&MOD=Mitsubishi&PR1=0&PR2=&RGD=0&DP1=0&DP2=&CAT=&VEH=9"
    if ("mitsubishi" in infolist and "MPV" in infolist):
        link = "http://www.stcars.sg/singapore-car/used-cars/search/mitsubishi-keyword/mpv-type-10?originalKeywords=mitsubishi"
    if ("mitsubishi" in infolist and "sport" in infolist):
        link = "http://www.stcars.sg/singapore-car/used-cars/search/mitsubishi-keyword/sports-car-type-8?originalKeywords=mitsubishi"
    if ("mitsubishi" in infolist and "hatchback" in infolist):
        link = "http://www.stcars.sg/singapore-car/used-cars/search/mitsubishi-keyword/hatchback-type-11?originalKeywords=mitsubishi"

    #find and print out the price information
    r = requests.get(link)
    soup = BeautifulSoup(r.content,"html.parser")
    for i in soup.find_all("div", {'id':'content'}):
        for j in soup.find_all('div', {'id':'car_listing'}):
            for k in soup.find_all('th', {'width':'115'}):
                ktext=k.text
                bot.sendMessage(chat_id, ktext)

#Updating user selection information (car type)
def updateCarInformation01(infolist):
    infolist[0]='sport'
    print(infolist)

def updateCarInformation02(infolist):
    infolist[0]='SUV'
    print(infolist)

def updateCarInformation03(infolist):
    infolist[0]='MPV'
    print(infolist)

def updateCarInformation04(infolist):
    infolist[0]='hatchback'
    print(infolist)

# the main handle loop    
def handle(msg):
    global count1, cartype
    count1 +=1
    content_type, chat_type, chat_id = telepot.glance(msg) #get the user message
    print(content_type, chat_type, chat_id) #print out user input type

    #Only greet the user when meet for the first time
    if count1==1:
        bot.sendMessage(chat_id, 'Hello, I am a bot serving you with used car information. Input "Yes" to continue, and "No" to quit')
        
    s = msg['text']
    s = s.lower() #converting user input to lowercase
    
    Decision(chat_id,msg)

    #detect the keywords entered by user
    if s.find("sports")!=-1:
        updateCarInformation01(infolist) #call function to update user car type selection information
        cartype = select(chat_id)
        bot.sendMessage(chat_id, "Current selection information:")
        bot.sendMessage(chat_id, "Current car type:"+ cartype)
        bot.sendMessage(chat_id, 'Please input the brand name') #prompt user to enter car brand name
        return cartype

    if s.find("suv")!=-1:
        updateCarInformation02(infolist)
        cartype = 'SUV'
        bot.sendMessage(chat_id, "Current car type:"+ cartype)
        bot.sendMessage(chat_id, 'Please input the brand name')
        return cartype

    if s.find("mpv")!=-1:
        updateCarInformation03(infolist)
        cartype = 'mpv'
        bot.sendMessage(chat_id, "Current car type:"+ cartype)
        bot.sendMessage(chat_id, 'Please input the brand name')
        return cartype

    if s.find("hatchback")!=-1:
        updateCarInformation04(infolist)
        cartype = 'hatchback'
        bot.sendMessage(chat_id, "Current car type:"+ cartype)
        bot.sendMessage(chat_id, 'Please input the brand name')
        return cartype
    
    if s.find("mitsubishi")!=-1:
        infolist[1]="mitsubishi" #call function to update user car brand selection information
        print(infolist)
        selection = str(infolist)
        bot.sendMessage(chat_id, "Current selection:"+ selection)
        bot.sendMessage(chat_id, "type 'print' to see the result and 'price' to see the prices") #prompt user how to get the result list and price information
        
    if s.find("nissan")!=-1:
        infolist[1]="nissan"
        print(infolist)
        selection = str(infolist)
        bot.sendMessage(chat_id, "Current selection:"+ selection)
        bot.sendMessage(chat_id, "type 'print' to see the result and 'price' to see the prices")

    if s.find("honda")!=-1:
        infolist[1]="honda"
        print(infolist)
        selection = str(infolist)
        bot.sendMessage(chat_id, "Current selection:"+ selection)
        bot.sendMessage(chat_id, "type 'print' to see the result and 'price' to see the prices")
        
    if s.find("toyota")!=-1:
        infolist[1]="toyota"
        print(infolist)
        selection = str(infolist)
        bot.sendMessage(chat_id, "Current selection:"+ selection)
        bot.sendMessage(chat_id, "type 'print' to see the result and 'price' to see the prices")

    #call function to search car information
    if s.find("print")!=-1:
        resultpage(chat_id, infolist)

    #call function to search car price information
    if s.find("price")!=-1:
        price(chat_id, infolist)

        
def Decision(chat_id,msg):
    s = msg['text']
    s=s.lower()
    if s.find("yes")!=-1 or s.find("Yes")!=-1:
        bot.sendMessage(chat_id, "Excellent! Key in the car type ('sports', 'SUV', 'MPV', or 'hatchback' ) you want to search about")
    if s.find("no")!=-1 or s.find("No")!=-1:
        bot.sendMessage(chat_id, "Okay, you don't like me")

def select(chat_id):
    return 'sport'


bot = telepot.Bot('376716354:AAF0NHj23anC1aT8owrVTBMBnMmOp-oD6KE') #identify the bot with token
bot.message_loop(handle) #run the main handle loop
print ('Listening ...')

while 1:
 time.sleep(10)
 
