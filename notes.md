## file_list_grabber.py 
(generates the filelist.txt)
1. Put this in songs folder and run it

    You will likely need to edit line 14: `regex_path = re.sub("^\.","C:\\\o",path_joined)` and change `C:\\\o` to whatever the path to your songs folder is.

    eg: from `regex_path = re.sub("^\.","C:\\\o",path_joined)` to `regex_path = re.sub("^\.","C:\\Users\\username\\AppData\\Local\\osu!\\Songs",path_joined)`

    If you run into issues with "bad escaping" or regex errors you likely need to change the slashes or add more slashes.

2. Take generated filelist.txt and move it to this folder
3. (Optional) Use regex to add a mod. Replace: `(?= |)` with the desired mod. Only single mods are supported and make sure to have a + infront of the mod. For example: +HD not HD.

## launcher.py 
(runs filelist.txt maps through osuSkills.exe)
1. Have filelist.txt, osuSkills.exe, and calculations folder in the same directory then run it.

    This is extremely slow and jank. It runs at about 500 maps per minute. 

    osuSkills.exe also has a very low chance of getting hung on some maps. If this happens you will see osuSkills.exe taking a very high amount of cpu and just sitting there. You can end the task in task manager and that map will be skipped.

## parser.py 
(parses the output of launcher.py after some minor manual fixing)

Fixing launcher.py output: (I was too lazy to automate this with another script)
1. Take the output of launcher.py in the calculations folder and run in cmd (for windows) `copy *.txt temp`
2. Take temp and copy all matches of the following regex: `Stamina: .*?\)`
3. Paste the copied matches into a file named osuskills_calculations_full.txt (make sure each match is pasted to a new line)

Using parser.py:
1. Run parser.py
2. Go through the cli
3. The output collection will be in a folder in the parsed_files folder