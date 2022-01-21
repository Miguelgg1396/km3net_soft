"""
This script takes the root histogram files generated with km3ant and shows several plots.
"""

import ROOT
from ROOT import TLegend
import numpy as np
import uproot
import matplotlib.pyplot as plt
import os


OUTDIR="./plotsMiguel/"
INDIR="./results/"


#Defining paths inside the root files
ROOTDIR1="ICRC_V2_count_hists/Cos theta/"
ROOTDIR2="ICRC_V2_count_hists/JEnergy (linear scale)/"
CROOTDIR1="ICRC_V2_100GeV_count_hists/Cos theta/"
CROOTDIR2="ICRC_V2_100GeV_count_hists/JEnergy (linear scale)/"
ROOTDIR3="ICRC_V2_count_hists/JEnergy (log scale)/"
CROOTDIR3="ICRC_V2_100GeV_count_hists/JEnergy (log scale)/"
ROOTDIR4="ICRC_V2_count_hists/JStart energy (log scale)/"
CROOTDIR4="ICRC_V2_100GeV_count_hists/JEnergy (log scale)/"
ROOTDIR5="antinoise_count_hists/Cos theta/"
label1="cos(theta)"
label2="E (GeV)"

#PATHS is defined in this way: (name of the plot, variable to plot, x-axis legend, lin or log plot, xmin, xmax)
PATHS=[("cos_nocut.pdf", ROOTDIR1, label1, "lin", -1, 1), ("En_nocut.pdf", ROOTDIR2, label2, "lin", 0, 120), ("logEn_nocut.pdf", ROOTDIR3, label2, "log", 1, 1e4), ("StEn_nocut.pdf", ROOTDIR4, label2, "log", 1, 1e3), ("cos_cut.pdf", CROOTDIR1, label1, "lin", -1, 1), ("En_cut.pdf", CROOTDIR2, label2, "lin", 0, 120), ("logEn_cut.pdf", CROOTDIR3, label2, "log", 0, 1e3), ("StEn_cut.pdf", CROOTDIR4, label2, "log", 1, 1e3), ("cos_antinoise.pdf", ROOTDIR5, label1, "lin", -1, 1)]


f = ROOT.TFile(INDIR+"hist_ICRC2021_ORCA6_v6.00.root")
ROOT.gStyle.SetOptStat(0)


for tuple in PATHS:
	path=tuple[1]
	name=tuple[0]
	h_data = f.Get(path+"data")
	h_MC = f.Get(path+"mc total")
	h_nueCC=f.Get(path+"nu e CC tot")
	h_numuCC=f.Get(path+"nu mu CC tot")
	h_nutauCC=f.Get(path+"nu tau CC tot")
	h_numuNC=f.Get(path+"nu mu NC tot")
	h_muon=f.Get(path+"muons")

	#MC is defined in this way: (title to show in the legend, color of the plot, variable to save the plot)
	MC=[("MC tot", 2, h_MC), ("nu mu CC", 7, h_numuCC),("nu e CC", 6, h_nueCC), ("nu tau CC", 4, h_nutauCC), ("nu mu NC", 3, h_numuNC), ("muon", 5, h_muon)] 


	c1=ROOT.TCanvas("can")
	if tuple[3]=="log":
		c1.SetLogx()
	else:
		c1.SetLogx(0)
		
	legend=TLegend(0.7,0.7,1,1)
	h_data.SetTitle("")
	legend.AddEntry(h_data, "Data")
	h_data.GetXaxis().SetTitle(tuple[2])
	h_data.GetYaxis().SetTitle("Num. Events")
	h_data.SetMarkerStyle(20)
	h_data.SetAxisRange(tuple[4], tuple[5], "X")
	h_data.Draw("PLC E1")
	for mctuple in MC:
		h=mctuple[2]
		color=mctuple[1]
		lnames=mctuple[0]
		h.SetLineColor(1)
		h.SetFillColor(color)
		h.Draw("SAME HIST")
		legend.AddEntry(h, lnames)
		
	legend.AddEntry(0,"N_data: " + str("{0:.1f}".format(h_data.Integral(""))))
	legend.AddEntry(0,"N_MC: " + str("{0:.1f}".format(h_MC.Integral(""))))

	legend.Draw()
	c1.SaveAs(OUTDIR+name)
	c1.Delete()

