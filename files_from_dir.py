import os

def files_from_dir(map, directory="files"):
    list2=[]
    list= os.listdir(f"{os.getcwd()}/{directory}/{map}")
    for file in list:
        if file.endswith(".pdb"):
            list2.append(file[:-4])
    return list2
