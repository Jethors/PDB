import SAP_XML as sap
import os

def SAP_From_List(PDB_List, PDB_files_map, directory=f"{os.getcwd()}/files"):
    """Run SAP-score for a list of PDB-Ids
    Arguments
    PDB_ID: PDB ID of the protein
    PDB_files_map: name of the map which contain the proteins PDB file
    directory: path to the map where the PDB_files_map is located. (defaults to working directory for the program /files)
    """
    for PDB_ID in PDB_List:
        sap.SAP_XML(PDB_ID, PDB_files_map, directory)
