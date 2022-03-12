import re
import os
import subprocess

filter_setting = input("Enter the numbers for all the filters you want. eg: \"12\" to filter Stamina and Tenacity:\n1. Stamina\n2. Tenacity\n3. Agility\n4. Accuracy\n5. Precision\n6. Reaction\n7. Memory\n: ")
filename = ""

if re.search("1", filter_setting) is not None:
    Stamina_min = input("Enter minimum Stamina value: ")
    Stamina_max = input("Enter maximum Stamina value: ")
    filename = filename + "_Stamina_" + str(Stamina_min) + "-" + str(Stamina_max)
    
if re.search("2", filter_setting) is not None:
    Tenacity_min = input("Enter minimum Tenacity value: ")
    Tenacity_max = input("Enter maximum Tenacity value: ")
    filename = filename + "_Tenacity_" + str(Tenacity_min) + "-" + str(Tenacity_max)
                
if re.search("3", filter_setting) is not None:
    Agility_min = input("Enter minimum Agility value: ")
    Agility_max = input("Enter maximum Agility value: ")
    filename = filename + "_Agility_" + str(Agility_min) + "-" + str(Agility_max)
    
if re.search("4", filter_setting) is not None:
    Accuracy_min = input("Enter minimum Accuracy value: ")
    Accuracy_max = input("Enter maximum Accuracy value: ")
    filename = filename + "_Accuracy_" + str(Accuracy_min) + "-" + str(Accuracy_max)
    
if re.search("5", filter_setting) is not None:
    Precision_min = input("Enter minimum Precision value: ")
    Precision_max = input("Enter maximum Precision value: ")
    filename = filename + "_Precision_" + str(Precision_min) + "-" + str(Precision_max)
    
if re.search("6", filter_setting) is not None:
    Reaction_min = input("Enter minimum Reaction value: ")
    Reaction_max = input("Enter maximum Reaction value: ")
    filename = filename + "_Reaction_" + str(Reaction_min) + "-" + str(Reaction_max)
    
if re.search("7", filter_setting) is not None:
    Memory_min = input("Enter minimum Memory value: ")
    Memory_max = input("Enter maximum Memory value: ")
    filename = filename + "_Memory_" + str(Memory_min) + "-" + str(Memory_max)

filename_stripped = re.sub("^_","",filename)
foldername1 = "parsed_files"
foldername2 =  filename_stripped
foldername = foldername1 + "\\" + foldername2

if os.path.isdir(foldername1) is not True:
    os.mkdir(foldername1)
if os.path.isdir(foldername1 + "\\" + foldername2) is not True:
    os.mkdir(foldername1 + "\\" + foldername2)
file_list = os.listdir(foldername)
for element in file_list:
    dbsearch = re.search("\.db", element)
    if dbsearch is None:
        try:
            with open (foldername + "\\" + element, 'w') as wipe_file:
                pass
        except Exception as e:
            print(e)
            pass

    
with open ("osuskills_calculations_full.txt", "r", encoding="UTF-8") as osuskills_calculationsRaw:
        osuskills_calculationsLines = osuskills_calculationsRaw.readlines()
        osuskills_calculations = list(map(str.strip, osuskills_calculationsLines))

        for element in osuskills_calculations:
            filter_check = 0
            filename = ""
            
            mod = re.search("(?<=Mod: )(\w| )+", element)
            if mod is not None:
                filename_stripped_mod = filename_stripped + "_" + mod.group(0)
            else:
                filename_stripped_mod = filename_stripped + "_Invalid_mod"

            if re.search("1", filter_setting) is not None:
                Stamina_number = re.search("(?<=Stamina: )(\d|\.)+",element)

                if Stamina_number is not None:
                    if float(Stamina_number.group(0)) >= float(Stamina_min) and float(Stamina_number.group(0)) <= float(Stamina_max):
                        filter_check = filter_check + 1
                    else:
                        filter_check = filter_check + 10
                else:
                    filter_check = filter_check + 100
                
            if re.search("2", filter_setting) is not None:
                Tenacity_number = re.search("(?<=Tenacity: )(\d|\.)+",element)

                if Tenacity_number is not None:
                    if float(Tenacity_number.group(0)) >= float(Tenacity_min) and float(Tenacity_number.group(0)) <= float(Tenacity_max):
                        filter_check = filter_check + 1
                    else:
                        filter_check = filter_check + 10
                else:
                    filter_check = filter_check + 100
                
            if re.search("3", filter_setting) is not None:
                Agility_number = re.search("(?<=Agility: )(\d|\.)+",element)
                
                if Agility_number is not None:
                    if float(Agility_number.group(0)) >= float(Agility_min) and float(Agility_number.group(0)) <= float(Agility_max):
                        filter_check = filter_check + 1
                    else:
                        filter_check = filter_check + 10
                else:
                    filter_check = filter_check + 100
                
            if re.search("4", filter_setting) is not None:
                Accuracy_number = re.search("(?<=Accuracy: )(\d|\.)+",element)
                
                if Accuracy_number is not None:
                    if float(Accuracy_number.group(0)) >= float(Accuracy_min) and float(Accuracy_number.group(0)) <= float(Accuracy_max):
                        filter_check = filter_check + 1
                    else:
                        filter_check = filter_check + 10
                else:
                    filter_check = filter_check + 100
                
            if re.search("5", filter_setting) is not None:
                Precision_number = re.search("(?<=Precision: )(\d|\.)+",element)
                
                if Precision_number is not None:
                    if float(Precision_number.group(0)) >= float(Precision_min) and float(Precision_number.group(0)) <= float(Precision_max):
                        filter_check = filter_check + 1
                    else:
                        filter_check = filter_check + 10
                else:
                    filter_check = filter_check + 100
                
            if re.search("6", filter_setting) is not None:
                Reaction_number = re.search("(?<=Reaction: )(\d|\.)+",element)
                                
                if Reaction_number is not None:
                    if float(Reaction_number.group(0)) >= float(Reaction_min) and float(Reaction_number.group(0)) <= float(Reaction_max):
                        filter_check = filter_check + 1
                    else:
                        filter_check = filter_check + 10
                else:
                    filter_check = filter_check + 100
                
            if re.search("7", filter_setting) is not None:
                Memory_number = re.search("(?<=Memory: )(\d|\.)+",element)
                
                if Memory_number is not None:
                    if float(Memory_number.group(0)) >= float(Memory_min) and float(Memory_number.group(0)) <= float(Memory_max):
                        filter_check = filter_check + 1
                    else:
                        filter_check = filter_check + 10
                else:
                    filter_check = filter_check + 100

            if filter_check >= 10:
                pass
            else:
                if os.path.isdir(foldername1) is not True:
                    os.mkdir(foldername1)
                    
                if os.path.isdir(foldername1 + "\\" + foldername2) is not True:
                    os.mkdir(foldername1 + "\\" + foldername2)

                with open (str(foldername) + "\\" + str(filename_stripped_mod), 'a') as md5_file:
                    md5_regex = re.search("\w{32}",element)
                    md5_file.write(",," + md5_regex.group(0))
                    md5_file.write("\n")

file_list = os.listdir(foldername)
for element in file_list:
    dbsearch = re.search("\.db", element)
    if dbsearch is None:
        try:
            subprocess.check_call([r"CollectionCSVtoDB\CollectionCSVtoDB.exe", foldername + "\\" + element, foldername + "\\" + element + ".db"])
            print("Collection " + element + ".db Generated!")
        except Exception as e:
            print(e)
            pass
    else:
        pass

input("Press any key to exit.\n")
