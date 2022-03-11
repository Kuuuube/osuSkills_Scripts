import re
import hashlib
import os

with open ("filelist.txt", "r", encoding="UTF-8") as filelistRaw:
        filelistLines = filelistRaw.readlines()
        filelist = list(map(str.strip, filelistLines))

        for element in filelist:
            try:
                command = element
                #path = re.search(".*(?=<\|\|>)", element)
                pipe = re.search("(?<=\> \").*?(?=\")", element)
                osuhash = re.search("\w{32}(?=\.txt\"$)", element)
                mod_regex = re.search("\w+(?= \|)", element)
                if mod_regex is not None:
                    mod_formatted = re.sub("^", "Mod: ", mod_regex.group(0))
                else:
                    mod_formatted = "Mod: NM"

                os.system(command)
                #hasher = hashlib.md5()
                #with open (path.group(0), 'rb') as hashingfile:
                #    buf = hashingfile.read()
                #    hasher.update(buf)

                pipedata = ""
                    
                with open (pipe.group(0), 'r', encoding="UTF-8") as pipefile:
                    strip_lines = re.sub("(\n|\r)", " ", pipefile.read())
                    strip_trash = re.search("Stamina.*?Memory: \d+",strip_lines)
                    if strip_trash is not None:
                        pipedata = strip_trash.group(0)
                    else:
                        pipedata = "Invalid map"

                with open (pipe.group(0), 'w', encoding="UTF-8") as pipefile2:
                    pipefile2.write(pipedata)
                    pipefile2.write(", " + mod_formatted)
                    pipefile2.write(", MD5 (" + osuhash.group(0) + ")")

                with open ("log.txt", "a", encoding='utf8') as log_file:
                    log_file.write(str(element))
                    log_file.write("\n")
                            
            except Exception as e:
                try:
                    with open ("log.txt", "a", encoding='utf8') as log_file:
                        log_file.write(str(element) + " Failed")
                        log_file.write("\n")
                    with open ("error_log.txt", "a", encoding='utf8') as error_log:
                        error_log.write(str(element) + "\n" + str(e) + " Failed")
                        error_log.write("\n")
                    print(str(e))
                    pass
                
                except Exception as e:
                    with open ("error_log.txt", "a", encoding='utf8') as error_log:
                        error_log.write(str(e))
                        error_log.write("\n")
