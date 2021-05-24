import random


# Each instance of Bob represents a individual in the epidemic
class Pop():

    def __init__(self, pop_id, home_id, work_id, infected):
        self.id = pop_id             # holds the unique ID for each bob
        self.home_id = home_id       # holds the home ID that the bob is assigned to
        self.work_id = work_id       # holds the work ID that the bob is assigned to
        self.infected = infected     # holds boolean for if the bob is infected or not

    # holds days infected and recovered
    day_infected = 0
    day_recovered = 0

    # health status
    immune = False
    dead = False


# The pathogen contains all of the specific attributes for the simulated epidemic
class Pathogen():

    def __init__(self, name, infectivity_indoors, infectivity_outdoors, v_duration, i_duration, mortality):
        self.name = name                                  # Name of the pathogen
        self.infectivity_indoors = infectivity_indoors    # % chance of infection on exposure at home
        self.infectivity_outdoors = infectivity_outdoors  # % chance of infection on exposure at work
        self.v_duration = v_duration                      # duration of time which an individual is infected/infectious
        self.i_duration = i_duration                      # duration of time which an individual is immune
        self.mortality = mortality                        # % chance of dying from infection


# Each instance of Household represents a home populated by pops
class Household():

    def __init__(self, id):
        self.id = id
        self.pops_inside = None
        self.bobs_infected = None


# Each instance of Workplace represents a workplace pops are designated to
class Workplace():

    def __init__(self, id, pops_inside):
        self.id = id
        self.pops_inside = pops_inside


'''
BUILD POPS

build_pops generates and returns a list of pops
pops are assigned to homes in chronological order and workplaces randomly
'''


def build_pops(population, h_size, w_size):
    pops_population = population
    home_size = h_size
    work_size = w_size
    pops_list = []

    building_world = True
    pops_created = 0
    current_home = 0
    current_home_pop = 0
    current_work = 0
    current_work_pop = 0
    while building_world:
        if pops_created != pops_population:
            pops_list.append(Pop(pops_created, current_home, 0, False))
            pops_created += 1

            if current_home_pop == home_size - 1:
                current_home = current_home + 1
                current_home_pop = 0
            else:
                current_home_pop = current_home_pop + 1

        else:
            random.shuffle(pops_list)
            for bob in pops_list:
                bob.work_id = current_work
                if current_work_pop == work_size - 1:
                    current_work = current_work + 1
                    current_work_pop = 0
                else:
                    current_work_pop = current_work_pop + 1

            pops_list.sort(key=lambda x: x.id)
            building_world = False
    return pops_list


# returns a list containing a specified number of homes
def build_homes(num):
    home_number = num
    homes_list = []

    homes_built = 0
    while homes_built != home_number:
        homes_list.append(Household(homes_built))
        homes_built += 1
    return homes_list


# returns a list containing a specified number of workplaces
def build_workplaces(num):
    workplace_number = num
    workplace_list = []

    workplaces_built = 0
    while workplaces_built != workplace_number:
        workplace_list.append(Household(workplaces_built))
        workplaces_built += 1
    return workplace_list
