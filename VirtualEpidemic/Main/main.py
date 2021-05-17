from Main import world_builder as wb
from Main import world_simulation as ws
from Main import Visualization as Vz

# Default world attributes
bob_population = 1000
home_count = 250
work_count = 125
home_size = 4
work_size = 8

# Default pathogen attributes
indoor_infectivity = 10
outdoor_infectivity = 1
p_duaration = 20
i_duration = 32
mortality = 2

Vz.startup()

answer = input("Use default settings? ")
use_default = None

if "Y" in answer:
    use_default = True
    print("Using Default Settings!")

if "N" in answer:
    use_default = False
    print("Configure Custom Settings!\n")

if use_default == False:

    print("Configure Environment:")
    bob_population = int(input("Population = "))
    home_count = int(input("Home Count = "))
    work_count = int(input("Work Count = "))
    home_size = int(input("Home Size = "))
    work_size = int(input("Work Size = "))

    print("Configure Pathogen:")
    indoor_infectivity = int(input("Indoor Infectivity % = "))
    outdoor_infectivity = int(input("Outdoor Infectivity % = "))
    p_duaration = int(input("Infection Duration = "))
    i_duration = int(input("Immunity Duration = "))
    mortality = int(input("Mortality % = "))

bob_list = wb.summon_bobs(bob_population, home_size, work_size)
home_list = wb.build_homes(home_count)
workplace_list = wb.build_workplaces(work_count)

virus = wb.Pathogen("Default Pathogen", indoor_infectivity, outdoor_infectivity, p_duaration, i_duration, mortality)

daily_data_lists = (ws.run_simulation(bob_list, home_list, workplace_list, virus))

Vz.visualization(daily_data_lists, virus.name)
