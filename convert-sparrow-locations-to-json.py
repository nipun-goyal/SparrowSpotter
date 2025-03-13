# -*- coding: utf-8 -*-
"""
This file contains code to convert the .csv containing information on which
locations mention the Baird's Sparrow in the document to a JavaScript file
with a JSON object so it can be loaded into the interactive map.
"""
import json
import pandas as pd
import re

"""
Please change the following variables to where you have the input and where
you want the output:
    INPUT_CSV:  the .csv file containing the data about the Baird's Sparrow locations
    OUTPUT_JS:  the .js file containing the converted JSON data so it can be loaded
                into the interactive visualization
"""
INPUT_CSV = "W:/COE/coeprojects/NEB/2019_IN_Text_S52/03_WIP/bairds-sparrow-demo/bairds_sparrow_locations.csv"
OUTPUT_JS = "W:/COE/coeprojects/NEB/2019_IN_Text_S52/03_WIP/bairds-sparrow-demo/interactive-map/locations.js"


# read the sparrow locations
sparrow_locations_df = pd.read_csv(INPUT_CSV)

# container for the output, contains a list of dictionaries with each dictionary
# containing data representing a single location identified from the document
# (along with information on whether that location is associated with the Baird's Sparrow)
output = []

for _, row in sparrow_locations_df.iterrows():
    # use regular expressions to convert the text representation of the lat-long
    # coordinate into floats representing degrees North and West
    N = float(re.findall(r'(\d+\.\d+)\sN', row['latitude_longitude'])[0])
    W = float(re.findall(r'(\d+\.\d+)\sW', row['latitude_longitude'])[0])
    
    output.append({
        "DLS_code": row["DLS_code"],
        "page_number": row["page_number"],
        "species": "unknown" if pd.isna(row["species"]) else row["species"],
        "status": "unknown" if pd.isna(row["status"]) else row["status"],
        "N": N,
        "W": W,
        "text": row["latitude_longitude"]
    })

# convert the output list to JSON and write to the output file
with open(OUTPUT_JS, "w+", encoding="utf-8") as f:
    f.write("const locations = ")
    f.write(json.dumps(output, indent=2))
    
