# -*- coding: utf-8 -*-
"""
This file contains code we used to build the the Baird's Sparrow locations
visualization. It extracts all DLS locations from a specific document and
saves the results into a .csv file.

It is important to note that this script does not identify which locations include
the Baird's Sparrow. This was done manually using the output csv file from this script.
"""

import pandas as pd

import html_analyzer
import html_document

"""
Please change the following variables to where you have the input and where
you want the output:
    INPUT_FILE:     the input HTML file for the location extraction
    OUTPUT_FILE:    the output .csv file in which the DLS locations extracted from
                    the document will be recorded in
"""

INPUT_FILE = "W:/COE/coeprojects/NEB/2019_IN_Text_S52/03_WIP/bairds-sparrow-demo/bairds-sparrow-location-extraction/B3%2D07 %2D Appendix 06 %2D ESA Appendix 10 %2D Wildlife Technical Report Part 2 of 2 %2D A4E7D7.html"
OUTPUT_FILE = "W:/COE/coeprojects/NEB/2019_IN_Text_S52/03_WIP/bairds-sparrow-demo/bairds-sparrow-location-extraction/locations.csv"


# columns of the output .csv table
order = []
lat_long = []
dls_code = []
page_numbers = []

with open(INPUT_FILE, 'r', encoding='utf-8') as f:
    # initialize document
    html_doc = html_document.html_document(f, extract_images=False)
    for page_number, page in enumerate(html_doc.pages):
        # find all DLS location tags
        _, dls, _, _ = html_analyzer.find_location_tags(page)
        for dls_loc in dls:
            # add location to table
            order.append(len(order) + 1)
            lat_long.append(dls_loc.lat_long.text)
            dls_code.append(dls_loc.text)
            page_numbers.append(page_number + 1)
            

# save table as .csv
df = pd.DataFrame({'order_in_document': order, 'latitude_longitude': lat_long, 'DLS_code': dls_code, 'page_number': page_numbers})
df.to_csv(OUTPUT_FILE)
        
