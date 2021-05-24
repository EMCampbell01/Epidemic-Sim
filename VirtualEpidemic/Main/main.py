from Main import world_builder as wb
from Main import world_simulation as ws
from Main import Visualization as Vz

# Default world attributes
population = 1000
home_count = 250
work_count = 125
home_size = 4
work_size = 8

# Default pathogen attributes
indoor_infectivity = 2
outdoor_infectivity = 2
p_duration = 14
i_duration = 32
mortality = 10

# Generates instance of default pathogen
pathogen = wb.Pathogen("Default Pathogen", indoor_infectivity, outdoor_infectivity, p_duration, i_duration, mortality)

Vz.startup()  # Print title

# Option to use default / configure settings
answer = input("Use default settings? ")
use_default = None

# Use default settings
if "Y" in answer or "y" in answer:
    use_default = True
    print("Using Default Settings!")

# Configure custom settings
if "N" in answer or "n" in answer:
    use_default = False
    print("Configure Custom Settings!\n")

if not use_default:

    # Set world attributes
    print("Configure Environment:")
    population = int(input("Population = "))
    home_count = int(input("Home Count = "))
    work_count = int(input("Work Count = "))
    home_size = int(input("Home Size = "))
    work_size = int(input("Work Size = "))

    # Set pathogen attributes
    print("\nConfigure Pathogen:")
    pathogen.name = input("Pathogen Name = ")
    indoor_infectivity = int(input("Indoor Infectivity % = "))
    outdoor_infectivity = int(input("Outdoor Infectivity % = "))
    p_duration = int(input("Infection Duration = "))
    i_duration = int(input("Immunity Duration = "))
    mortality = int(input("Mortality % = "))

# Generate world, population and virus according to selected attributes
home_list = wb.build_homes(home_count)
workplace_list = wb.build_workplaces(work_count)
pop_list = wb.build_pops(population, home_size, work_size)

# Runs the virtual epidemic and returns a list containing generated data
daily_data_lists = (ws.run_simulation(pop_list, home_list, workplace_list, pathogen))

# Plots and visualizes data
Vz.visualization(daily_data_lists, pathogen.name)
Vz.line_visualization(daily_data_lists)

