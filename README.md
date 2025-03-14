# SparrowSpotter

## Purpose
The purpose of **SparrowSpotter** is to visualize the locations of specific species of interest, utilizing the results from location extraction. Using a sample document, all locations related to the **Baird’s Sparrow** (a bird species designated as “Special Concern”) were identified. These locations were then plotted onto an interactive map using **Leaflet**.

## Input
- The document containing locations related to the **Baird’s Sparrow**.

## Output
- An interactive map of all locations extracted from the document, with the option to highlight locations specifically related to the **Baird’s Sparrow**.

## Tools
- **Leaflet**: An open-source JavaScript library used to build web mapping applications.
- **jQuery**: An open-source JavaScript library used for web development.
- **OpenStreetMap**: A free map tile provider.
- **BeautifulSoup4**: An open-source HTML parsing library for Python, used to extract text content, font styles, locations, sizes, and other useful information from HTML documents.
- **Regular Expressions (regex)**: A pattern matching tool for text that allows us to identify locations in consistent formats for specific location extraction.

## Code

- **convert-sparrow-locations-to-json.py**: This script converts a .csv file of Baird’s Sparrow locations to a JavaScript file with JSON data, enabling it to be loaded into the visualization.
  
The `bairds-sparrow-location-extraction/` folder contains:
- The HTML document used for this demonstration.
- The code used to extract locations, named **extract-locations-bairds-sparrow.py**. This script is similar to the location extraction for all documents, except the output is a .csv (instead of a text file) to easily fill in the locations related to the Baird’s Sparrow.

The `docs/` folder contains:
- The JavaScript code (demo.js) used for the map.

## Method
1. **Extraction**: All locations were extracted from the sample document using the location extraction methods documented in Appendix J. The locations were saved into a .csv file, which included information on which page each location was identified on and the order in which the locations appeared in the document.

2. **Manual Check**: Using the output .csv file, we manually checked the locations in the document to find those related to the **Baird’s Sparrow**. These locations were marked in a designated column in the .csv file.

3. **Conversion**: The final .csv file was converted to a JavaScript file containing a JSON object with information on the locations.

4. **Visualization**: A visualization was built using **Leaflet**, with tiles provided from **OpenStreetMap**. This visualization allows users to view all locations identified in the document and highlight locations specifically related to the **Baird’s Sparrow**.
