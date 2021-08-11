import PySimpleGUI as sg
from urllib.request import urlopen
from bs4 import BeautifulSoup
import time
import threading

sg.theme('dark grey 1') # color theme
def nis(): # New israeli shakel 
    ils="*"
    ils+="3.34"
    url1="https://www.globes.co.il/portal/instrument.aspx?instrumentid=10463"
    html1=urlopen(url1)
    soup1 = BeautifulSoup(html1,"html.parser")
    x=soup1.find("div",id="divCurrencyRate")
    x=x.find("div")
    return (x.get_text())

def find(name): # find(coin)
    ils="*"
    copyNis=nis() # str() > copy nis
    ils+=copyNis
    name=name.lower() # 
    name=name.replace(" ","-")
    url="https://coinmarketcap.com/all/views/all/"
    html=urlopen(url)
    soup = BeautifulSoup(html,"html.parser")
    name_stack="/currencies/"
    name_stack+=name
    name_stack+="/markets/" # name_stack= "/currencies/bitcoin/markets"
    a=soup.find(href=name_stack)
    if a:
        usd=a.get_text().replace("$"," ")
        usd=a.get_text().replace(",","")
        usd=usd.replace("$","")
        usd+=ils
        newIls=eval(usd)
        return (name +":  "+ str(a.get_text())+" , "+str(newIls)+"₪")
    else:
        return ("There is no Coin " + name + "\n")
    
    
# ____  ____  ____ Define the window's contents ____  ____  ____
choices =["NANO","Bitcoin"]
layout = [[sg.Text("Enter Coin Name:",font='Any 12')],
          [sg.Input(key='-INPUT-')], 
          [sg.Button('Bitcoin'), sg.Button('Litecoin'), sg.Button('XRP'), sg.Button('TRON'),
          ],
           [sg.Button('Zcash'), sg.Button('Celsius'), sg.Button('Stacks'), sg.Button('Tether'),sg.Button('Flow')
          ],
          [ sg.Button('Dent'), sg.Button('Ravencoin'), sg.Button('Uniswap'),sg.Button('Ethereum'),
           ],
          [ sg.Button('Helium'), sg.Button('Bitcoin Cash'),sg.Button('Dogecoin'), sg.Button('Neo'), sg.Button('ICON')
          ],
          [sg.Text(size=(40,1), key='-OUTPUT-',font='Any 12')],
          [sg.Button("₪",font='Any 12'),sg.Text(size=(40,1),font='Any 12', key='-nis-')],
          [sg.Button('Ok',font='Any 12'), sg.Button('Quit',font='Any 12')]]

#  ____  ____  ____ Create the window  ____  ____  ____

window = sg.Window('Coin market Script - By BEN N0I0FF', layout)

# Display and interact with the Window using an Event Loop  ____  ____  ____
while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    # Output a message to the window

        
    if event=="₪":
         window['-nis-'].update("1$ = "+nis()+"₪")
         
    elif event=="Ok":
         values['-INPUT-'] = find(values['-INPUT-'])
         time.sleep(5)
         window['-OUTPUT-'].update("" + values['-INPUT-'] + "")
    else:
        values['-INPUT-']=event
        name=values['-INPUT-']
        window['-OUTPUT-'].update(name+"!!")
        values['-INPUT-'] = find(values['-INPUT-'])
        time.sleep(5)
        window['-OUTPUT-'].update("" + values['-INPUT-'] + "")
# ____  ____  ____ Finish up by removing from the screen  ____  ____  ____
window.close() # event close()!

