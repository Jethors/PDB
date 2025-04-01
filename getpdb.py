import os
import requests
import time


def download_pdb(pdb_ids, folder="lac_PDB_files",directory="files" , retries=1, delay=2):
    """Downloads PDB files while avoiding re-downloading existing files.

    Arguments:
    - pdb_ids: List of PDB IDs to download.
    - directory: Directory where PDB files will be saved (defaults to 'files' in the working dir).
    - folder: Subfolder name inside the directory (e.g., 'lac_PDB_files').
    - retries: Number of times to retry a failed download.
    - delay: Seconds to wait before retrying a failed request.
    """
    save_dir = os.path.join(os.getcwd(), directory, folder)  # Full path
    os.makedirs(save_dir, exist_ok=True)  # Ensure directory exists

    base_url = "https://files.rcsb.org/download/{}.pdb"
    total_files = len(pdb_ids)
    success_count = 0  # Counter for successful downloads
    skipped_count = 0  # Counter for skipped files
    failed_ids = []  # List to store PDB IDs that failed after all retries

    for index, pdb_id in enumerate(pdb_ids, start=1):  # Track progress
        pdb_id = pdb_id.strip().upper()
        file_path = os.path.join(save_dir, f"{pdb_id}.pdb")

        # ✅ **Check if file already exists**
        if os.path.exists(file_path):
            skipped_count += 1
            print(f"⏩ ({index}/{total_files}) Skipped: {pdb_id} (Already exists)")
            continue  # Move to the next file

        url = base_url.format(pdb_id)

        for attempt in range(retries):
            try:
                response = requests.get(url, timeout=10)  # Timeout to prevent hanging

                if response.status_code == 200:
                    with open(file_path, "wb") as f:
                        f.write(response.content)
                    success_count += 1  # Increment successful download counter
                    print(f"✅ ({success_count}/{total_files}) Downloaded: {pdb_id}")
                    break  # Exit retry loop on success
                else:
                    print(f"⚠️ ({index}/{total_files}) Failed to get {pdb_id} (Status: {response.status_code})")

            except requests.exceptions.RequestException as e:
                print(f"❌ ({index}/{total_files}) Error downloading {pdb_id}: {e}")

            if attempt < retries - 1:
                print(f"🔄 Retrying {pdb_id} in {delay} seconds...")
                time.sleep(delay)  # Wait before retrying

        else:
            # After all retries, add the PDB ID to the failed list
            failed_ids.append(pdb_id)
            print(f"❗ ({index}/{total_files}) Giving up on {pdb_id} after {retries} attempts.")

    print(f"\n🎯 Finished! {success_count}/{total_files} PDB files downloaded successfully.")
    print(f"📁 Skipped {skipped_count} files (Already existed).")

    # Print the list of PDB IDs that failed after all retries
    if failed_ids:
        print("\n⚠️ The following PDB IDs failed after all retries:")
        for failed_id in failed_ids:
            print(f"- {failed_id}")
