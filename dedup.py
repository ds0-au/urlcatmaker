import os
from tqdm import tqdm

# USER PROMPT
original_folder = input("Enter the path of the original folder containing the text files: ")

# CREATE NEW FOLDER TO STORE
export_folder = os.path.join(original_folder, 'Export')
if not os.path.exists(export_folder):
    os.makedirs(export_folder)

# CREATE AN EMPTY SET TO STORE LINES
unique_lines = set()

# MAKE A LIST TO STORE THE INPUT FILES
input_files = [f for f in os.listdir(original_folder) if f.endswith('.txt')]

# OPEN A FILE TO WRITE DUPLICATES TO
with open(os.path.join(export_folder, 'duplicates.txt'), 'w') as dup_file:
    for file in input_files:
        unique_lines_list = []
        with open(os.path.join(original_folder, file), 'r') as in_file:
            for line in tqdm(in_file):
                if line in unique_lines:
                    dup_file.write(line)
                else:
                    unique_lines.add(line)
                    unique_lines_list.append(line)
        # WRITE THE REMAINING UNIQUE LINES TO A FILE
        with open(os.path.join(export_folder, file), 'w') as dedup_file:
            for line in unique_lines_list:
                dedup_file.write(line)
