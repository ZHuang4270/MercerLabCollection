# MercerLabCollection
This is a small python program designed to collect 5S, 16S, and 23S rRNA sequences from genome text files


Required libraries: Selenium, requests, re, bs4, glob, os, search, folderparser, tkinter

Input: A folder full of text or FNA files. Each file should be the full genome of a bacteria downloaded from NCBI
Output: Within the same folder, rRNAs will be collected in fasta format and placed into new folders (categorized by species)

Suggestion: Run the program in an IDE (I used Pycharm)

Noteable change: In search.py, line 79 points to a specific location for the headless Chrome webdriver. You'll want to change that. 

Walkthrough:

First, the program asks if the use would like to use the most recent read folder. 
If not, the program will prompt the user to point it towards a different folder.
Keep in mind that the program will write the new .fasta documents in the same folder.

The program next asks if the user would like to use the most recent products.
If not, the user should separate the product they're interested in by spaces.

The program will iterate through the folder and begin to parse out the files. The header is structured as such:

>{First Letter of genus, first two letters of species}_{Strain}_{First letter of host genus, first two letters of host species}_{rRNA product} {Full genus}_{Full species}_{Strain}

For example: ">Bap_BAg_BAg_5S Buchnera_aphidicola_BAg" for Buchnera aphidicola (Aphis glycines) strain BAg (NZ_CP009253.1)

The program will parse through the NCBI website. It is set to take some time to allow the website to load.
Occasionally, the program will crash because the  website wasn't given enough time to load. Usually, rerunning the program will do the trick. 
To change the amount of time the website is given to load, go to search.py line 83

The program will do its best to suggest a header. 
For example: Bap_BAg_xx_xx Buchnera_aphidicola_BAg (The xx's hold the spot for the host and the rRNA product)
If the user chooses yes, the program prompts the user for a host (in the host format referenced above)
If the user chooses no, the program prompts the user to enter in their own header. The format should be like this:
"Cam_FDAARGOS.165_NA Citrobacter_amalonaticus_FDAARGOS.165"
Note that the user is expected to include the host as well, but does not have to leave space for the rRNA product.

Once the user confirms their input, the program creates the files and moves on to the next genome.

Naming conventions: For some strains, there are special characters we removed/replaced.
If the strain has a space in its name, the space was skipped and the two words were concatenated together. 
If the strain had a "-" or a "_", they were replaced with "."


