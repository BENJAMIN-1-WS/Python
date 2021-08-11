from urllib.request import urlopen
from bs4 import BeautifulSoup

url="https://www.livegames.co.il/broadcastspage.aspx"     #link
html=urlopen(url)
soup = BeautifulSoup(html,"html.parser")
channel=soup.findAll("td",{"class":"broadcastTd broadcastRCol textalign td2"})     
time=soup.findAll("td",{"class":"broadcastTd broadcastRCol td3"})     
team=soup.findAll("td",{"class":"broadcastTd broadcastLcols td4"})
day=soup.findAll("li",{"class":"MenuOfDates"})

print(len(day))
j=0
print(len(team))
print(len(channel))
x=len(channel)
print(day[j].text)
for i in range(x-1):
    print("ערוץ: \t"+channel[i].text) 
    print("משחק: \t"+team[i].text)
    print("שעה: \t"+time[i].text)
    if time[i].text>time[i+1].text:
        print("\n\t_________________________________"+
              "_________________________________\n")
        j=j+1
        print("תאריך: "+day[j].text)
