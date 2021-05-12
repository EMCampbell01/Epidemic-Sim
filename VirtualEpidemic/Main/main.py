from Main import world_builder as wb
from Main import world_simulation as ws
from Main import Visualization as Vz

print("VIRTUAL EPIDEMIC\n")

# World attributes
bob_population = 1000
home_count = 250
work_count = 125
home_size = 4
work_size = 8

# Pathogen attributes
h_infectivity = 10
w_infectivity = 10
p_duaration = 20
i_duration = 32
mortality = 2

bob_list = wb.summon_bobs(bob_population, home_size, work_size)
home_list = wb.build_homes(home_count)
workplace_list = wb.build_workplaces(work_count)

virus = wb.Pathogen("Bubonic Plague", h_infectivity, w_infectivity, p_duaration, i_duration, mortality)

daily_data_lists = (ws.run_simulation(bob_list, home_list, workplace_list, virus))

Vz.visualization(daily_data_lists)
