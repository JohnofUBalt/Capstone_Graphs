#_____________________________##CONDITIONS GRAPHS_______________________________#

#Conditions: pH - line graph
import matplotlib.pyplot as plt
import pandas as pd
condtions = pd.read_excel(r"C:\Users\terra\OneDrive\Documents\UB_Documents\Classes\2024_Spring_ENVS_490_Capstone\Aeroponic_Project_Conditions_Results_Got_Plants_and_Water.xlsx", sheet_name= "Conditions")
condtions_df = pd.DataFrame(condtions)

plt.plot(condtions_df['Date'], condtions_df['pH'], color = "green")
plt.title("pH Over Course of Experiment", fontsize = 15, color = "navy")
plt.grid("major")
plt.xlabel("Date")
plt.ylabel("pH")
plt.show()

#Conditions: EC - line graph
import matplotlib.pyplot as plt
import pandas as pd
condtions = pd.read_excel(r"C:\Users\terra\OneDrive\Documents\UB_Documents\Classes\2024_Spring_ENVS_490_Capstone\Aeroponic_Project_Conditions_Results_Got_Plants_and_Water.xlsx", sheet_name= "Conditions")
condtions_df = pd.DataFrame(condtions)

plt.plot(condtions_df['Date'], condtions_df['EC'], color = "grey")
plt.title("EC Over Course of Experiment", fontsize = 15, color = "navy")
plt.grid("major")
plt.xlabel("Date")
plt.ylabel("Electroconductivity (EC)")
plt.show()

#Conditions: Humidity - line graph
import matplotlib.pyplot as plt
import pandas as pd
condtions = pd.read_excel(r"C:\Users\terra\OneDrive\Documents\UB_Documents\Classes\2024_Spring_ENVS_490_Capstone\Aeroponic_Project_Conditions_Results_Got_Plants_and_Water.xlsx", sheet_name= "Conditions")
condtions_df = pd.DataFrame(condtions)

plt.plot(condtions_df['Date'], condtions_df['Humidity'])
plt.grid("major")
plt.xlabel("Date")
plt.ylabel("Humidity%")
plt.title("Humidity Over Course of Experiment", fontsize = 15, color = "navy")
plt.show()

#Conditions: Air Temp - line graph
import matplotlib.pyplot as plt
import pandas as pd
condtions = pd.read_excel(r"C:\Users\terra\OneDrive\Documents\UB_Documents\Classes\2024_Spring_ENVS_490_Capstone\Aeroponic_Project_Conditions_Results_Got_Plants_and_Water.xlsx", sheet_name= "Conditions")
condtions_df = pd.DataFrame(condtions)

plt.plot(condtions_df['Date'], condtions_df['Air Temp'])
plt.grid("major")
plt.xlabel("Date")
plt.ylabel("Air Temperature (Celsius)")
plt.title("Air Temp Over Course of Experiment", fontsize = 15, color = "navy")
plt.show()

#Conditions: Pots with Growth - bar graph
import matplotlib.pyplot as plt
import pandas as pd
condtions = pd.read_excel(r"C:\Users\terra\OneDrive\Documents\UB_Documents\Classes\2024_Spring_ENVS_490_Capstone\Aeroponic_Project_Conditions_Results_Got_Plants_and_Water.xlsx", sheet_name= "Conditions")
condtions_df = pd.DataFrame(condtions)

plt.plot(condtions_df['Date'], condtions_df['Pots with Growth'], color = "green")
plt.grid("major")
plt.xlabel("Date")
plt.ylabel("Number of Pots")
plt.title("Number of Pots with Growth Over Course of Experiment", fontsize = 15, color = "navy")
plt.show()


#_____________________________RESULTS GRAPHS__________________________________#

#results gross mass growth
import matplotlib.pyplot as plt
import pandas as pd
results = pd.read_excel(r"C:\Users\terra\OneDrive\Documents\UB_Documents\Classes\2024_Spring_ENVS_490_Capstone\Aeroponic_Project_Conditions_Results_Got_Plants_and_Water.xlsx", sheet_name = "Results")
results_df = pd.DataFrame(results)
x = results_df['Harvest #']
y = results_df['Gross Growth Mass']

plt.bar(x, y, width = .75)
plt.xlabel("Harvest Number")
plt.xticks(results_df["Harvest #"])
plt.ylabel("Gross Mass")
plt.show()

#results net growth
import matplotlib.pyplot as plt
import pandas as pd
results = pd.read_excel(r"C:\Users\terra\OneDrive\Documents\UB_Documents\Classes\2024_Spring_ENVS_490_Capstone\Aeroponic_Project_Conditions_Results_Got_Plants_and_Water.xlsx", sheet_name = "Results")
results_df = pd.DataFrame(results)
x = results_df['Harvest #']
y = results_df['Net Growth']

plt.bar(x, y, width = .75)
plt.xlabel("Harvest Number")
plt.xticks(results_df["Harvest #"])
plt.ylabel("Net Mass")
plt.title("Net Wet Mass by 'Harvest'")
plt.show()

#results gross dry mass
#results net growth
import matplotlib.pyplot as plt
import pandas as pd
results = pd.read_excel(r"C:\Users\terra\OneDrive\Documents\UB_Documents\Classes\2024_Spring_ENVS_490_Capstone\Aeroponic_Project_Conditions_Results_Got_Plants_and_Water.xlsx", sheet_name = "Results")
results_df = pd.DataFrame(results)
x = results_df['Harvest #']
y = results_df['Gross Dry Mass']

plt.bar(x, y, width = .75)
plt.xlabel("Harvest Number")
plt.xticks(results_df["Harvest #"])
plt.ylabel("Gross Dry Mass (g)")
plt.show()


###GOT PLANTS AND/OR WATER - GROUPED BAR CHART###
#original code from Codefinity, modified for use in this project

#importing necessary modules
import matplotlib.pyplot as plt
import pandas as pd
import numpy as py

#setting up necessary parameters(?)
got_plants_and_water = pd.read_excel(r"C:\Users\terra\OneDrive\Documents\UB_Documents\Classes\2024_Spring_ENVS_490_Capstone\Aeroponic_Project_Conditions_Results_Got_Plants_and_Water.xlsx", 
                                     sheet_name = "Got_Water_or_Plants", 
                                     usecols = ["Pot", "Days with Water", "Days with Growth"])
plants_and_water_df = pd.DataFrame(got_plants_and_water)

#making arrays
Pots = py.array(plants_and_water_df["Pot"])
water_pots = py.array(plants_and_water_df["Days with Water"])
growth_pots = py.array(plants_and_water_df["Days with Growth"])
positions = py.arange(len(Pots))
water_or_growth = py.array([water_pots, growth_pots])

#plotting bars using for loop
width = .4
for i in range(len(water_or_growth)):
    plt.bar(positions + width * i, water_or_growth[i], width)


#customization of axes, labels, add legend, size title, etc.
plt.xlabel("Pot Number", color = "navy")
plt.ylabel("Number of Days", color = "navy")
plt.title("Number of Days Pots had Water and/or Plant Growth", 
          fontsize = 15, 
          color = "navy")
plt.xlabel("Pot")
plt.yticks(py.arange(0, len(water_pots), step = 4))
plt.xticks(py.arange(start= 0, stop=40, step = 1))
plt.legend( ["Days with Water", "Days with Growth"])
plt.show()


##KRUSKAL-WALLIS TESTS##
#code example from https://www.statology.org/kruskal-wallis-test-python/
from scipy import stats
import pandas as pd

#read in data w appropriate sheet and columns selected, make dataFrame
results = pd.read_excel(r"C:\Users\terra\OneDrive\Documents\UB_Documents\Classes\2024_Spring_ENVS_490_Capstone\Aeroponic_Project_Conditions_Results_Got_Plants_and_Water.xlsx",
                        sheet_name="Results",
                        usecols=["Gross Growth Mass",
                                 "Net Growth",
                                 "Growth per Pot",
                                 "Gross Dry Mass",
                                 "Net Dry Mass",
                                 "Dry Mass per Pot"])
Results_df = pd.DataFrame(results)

##set up the three samples for each variable at EC = 0, 0.8, 1.6

#Gross Growth Mass
EC0_GGM = Results_df["Gross Growth Mass"][0:3] #Gross Growth Mass (GGM) at EC = 0
EC8_GGM = Results_df["Gross Growth Mass"][3:7] #Gross Growth Mass (GGM) at EC = 0.8
EC16_GGM = Results_df["Gross Growth Mass"][6:10] #Gross Growth Mass (GGM) at EC = 1.6
GGM_KWT = stats.kruskal(EC0_GGM, EC8_GGM, EC16_GGM)

#Net Wet Growth
EC0_NWG = (Results_df["Net Growth"][0:3]) #Net Wet Growth (NWG) at EC = 0
EC8_NWG = Results_df["Net Growth"][3:7] #Net Wet Growth (NWG) at EC = 0.8
EC16_NWG = Results_df["Net Growth"][6:10] #Net Wet Growth (NWG) at EC = 1.6
NWG_KWT = stats.kruskal(EC0_NWG, EC8_NWG, EC16_NWG)

#Growth Per Pot
EC0_GPP = Results_df["Growth per Pot"][0:3] #Growth per Pot (GPP) at EC = 0
EC8_GPP = Results_df["Growth per Pot"][3:7] #Growth per Pot (GPP) at EC = 0.8
EC16_GPP = Results_df["Growth per Pot"][6:10] #Growth per Pot (GPP) at EC = 1.6
GPP_KWT = stats.kruskal(EC0_GPP, EC8_GPP, EC16_GPP)

#Gross Dry Mass
EC0_GDM = Results_df["Gross Dry Mass"][0:3] #Gross Dry Mass (GDM) at EC = 0
EC8_GDM = Results_df["Gross Dry Mass"][3:7] #Gross Dry Mass (GDM) at EC = 0.8
EC16_GDM = Results_df["Gross Dry Mass"][6:10] #Gross Dry Mass (GDM) at EC = 1.6
GDM_KWT = stats.kruskal(EC0_GDM, EC8_GDM, EC16_GDM)

#Net Dry Mass
EC0_NDM = Results_df["Net Dry Mass"][0:3] #Net Dry Mass (NDM) at EC = 0
EC8_NDM = Results_df["Net Dry Mass"][3:7] #Net Dry Mass (NDM) at EC = 0.8
EC16_NDM = Results_df["Net Dry Mass"][6:10] #Net Dry Mass (NDM) at EC = 1.6
NDM_KWT = stats.kruskal(EC0_NDM, EC8_NDM, EC16_NDM)

#Dry Mass per Pot
EC0_DMPP = Results_df["Gross Dry Mass"][0:3] #Dry Mass per Pot (DMPP) at EC = 0
EC8_DMPP = Results_df["Gross Dry Mass"][3:7] #Dry Mass per Pot (DMPP) at EC = 0.8
EC16_DMPP = Results_df["Gross Dry Mass"][6:10] #Dry Mass per Pot (DMPP) at EC = 1.6
DMPP_KWT = stats.kruskal(EC0_DMPP, EC8_DMPP, EC16_DMPP)

#printing all the tests
print(f'gross growth mass: {GGM_KWT}')
print(f'net growth: {NWG_KWT}')
print(f'growth per pot: {GPP_KWT}')
print(f'gross dry mass: {GDM_KWT}')
print(f'net dry mass: {NDM_KWT}')
print(f'dry mass per pot: {DMPP_KWT}')



