import readExcell as excell
import readWrite_csv as csv
import getpdb as pdb
"""packages som behövs i importerna och denna kod: panda openpyxl requests rcsb-api"""

# skapa listor av column 2 i Excel document
listEco = excell.read_excel_column("files/ProteinlistaEco.xlsx")
listSal = excell.read_excel_column("files/ProteinlistaSal.xlsx")
listLac = excell.read_excel_column("files/ProteinlistaLac.xlsx")

# API code
from rcsbapi.search import AttributeQuery, TextQuery
rId_list = []
    # välj lista
for val in listSal:
    q1 = TextQuery(value= val)
    #q2 = TextQuery(value= "lactobacillus")
    #q3 = TextQuery(value= "")
    q4 = AttributeQuery(
        attribute= "rcsb_entity_source_organism.scientific_name",
        operator= "exact_match",
        value="salmonella",
    )

    query = q1 & q4
    for rId in query():
        if rId not in rId_list:
            rId_list.append(rId)
print(f" rId_list innehåller {len(rId_list)} stycken Id!")



# testlista
TestList=["1CRN","4HHB","1DG1"]

# sparar en fil, välj filnamn , (går att ändra directory med ett 3:e atribut)
csv.write_csv("Sal_output.csv", rId_list)

# läser in csv fil, välj rätt fil, (det går att ändra directory med ett andra attribut).
pdb_list = csv.read_csv("Sal_output.csv")

# laddar ner pdb, välj var du ska skappa mappen samt mappens namn, i förhållande till denna python fil
pdb.download_pdb(pdb_list, directory="files", map="SalPDBfiles", retries=1, delay=2)

print("KLAR")

