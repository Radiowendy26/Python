import twitter
import datetime
import sqlite3
import shutil
import time
LastSite = ""
LastSite2 = ""

while True:

    file = open("TwitterCredentials.txt")
    creds = file.read().split('\n')

    api = twitter.Api(creds[0],creds[1],creds[2],creds[3])

    shutil.copyfile("C:\Users\wendy_2\AppData\Local\Google\Chrome\User Data\Default\History", "History")

    History = "History"

    console = sqlite3.connect("History")
    cursor = console.cursor()

    cursor.execute("SELECT * FROM urls")

    rows = cursor.fetchall()

    for row in rows:
        var = row[2]

    var2 = var.split('\n')  

    LastSite = var2[-1]

    if LastSite != LastSite2 :
        response = api.PostUpdate("I'm really liking " + LastSite) 
        LastSite2 = LastSite
        print("Status updated to: " + response.text)
    else :
        print "No change"

    time.sleep(3600)
    console.close()

