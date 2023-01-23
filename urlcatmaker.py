import csv
import os
import re
import tldextract

# USER PROMPT
file_path = input("Please enter the file path: ")
print("Extracting information from CSV file...")

# OPEN CSV
with open(file_path, "r") as f:
    reader = csv.DictReader(f)

    # CREATE A DICTIONARY TO HOUSE THE HUNDREDS/THOUSANDS OF LINES 
    data = {}
    row_count = sum(1 for row in reader)
    f.seek(0)
    current_row = 0
    for row in reader:
        current_row += 1
        
        # "USER" SPECIFICALLY FOR ZIA LOG EXPORT DEFINES THE LOCATION/USER
        a = row["User"] 
        
        # "URL" SPECIFICALLY FOR ZIA LOG EXPORT DEFINES THE FULL URL PATH
        b = row["URL"]
        
        # VALIDATE IF THE ENTRY IS AN IP AND REMOVE ONLY THE IP ADDRESS
        match = re.search(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", b)
        if match:
            b = match.group(0)
        else:
            # CUT DOWN THE URL PATH TO ONLY THE TLD AND PREPEND A WILDCARD [.] TO INCLUDE SUBDOMAINS
            # ZIA ONLY COVERS 5 LEVELS. IF SPECFICS ARE REQUIRED, REWORK THIS SPOT AS NEEDED.
            ext = tldextract.extract(b)
            b = "." + ext.domain + '.' + ext.suffix
            
        # VALIDATE IF IN THE DICTIONARY
        if a in data:
            data[a].append(b)
        else:
            data[a] = [b]
            
        # PROGRESS BAR
        print(f"Processing {current_row} of {row_count} rows...({current_row/row_count:.0%} complete)")
        
    # SANITISE
    for key in data:
        data[key] = list(set(data[key]))
        
    # EXPORT TO TEXT FILE. READY TO COPY AND PASTE INTO URL CATEGORIES [USER DEFINED]
    for key in data:
        b_values = data[key]
        file_name = key + ".txt"
        with open(file_name, "w") as f:
            for b in b_values:
                f.write(b + "\n")
