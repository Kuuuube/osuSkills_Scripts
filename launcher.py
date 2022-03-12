import re
import hashlib
import os

with open ("filelist.txt", "r", encoding="UTF-8") as filelistRaw:
        filelistLines = filelistRaw.readlines()
        filelist = list(map(str.strip, filelistLines))

        for element in filelist:
            try:
                command = element
                pipe = re.search("(?<=\> \").*?(?=\")", element)
                osuhash = re.search("\w{32}(?=\.txt\"$)", element)

                os.system(command)

                pipedata = ""

                with open (pipe.group(0), 'a', encoding="UTF-8") as pipefile2:
                    pipefile2.write(osuhash.group(0) + "\n")

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
