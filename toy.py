"""
This script is just a toy script to make sure that the tuples I have created with the km3ant software are readable.
"""

import ROOT
import math

#Let's define the input and output
inpath="/pbs/home/m/mgutierr/km3ant-examples/previous_analysis/ICRC2021/results/"
infile="outputTree_ICRC2021_ORCA6_v6.00_data.root"
#infile="hist_ICRC2021_ORCA6_v6.00.root"


fIn = ROOT.TFile(inpath+infile, "read")

tree = fIn.Get('tree')
tree.SetAlias("run_id","E.run_id") #remove th dot so we make sure that python won't give errors 

tree.Print()
print (tree.GetEntries())



cont=0
for entry in tree:
	#print (getattr(entry, "E.trks.E[:,0]"))
	if entry.energy>0:
		print (entry.weight*1e-4*entry.energy**-2)
	
	if entry.ICRC_V2_cuts == 1:
		cont+=1
	
print(cont)
