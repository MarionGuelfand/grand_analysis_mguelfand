import os
import time
import argparse

import grand.io.root_trees as rt

parser = argparse.ArgumentParser(description="Compare Root Header")

parser.add_argument('--root1',
                    dest='root1',
                    default='/sps/grand/data/nancay/may2023/ROOTfiles/md000500_f0002.root',
                    type=str,
                    help='Specifies the path of the ROOT data file containing the first\
                          root file.')
parser.add_argument('--root2',
                    dest='root2',
                    default='/sps/grand/data/nancay/may2023/ROOTfiles/md000500_f0002.root',
                    type=str,
                    help='Specifies the path of the ROOT data file containing the second\
                          root file.')      
                    
paths = parser.parse_args()

path1 = paths.root1
path2 = paths.root2

data_file1 = path1.split('/')[-1]
data_file2 = path1.split('/')[-1]

df1   = rt.DataFile(path1)
tadc1 = df1.tadc
tadc1.get_entry(0)
df2   = rt.DataFile(path2)
tadc2 = df1.tadc
tadc2.get_entry(0)

print(tadc1)
print(tadc2)

