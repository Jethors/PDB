import SAP_XML as sap

def SAP_From_List(PDB_List, PDB_files_map, directory="files"):
    for PDB_ID in PDB_List:
        sap.SAP_XML(PDB_ID, PDB_files_map, directory)
