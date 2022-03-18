### If you want to use the pre-done calculations, skip to "Using parser.py:" in [parser.py](https://github.com/Kuuuube/osuSkills_Scripts/blob/main/notes.md#parserpy).

<br>

# file_list_grabber.py 
(generates the filelist.txt)
1. Put this in songs folder and run it

    You will likely need to edit line 14: `regex_path = re.sub("^\.","C:\\\o",path_joined)` and change `C:\\\o` to whatever the path to your songs folder is.

    eg: from `regex_path = re.sub("^\.","C:\\\o",path_joined)` to `regex_path = re.sub("^\.","C:\\Users\\username\\AppData\\Local\\osu!\\Songs",path_joined)`

    If you run into issues with "bad escaping" or regex errors you likely need to change the slashes or add more slashes.

2. Take generated filelist.txt and move it to this folder
3. (Optional) Use regex to add a mod. Replace: `(?= |)` with the desired mod. Mods should be separated by a space. For example: `HD DT`.

# launcher.py 
(runs filelist.txt maps through osuSkills.exe)
1. Have filelist.txt, osuSkills.exe, and calculations folder in the same directory then run it.

    This is extremely slow and jank. It runs at about 500 maps per minute. 

    osuSkills.exe also has a very low chance of getting hung on some maps. If this happens you will see osuSkills.exe taking a very high amount of cpu and just sitting there. You can end the task in task manager and that map will be skipped.

# parser.py 
(parses the output of launcher.py after some minor manual fixing)

### Fixing launcher.py output: 

(an automated script to do this will probably be made eventually).

1. Take the output of launcher.py in the calculations folder and run in cmd (for windows) `copy *.txt temp`.
2. (Optional) It is recommended to take temp and copy all matches of the following regex: `Stamina: .*`. This will remove invalid map calculations which should speed up and cut down on errors in `parser.py`.
3. (Optional) Paste the copied matches into a new file (make sure each match is separated by a new line).
4. Name the file `osuskills_calculations_full.txt` and put it in the same directory as `parser.py`.

### Using parser.py:

(If you're using the pre-done calculations, first, extract the `osuskills_calculations_full.txt` and put it in the same directory as `parser.py`.)

1. Run parser.py.
2. Go through the cli.
3. The output collection will be in a folder in the `parsed_files` folder.

Note: When adding large amounts of filters the collection names can get too long for osu! to recognize. Changing the name of the MD5 list to something shorter and running it through CollectionCSVtoDB manually can fix this.