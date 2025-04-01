import pyrosetta
from pyrosetta.rosetta.protocols.rosetta_scripts import XmlObjects
from pyrosetta import pose_from_pdb
from pyrosetta.rosetta.core.scoring import get_score_function
import os


def SAP_XML(PDB_ID, PDB_files_folder, directory=f"{os.getcwd()}/files"):
    """perform sapscore for a protein
    Arguments
    PDB_ID: PDB ID of the protein
    PDB_files_folder: name of the folder which contain the proteins PDB file
    directory: path to the folder where the PDB_files_folder is located. (defaults to working directory for the program /files)
    """
    pdb_id = PDB_ID
    user = os.getlogin()
    program_directory = os.getcwd()
    working_directory = f"{directory}/{PDB_files_folder}" #working directory for this script


    # 🔹 Initialize PyRosetta with beta_nov16 correction
    pyrosetta.init("-corrections::beta_nov16 true")

    # 🔹 Load the PDB file (ensure path is correct)
    os.chdir(working_directory)
    pdb_file = pdb_id + ".pdb"  # Change to actual PDB file
    if not os.path.exists(pdb_file):
        raise FileNotFoundError(f"ERROR: PDB file '{pdb_file}' not found!")

    pose = pose_from_pdb(pdb_file)

    # 🔹 Load the RosettaScripts XML file
    xml_file = "/home/" + user + "/pymol/scripts/per_res_sap.xml"  # Update to actual XML filename
    if not os.path.exists(xml_file):
        raise FileNotFoundError(f"ERROR: XML file '{xml_file}' not found!")

    with open(xml_file, "r") as f:
        xml_script = f.read()

    # 🔹 Parse XML and retrieve objects
    xml_objects = XmlObjects.create_from_string(xml_script)

    # Get Movers
    store_bad_sap_mover = xml_objects.get_mover("store_bad_sap")
    protocol_mover = xml_objects.get_mover("redesign_bad_sap")

    # Get Metrics
    sap_metric = xml_objects.get_simple_metric("my_sap_score")
    per_res_sap_metric = xml_objects.get_simple_metric("my_per_res_sap")

    # 🔹 Step 1: Apply StoreResidueSubset Mover (store bad SAP residues)
    store_bad_sap_mover.apply(pose)

    # 🔹 Step 2: Run the SAP redesign protocol
    protocol_mover.apply(pose)

    # 🔹 Step 3: Calculate per-residue SAP scores and attach them to the pose
    per_res_sap_metric.apply(pose)

    # 🔹 Step 4: Save the modified structure WITH per-residue SAP scores
    output_pdb = pdb_id + "_sap.pdb"
    scorefxn = get_score_function()
    pose.dump_scored_pdb(output_pdb, scorefxn)

    print(f"\n💾 Modified structure with SAP scores saved as '{output_pdb}'")
    os.chdir(program_directory)

