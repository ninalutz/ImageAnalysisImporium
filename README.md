# ImageAnalysisImporium
A set of scripts authored by myself and my students at the University of Washington for ongoing work in image analysis. This folder is in use for our Directed Research Group around problematic imagery at the US Mexico land border. 

## Folder Structure
The scripts that are cleaned and ready for use are at the main level directory of this repository. 

### testing_scripts
These are for scripts that are actively being tweaked and developed by students or myself and are not meant for further use. 

### test_images
This image folder has 4 types of subfolders for testing:
#### 1. test_collection_border: This is a test selection of typical border rhetoric images
#### 2. test_collection_charts: This is a collection of charts (bar, pie, line, etc) with annotations 
#### 3. test_collection_fish: These are fish for debugging visual scripts -- highly recommend these instead of problematic imagery
#### 4. test_collection_memes: This is a folder of memes around the border rhetoric -- great for testing text extraction. 
This folder also has a test grid of Stable Diffusion images to test a grid parser helper script.

## Script Descriptions 
#### avg.py - Katie Arriaga, Nina Lutz 
This script takes in a collection of images and outputs the average of them, centering and scaling images of different sizes together. This utilizes a composite methodology to give an overall summation of a collection of images.

#### ocr_batch.py - Wilson Chen, Nina Lutz

#### edges.py - Zayna Lughod, Nina Lutz
This script takes in images and outputs their Canny edges
#### gridparse.py - Nina Lutz
#### colorquant.py - Jordyn Padzensky
