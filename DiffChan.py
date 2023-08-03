import os
import time
import argparse

import numpy as np
import matplotlib.pyplot as plt

import grand.io.root_trees as rt

'''
## PLOTTING TRACES OF GRAND DATA FILES #
#######################################

GRANDLIB BRANCH: `dev_io_root`

This script reads out a GRAND data file in ROOT format, and returns the difference of the position
of the maximum in channel X and the one in channel Y, in sample unit
'''

## Parser
#########

parser = argparse.ArgumentParser(description="Plot ADC traces of GRAND events.")

parser.add_argument('--path_to_data_file',
                    dest='path_to_data_file',
                    default='/sps/grand/data/nancay/may2023/ROOTfiles/md000500_f0002.root',
                    type=str,
                    help='Specifies the path of the ROOT data file containing the\
                          traces to plot.')
                          
options = parser.parse_args()

PathToDataFile   = options.path_to_data_file

## Read data file and obtain trees
##################################
if not os.path.exists(PathToDataFile):
    raise Exception('File not found:',PathToDataFile)
data_file = PathToDataFile.split('/')[-1]


## Initiate TADC tree and get first TADC entry
##############################################
df   = rt.DataFile(PathToDataFile)
tadc = df.tadc
tadc.get_entry(0)

##############3
# print(tadc)   #<- for debug instances
################

## subplots/plot definition (have to deal differently if 1 or more channels)
############################################################################


diffpos = []
for entry in range(tadc.get_number_of_entries()):

    tadc = df.tadc
    tadc.get_entry(entry)
    chanX = tadc.trace_ch[0][0]
    chanY = tadc.trace_ch[0][1]
    
    maxX = max(chanX)
    maxY = max(chanY)
        
    posX = chanX.index(maxX)
    posY = chanY.index(maxY)
    
    diffpos.append(posX-posY)
    print([posX,posY])

print(diffpos)        
        
