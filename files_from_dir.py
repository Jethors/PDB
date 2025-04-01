import os

def files_from_dir(folder, directory=f"{os.getcwd()}/files"):
    """Finds all .pdb files in a folder and returns a list of the PDB IDs
    Arguments:
    folder: The folder containing PDB files
    directory: path to the folder where the selected folder is located. (defaults to files in working directory)
    """
    list2=[]
    list= os.listdir(f"{directory}/{folder}") #lists everything in the folder
    for file in list:
        if file.endswith(".pdb"):  #check if its a pdb file
            list2.append(file[:-4])  #remove .pdb
    return list2
