"""
This code is not completed yet. 
When finished, it will show plots of the effective area of ORCA6.
"""


import ROOT
import math

ROOT.gStyle.SetOptStat(0)

INPATH="/pbs/home/m/mgutierr/km3ant-examples/previous_analysis/ICRC2021/results/"
INNAME="outputTree_ICRC2021_ORCA6_v6.00_data.root"
#INNAME="outputTree_ICRC2021_ORCA6_v6.00_nu-mu-CC-higher.root"
f=ROOT.TFile(INPATH+INNAME, 'READ')
tree=f.Get('tree')
ngen=tree.GetEntries()
print ("ngen=", ngen)
N_Ebins=36


#Let's consider only events with energy greater than 0
ngen=0

for entry in tree:
	if entry.energy>0.1:
		ngen+=1

print(ngen)


c1=ROOT.TCanvas("c1","c1",400,400)


hevts = ROOT.TH1D("hevts", "evens", N_Ebins, 0.1, 200)
tree.Draw('energy >> hevts', 'weight/(energy)', 'E0')
hevts.Scale(1./(ngen*math.log(10)*hevts.GetBinWidth(1)*3600*24*365*2*math.pi))
c1.Draw()
c1.SaveAs("plot.pdf")
