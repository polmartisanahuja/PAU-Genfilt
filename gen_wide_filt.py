import filt_functions as ft
import numpy as np
import os as os
from pau_wide_parameters_genfilt import *
	
#Compute effective filters...............................................
ft.gen_set_effect_filt(theo_filt_folder, effect_filt_folder, trans_folder)

#Plot set of narrow filt.................................................

#Theoretical
ft.plot_set_filt(theo_filt_folder, theo_filt_folder, theo_plot_file)

#Effective
#ft.plot_set_filt(theo_filt_folder, effect_filt_folder, effect_plot_file)
