![Lovebox](src/examples/lovebox.png?raw=true "Lovebox")

# Lovebox (music-player utils)
A wrapper easy-to-use for playlist queueing over rhythmbox in linux based system.
A music-player utils. Add songs of different genre in config file and play a genre in rhythmbox very easily.

![Preview](src/examples/preview.png?raw=true "Preview of Lovebox")

# Why lovebox?
## Features:
1. Closest match method: It has a closest match method to find the nearest song (if not sure about the spelling of song), so if you know the song put it in the config file (lovebox.json) and run it. No need to find the title folder name of the actual file in your local disk.

2. Crash handling: If no match found for a title, the app doesn't crash. It continues after a log report.

3. Wide utils:
Not only queuing custom playlist but Lovebox brings you many other features:

```
           playlist
0    rhythmic-hindi
1    hindi-romantic
2  rhythmic-english
3      Taylor Swift
4          newqueue
 
"n" to play next
"p" to play prev
"r" to repeat
"nr" to stop repeat
"scan" to rescan playlist file
"pause" to pause
"play" to play
"stop" to stop rhythmbox and exit
"exit" to exit console
"add" to enqueue new song
"addlist" to add songs in newqueue field of playlist file
```

## Dependencies
Rhythmbox, Python3 and import modules

bash```
sudo apt install python3.8 python3-pip
pip3 install modulename
```

## Configuration
1. Navigate into lovebox/src/. Run 
bash```
chmod +x lovebox
./lovebox
```
## If app doesn't start ethier your rhythmbox db file location is different or your playlist file is missing. (Follow these instructions to fix it)
2. There is an example json file as lovebox/src/lovebox.json which will act as your actual playlist file in a json format. The entire file is a key-value pairs of generes as key and array of corresponding song names as value of that key. Edit and add the song names to your choice.
3. Find out your rhythmbox xml db filepath (usually <~/.local/share/rhythmbox/rhythmdb.xml>); open lovebox/src/env.py file in editing mode and edit the 2nd line as RHYTHMBOXXMLPATH=<Rhythmbox_xml_db_filepath_string_within_quotes>.
4. Run lovebox and do as the console says. Resolve the modulenotfound error by running
bash```
pip3 install <modulename>
```
5. (Optional) add <path to lovebox/src> to your PATH variable and use this command from any directory. You can also write a desktop file (as given in the examples folder, first add src directory to your path)and put it in your home/applications folder to have a full fledged application use. 