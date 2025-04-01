import os

def files_from_dir(map, directory=f"{os.getcwd()}/files"):
    """Finds all .pdb files in a map and returns a list of the PDB IDs
    Arguments:
    map: The map containing PDB files
    directory: path to the map where the selected map is located. (defaults to files in working directory)
    """
    list2=[]
    list= os.listdir(f"{directory}/{map}") #lists everything in the map
    for file in list:
        if file.endswith(".pdb"):  #check if its a pdb file
            list2.append(file[:-4])  #remove .pdb
    return list2
