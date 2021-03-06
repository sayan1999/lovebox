from utils import loaddata
import readline
from difflib import get_close_matches
from pandas import DataFrame
from json import loads as load_json
from os import system as sysrun
from random import shuffle
from json.decoder import JSONDecodeError
from env import PLAYLISTFILEPATH

STARTED=False
ISNEWQUEUEADDED=False
COMMANDS=["n", "p", "r", "nr", "scan", "pause", "play", "stop", "exit", "add", "addlist"]

def complete(text, state):
    for cmd in COMMANDS:
        if cmd.startswith(text):
            if not state:
                return cmd
            else:
                state -= 1
def add_one(data, songlist, title):
	global STARTED

	matches=get_close_matches(title, songlist, n=10)
	if not len(matches):
		print("\t\t\t!!Sorry :(  No match for " + title + "!!")
		return
	print(dict(enumerate(matches)))
	index=eval(input("Choose one (Enter 99 to cancel): "))
	try:
		songlocation=data[data['song']==matches[index]]['location'].iloc[0]
		if STARTED:
			sysrun('rhythmbox-client --enqueue \"'+songlocation+"\" &")
			print("----------------Queued  "+matches[index]+"--------------------")
		else:
			sysrun('rhythmbox-client --play-uri=\"'+songlocation+"\" &")
			print("----------------Playing  "+matches[index]+"--------------------")
			STARTED=True
	except IndexError:
		print("Playlist no. out of bound.")


def enqueue(data, songlist, titles):
	shuffle(titles)
	global STARTED
	for title in titles:

		matches=get_close_matches(title, songlist)
		try:
			songlocation=data[data['song']==matches[0]]['location'].iloc[0]
			if STARTED:
				sysrun('rhythmbox-client --enqueue \"'+songlocation+"\" &")
				print("----------------Queued  "+matches[0]+"--------------------")
			else:
				sysrun('rhythmbox-client --play-uri=\"'+songlocation+"\" &")
				print("----------------Playing  "+matches[0]+"--------------------")
				STARTED=True
		except IndexError:
			print("\t\t\t!!No match for " + title + " :(!!")
			continue		

# main
sysrun('rhythmbox-client --clear-queue &')
sysrun('rhythmbox-client --stop')


data=loaddata('./objects/df.obj')
songlist=data['song'].tolist()

with open(PLAYLISTFILEPATH) as music:
	try:
		playlists = load_json(music.read())
	except JSONDecodeError:
		print("could not read file")
		sysrun("sleep 10")

genres=list(playlists.keys())

options=DataFrame({"playlist": genres})

newqueue=playlists.get("newqueue", [])

readline.parse_and_bind("tab: complete")
readline.set_completer(complete)

while(True):
	
	print("-----------------------------------------------------------------------------------------")
	print(str(options) + "\n \n\"n\" to play next\n\"p\" to play prev\n\
\"r\" to repeat\n\"nr\" to stop repeat\n\"scan\" to rescan playlist file\n\"pause\" to pause\n\
\"play\" to play\n\"stop\" to stop rhythmbox and exit\n\"exit\" to exit console\n\
\"add\" to enqueue new song\n\"addlist\" to add songs in newqueue field of playlist file")
	index=input("Enter Here: ")
	

	if(index=="n"):
		sysrun('rhythmbox-client --next')
		continue

	if(index=="p"):
		sysrun('rhythmbox-client --prev')
		continue

	if(index=="r"):
		sysrun('rhythmbox-client --repeat')
		continue

	if(index=="nr"):
		sysrun('rhythmbox-client --no-repeat')
		continue

	if(index=="scan"):
		with open(PLAYLISTFILEPATH) as music:
			try:
				playlists = load_json(music.read())
			except JSONDecodeError:
				print("could not read file")
		continue

	if(index=="pause"):
		sysrun('rhythmbox-client --pause')
		continue

	if(index=="play"):
		sysrun('rhythmbox-client --play')
		continue

	if(index=="stop"):
		sysrun('rhythmbox-client --stop')
		break

	if (index=="exit" or index=="bye"):
		break


	if(index=="add"):
		songname=str(input("Enter song name: "))
		add_one(data, songlist, songname)
		continue

	if(index=="addlist"):
		new_newqueue=playlists.get("newqueue", [])
		for songname in new_newqueue:
			if songname not in newqueue or ISNEWQUEUEADDED==False:
				enqueue(data, songlist, [songname])
		newqueue=playlists.get("newqueue", [])
		ISNEWQUEUEADDED=True
		continue

	
	try:
		genre=genres[int(index)]
		titles=playlists[genre]
		enqueue(data, songlist, titles)
		continue

	except IndexError:
		print("Playlist no. out of bound.")

	except ValueError:
		print("Invalid choice: ", index)