import SAP_XML as sap
import os

def SAP_From_List(PDB_List, PDB_files_folder, directory=f"{os.getcwd()}/files"):
    """Run SAP-score for a list of PDB-Ids
    Arguments
    PDB_ID: PDB ID of the protein
    PDB_files_folder: name of the folder which contain the proteins PDB file
    directory: path to the folder where the PDB_files_folder is located. (defaults to working directory for the program /files)
    """
    for PDB_ID in PDB_List:
        sap.SAP_XML(PDB_ID, PDB_files_folder, directory)
