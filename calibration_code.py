##############################
# Capacitive Soil Moisture
# Sensor Calibration Analysis
##############################
#
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

container_mass = 22.75 # measured mass of container [g]
soil_mass_dry = 24.74 # mass of dry soil [g]
soil_vol = 200 # volume of soil sample [ml]

rho_s = (soil_mass_dry/1000.0)/(soil_vol*np.power(10.0,-6.0)) # bulk density of soil [kg/m^3]
rho_w = 997.0 # density of water [kg/m^3]

###############################################
# Data inputs
#
soil_masses = np.subtract([62.78,71.51,82.41,96.94,109.22,
                           132.37,138.9,159.02,186.76],container_mass) # mass measurements [g]
cap_sensor_readings = np.array([2.96,2.90,2.94,2.78,2.43,2.08,2.04,2.01,1.81]) # cap sensor readings [V]

###############################################
# calculating volumetric water content [%]
#
theta_g = (soil_masses - soil_mass_dry)/soil_mass_dry # water proportion
theta_v = ((theta_g*rho_s)/rho_w) # volumetric soil content [g/ml / g/ml]

###############################################
# Fitting 1/sensor readings with measurements
#
x_for_training = 1.0/cap_sensor_readings # 1/sensor readings
slope, intercept, r_value, p_value, std_err = stats.linregress(x_for_training, theta_v) # linear fit
theta_predict = (slope*(x_for_training))+intercept # prediction of theta_v with sensor

###############################################
# Plot the results
#
plt.style.use('ggplot')
fig,axs = plt.subplots(2,1,figsize=(12,9))
# plotting the sensor to theta_v
ax = axs[0]
ax.plot(x_for_training,theta_v,label='Data',linestyle='',marker='o',color=plt.cm.Set1(0),
       markersize=10,zorder=999)
ax.plot(x_for_training,theta_predict,label='Fit ({0:2.2f}$\cdot$(1/V) {1:+2.2f})'.format(slope,intercept),
        color=plt.cm.Set1(1),linewidth=4)
ax.set_xlabel(r'Inverse of Capacitive Sensor Voltage [V$^{-1}$]',fontsize=18)
ax.set_ylabel(r'$\theta_v$ [cm$^{3}$/cm$^3$]',fontsize=18)
ax.legend(fontsize=16)

rmse = np.sqrt(np.mean(np.power(np.subtract(theta_predict,theta_v),2.0))) # value error
mape = np.mean(np.divide(np.subtract(theta_predict,theta_v),theta_v)*100) # % error

# plotting the comparison between fit and data
ax2 = axs[1]
ax2.plot(theta_predict,theta_v,label='Capacitive (RMSE: {0:2.3f}, MAPE: {1:2.0f}%)'.format(rmse,mape),
         linestyle='',marker='o',color=plt.cm.Set1(2),markersize=10,zorder=999)
ax2.plot(theta_v,theta_v,label='Gravimetric',color=plt.cm.Set1(3),linewidth=4)
ax2.set_xlabel(r'$\theta_{v,cap}$ [cm$^{3}$/cm$^3$]',fontsize=18)
ax2.set_ylabel(r'$\theta_{v,grav}$ [cm$^{3}$/cm$^3$]',fontsize=18)
ax2.legend(fontsize=16)
fig.savefig('soil_moisture_calibration_results.png',dpi=300,bbox_inches='tight',facecolor='#FCFCFC')
plt.show()
