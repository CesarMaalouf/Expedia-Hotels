# Predicting Hotel Choices from Search Parameter

## Data
Data can be downloaded from the kaggle competition page on Expedia data.
It can be put into any directory you choose.
The path where the data is located should be placed in a file called `datapath.txt`.
The file `example_datapath.txt` shows an example which points to the local directory.
The path should then be read from this file using

    with open('datapath.txt') as f:
    	 datapath=f.readlines()[0].rstrip()

