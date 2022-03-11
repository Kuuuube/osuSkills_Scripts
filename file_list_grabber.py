import os
import re
from fnmatch import fnmatch
import hashlib

root = '.'
pattern = "*.osu"

for path, subdirs, files in os.walk(root):
    for name in files:
        if fnmatch(name, pattern):
            with open ("filelist.txt", 'a', encoding="utf8") as filelist:
                path_joined = os.path.join(path, name)
                regex_path = re.sub("^\.","C:\\\o",path_joined)
                regex_path1 = re.sub("^","echo \"",regex_path)
                hasher = hashlib.md5()
                with open (regex_path, 'rb') as hashingfile:
                    buf = hashingfile.read()
                    hasher.update(buf)
                name_regex = re.sub("\.osu","_" + hasher.hexdigest() + ".txt\"",name, flags=re.IGNORECASE)
                name_regex1 = re.sub("^","\"calculations/",name_regex)

                regex_path2 = re.sub("$","\" | osuSkills.exe > " + name_regex1,regex_path1)
                filelist.write (regex_path2)
                filelist.write ("\n")
