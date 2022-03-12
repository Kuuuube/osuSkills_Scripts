# osuSkills Scripts

Jank scripts for automated calculation of osuSkills stats on maps.

## Downloads

Downloads with prebuilt binaries are in [Releases](https://github.com/Kuuuube/osuSkills_Scripts/releases)

Pre-done calculations for NM, DT, and HR done on my songs folder (170k maps) are available in [Releases](https://github.com/Kuuuube/osuSkills_Scripts/releases).

## Usage

See: [notes](https://github.com/Kuuuube/osuSkills_Scripts/blob/main/notes.md) for usage explanations.

## Dependencies

Python 3: https://www.python.org/downloads/

.Net Runtime 6.0 x64: https://dotnet.microsoft.com/en-us/download/dotnet/6.0

## Manual building and setup instructions:

Required file Structure:
```
Main Folder
├───osuSkills.exe 
├───file_list_grabber.py
├───launcher.py
├───parser.py
└───CollectionCSVtoDB
    └───CollectionCSVtoDB.exe
```

osuSkills.exe is built from a fork of the [osuSkills Console App Branch](https://github.com/Kuuuube/osuSkills/tree/console_app) using:
```
g++ -std=c++11 *.cpp -O2 -o osuSkills.exe
```

CollectionCSVtoDB is built from [osu! CollectionCSVtoDB](https://github.com/Kuuuube/osu_CollectionCSVtoDB) using:
```
$options= @('--configuration', 'Release', '-p:PublishSingleFile=true', '-p:DebugType=embedded', '--self-contained', 'false')
dotnet publish CollectionCSVtoDB $options --runtime win-x64 --framework net6.0 -o build/win-x64
```