import filt_functions as ft
import numpy as np
import os as os
from pau_narrow_parameters_genfilt_log import *

Ctn = Dx0 / x0

#Compute filters..........................................................
x_init = x0
for i in range(n_filt):
	Dx = Ctn * x_init	
	#x_step = Dx / n_x_step
	print x_init, Dx, x_step

	#Theoretical
	lam, R = ft.gen_filt(x_init, Dx , dx, x_step)
	np.savetxt(theo_filt_folder + str(int(x_init)) + ".res", np.array([lam, R]).T, fmt = ["%2.2f", "%5.5f"])

	#Effective
	eff_R = ft.gen_effect_filt(lam, R, trans_folder)
	np.savetxt(effect_filt_folder + str(int(x_init)) + ".res", np.array([lam, eff_R]).T, fmt = ["%2.2f", "%5.5f"])
	x_init += Dx

#Plot set of narrow filt.................................................

#Theoretical
ft.plot_set_filt(theo_filt_folder, theo_filt_folder, theo_plot_file)

#Effective
ft.plot_set_filt(theo_filt_folder, effect_filt_folder, effect_plot_file)
