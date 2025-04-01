import readExcell as excell
import readWrite_csv as csv
import getpdb as pdb
import SAP_From_List as sapl
from rcsbapi.search import AttributeQuery, TextQuery
import files_from_dir as ffd

"""packages needed for this code: panda openpyxl requests rcsb-api pyrosetta-distributed"""

# Creates lists from column 2 in an Excel document
listEco = excell.read_excel_column("files/ProteinlistaEco.xlsx")
listSal = excell.read_excel_column("files/ProteinlistaSal.xlsx")
listLac = excell.read_excel_column("files/ProteinlistaLac.xlsx")

# Search API code
rId_list = []
    #Query configuration
for val in listSal: # Choose list
    q1 = TextQuery(value= val)
    #q2 = TextQuery(value= "lactobacillus")
    #q3 = TextQuery(value= "")
    q4 = AttributeQuery(
        attribute= "rcsb_entity_source_organism.scientific_name",
        operator= "exact_match",
        value="salmonella",
    )

    query = q1 & q4
    #Creates a list of all the search results and filters out duplicates.
    for rId in query():
        if rId not in rId_list:
            rId_list.append(rId)
print(f" rId_list innehåller {len(rId_list)} stycken Id!")

# Saves a CSV file of search results.
csv.write_csv("Sal_output.csv", rId_list) # Choose file name, it's saved in /files in working directory by default, can be changed. Replaces files with the same name.

# Read a CSV file and create a list.
pdb_list = csv.read_csv("Sal_output.csv") #Choose the file name of the file you want to read, defaults to /files/"selected file name" in working directory, can be changed.

# Download PDB files from a list, creates map if it does not exist, uses existing map if it exists.
pdb.download_pdb(pdb_list, "SalPDBfiles", retries=0) #Give a list of PDB IDs to the constructor and choose the name of the folder where the files should be downloaded to. Defaults to /files/"selected folder" in working directory, can be changed.

# Read a list of available PDB files in a folder, defaults to /files/"chosen folder" in working directory. (PDB ID list)
pdb_list_from_dir= ffd.files_from_dir("SalPDBfiles") # Choose the folder, directory of the folder defaults to /files/"selected folder" in working directory.

#SAP the PDB files in a folder.
sapl.SAP_From_List(pdb_list_from_dir, "SalPDBfiles") #Give a list of the pdb files in the folder and the name of the folder, defaults to /files/"selected folder" in working directory.

