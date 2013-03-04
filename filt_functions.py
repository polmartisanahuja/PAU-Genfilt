import numpy as np
import scipy as sp
import scipy.interpolate
import os as os
import sys
import matplotlib.pyplot as plt

def gen_filt(x0, Dx, dx, x_step):
	"""Generates a single rectangle filter with main body 
	width Dx and wings width dx.The main body starts at x0 """
	
	if(Dx == 0): sys.exit("Filter width must be non-zero")
	if(dx == 0): dx = 0.01 * Dx 
	
	y = np.array([0,0.95,0.95,0])
	x = np.array([x0 - dx, x0, x0 + Dx, x0 + Dx + dx])
	
	new_x = np.arange(x[0],x[3] + x_step, x_step)
	new_y = interpol(x, new_x, y)
	
	return new_x, new_y
	
def gen_effect_filt(lam, R, trans_curves_folder):
	"""Returns the filter x,y convoluted with all the transmission curves in
	the ~/routines/trans_curves folder"""
	
	files = os.listdir(trans_curves_folder)
	
	eff_R = R
	for name in files:
		tx, ty = np.loadtxt(trans_curves_folder + name, unpack = True)
		t = sp.interpolate.interp1d(tx,ty)
		eff_R = eff_R * t(lam)
	
	return eff_R
	
def interpol(x, newx, y):
	"""Returnes the array y once has been interpolated into the newx array. 
	The interpolation is made linearly"""
	
	f = sp.interpolate.interp1d(x,y)
	
	return f(newx)
	
def plot_set_filt(list_folder, filt_folder, file_plot):
	"""Plot the filters are in the folder_name"""

	try: os.remove(list_folder + ".DS_Store")
	except: pass
	
	files = list_filt(os.listdir(list_folder), '.res')

	for name in files:
		lam, R = np.loadtxt(filt_folder + name, unpack = True)
		plt.fill(lam, R, alpha = 0.75)

	plt.xlabel("$\lambda$ ($\AA$)")
	plt.ylabel("Throughput")
	plt.title(file_plot)
	plt.savefig(filt_folder + file_plot + '.pdf')
	plt.close()
		
def plot_set_trans_curves(folder_name, file_plot):

	try: os.remove(folder_name + ".DS_Store")
	except: pass
	
	files = list_filt(os.listdir(folder_name), '.txt')
	
	for name in files:
		lam, T = np.loadtxt(folder_name + name, unpack = True)
		plt.plot(lam, T, label = name)

	plt.xlabel("$\lambda$ ($\AA$)")
	plt.ylabel("Transmission")
	plt.legend(loc='best')
	plt.title(file_plot)
	plt.savefig(folder_name + file_plot + '.pdf')
	plt.close()
	
def gen_set_effect_filt(folder_name, folder_name_effective, trans_curves_folder):
	
	try: os.remove(folder_name + ".DS_Store")
	except: pass
	
	files = list_filt(os.listdir(folder_name), '.res')
	
	for name in files:
		lam, R = np.loadtxt(folder_name + name, unpack = True)
		eff_R = gen_effect_filt(lam, R, trans_curves_folder)
		filt = np.array([lam, eff_R])
		np.savetxt(folder_name_effective + name, filt.T, fmt = ["%2.2f", "%5.5f"])
	
def list_filt(files, extention):

	n_ext = len(extention)
	new_files = [] 
	for l in files:
		if(l[-n_ext:] == extention): new_files += [l]	
	return new_files
