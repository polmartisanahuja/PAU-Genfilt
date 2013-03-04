import filt_functions as ft
import numpy as np
import os as os
from genfilt_narrow_para import *

#Compute filters..........................................................
for i in range(n_filt):
	x_init = x0 + i * Dx

	#Theoretical
	lam, R = ft.gen_filt(x_init, Dx , dx, x_step)
	np.savetxt(theo_filt_folder + str(x_init) + ".res", np.array([lam, R]).T, fmt = ["%2.2f", "%5.5f"])

	#Effective
	eff_R = ft.gen_effect_filt(lam, R, trans_folder)
	np.savetxt(effect_filt_folder + str(x_init) + ".res", np.array([lam, eff_R]).T, fmt = ["%2.2f", "%5.5f"])

#Plot set of narrow filt.................................................

#Theoretical
ft.plot_set_filt(theo_filt_folder, theo_filt_folder, theo_plot_file)

#Effective
ft.plot_set_filt(theo_filt_folder, effect_filt_folder, effect_plot_file)
