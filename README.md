# osuSkills Scripts

Jank scripts for automated calculation of osuSkills stats on maps.

## General use

Downloads with prebuilt binaries are in [Releases](https://github.com/Kuuuube/osuSkills_Scripts/releases)

See: [notes](https://github.com/Kuuuube/osuSkills_Scripts/blob/main/notes.md) for explanations on how the scripts should be used.

I have included calculations for NM, DT, and HR done on my songs folder into the [Releases](https://github.com/Kuuuube/osuSkills_Scripts/releases).

<br>

## Manual building and setup instructions:

Required file Structure:
```
Main Folder
├───osuSkills.exe 
├───file_list_grabber.py
├───launcher.py
├───parser.py
└───CollectionCSVtoDB
    ├───CollectionCSVtoDB.dll
    ├───CollectionCSVtoDB.exe
    └───CollectionCSVtoDB.runtimeconfig.json
```

osuSkills.exe is built from a fork of the [osuSkills Console App Branch](https://github.com/Kuuuube/osuSkills/tree/console_app) using:
```
g++ -std=c++11 *.cpp -O2 -o osuSkills.exe
```

CollectionCSVtoDB must be built to an executable as well.