import random


# Each instance of Bob represents a individual in the epidemic
class Bob():

    def __init__(self, bob_id, home_id, work_id, infected):
        self.id = bob_id             # holds the unique ID for each bob
        self.home_id = home_id       # holds the home ID that the bob is assigned to
        self.work_id = work_id       # holds the work ID that the bob is assigned to
        self.infected = infected     # holds boolean for if the bob is infected or not

    # holds days infected and recovered
    day_infected = 0
    day_recovered = 0

    # health status
    recovered = False
    immune = False
    dead = False


# The pathogen contains all of the specific attributes for the simulated epidemic
class Pathogen():

    def __init__(self, name, infectivity_home, infectivity_work, v_duration, i_duration, mortality):
        self.name = name                          # Name of the pathogen
        self.infectivity_home = infectivity_home  # % chance of infection on exposure at home
        self.infectivity_work = infectivity_work  # % chance of infection on exposure at work
        self.v_duration = v_duration              # duration of time which an individual remains infected/infectious
        self.i_duration = i_duration              # duration of time which an individual remains immune
        self.mortality = mortality                # % chance of dying from infection


class Household():

    def __init__(self, id):
        self.id = id
        self.bobs_inside = None
        self.bobs_infected = None


class Workplace():

    def __init__(self, id, bobs_inside):
        self.id = id
        self.bobs_inside = bobs_inside


def summon_bobs(num, h_size, w_size):
    bobs_population = num
    home_size = h_size
    work_size = w_size
    bobs_list = []

    building_world = True
    bobs_created = 0
    current_home = 0
    current_home_pop = 0
    current_work = 0
    current_work_pop = 0
    while building_world:
        if bobs_created != bobs_population:
            bobs_list.append(Bob(bobs_created, current_home, 0, False))
            bobs_created += 1

            if current_home_pop == home_size - 1:
                current_home = current_home + 1
                current_home_pop = 0
            else:
                current_home_pop = current_home_pop + 1

        else:
            random.shuffle(bobs_list)
            for bob in bobs_list:
                bob.work_id = current_work
                if current_work_pop == work_size - 1:
                    current_work = current_work + 1
                    current_work_pop = 0
                else:
                    current_work_pop = current_work_pop + 1

            bobs_list.sort(key=lambda x: x.id)
            building_world = False
    return bobs_list


def build_homes(num):
    home_number = num
    homes_list = []

    homes_built = 0
    while homes_built != home_number:
        homes_list.append(Household(homes_built))
        homes_built += 1
    return homes_list


def build_workplaces(num):
    workplace_number = num
    workplace_list = []

    workplaces_built = 0
    while workplaces_built != workplace_number:
        workplace_list.append(Household(workplaces_built))
        workplaces_built += 1
    return workplace_list
