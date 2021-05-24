import random

''' 
RUN SIMULATION

Requires lists containing pops, homes, workplaces used in the simulation and the pathogen

run_simulation returns a list of lists which contain the count of pops for each health status
While running the status of each pop id is output, identified by its colour

Begins by Infecting pop #0 (patient 0)
For every day infected pops have a chance of infecting pops which they share a home/workplace with
Daily random interactions are generated between randomly selected pops which potentially causes new infections
Before the next iteration of each day, the number of pops in each status is appended to their lists
On the start of each new day status's are cleared from pops who have been infected/immune for the specified duration
'''


def run_simulation(pop_list, home_list, workplace_list, virus):

    pops_list = pop_list
    home_list = home_list
    workplace_list = workplace_list
    virus = virus

    random_interactions = 100

    # lists holding count of number of bobs in each state for each day
    healthy_count_list = []
    infected_count_list = []
    immune_count_list = []
    dead_count_list = []

    # creates patient 0
    pops_list[0].infected = True
    pops_list[0].day_infected = 0

    simulation_running = True
    day = 0

    # iterates through days
    while simulation_running:

        # clears infection/immunity from pops after status duration has expired.
        # Chance of infected pops dying after duration of infection
        for pop in pops_list:
            if pop.infected:

                # removes infected status after duration is complete
                if pop.day_infected + virus.v_duration == day:
                    pop.infected = False

                    # % chance of bobs dying after completing its infection duration
                    if random.randint(0, 100) < virus.mortality:
                        pop.dead = True

                    # surviving bobs are given immunity for set duration
                    else:
                        pop.immune = True
                        pop.day_recovered = day
            if pop.immune:

                # removes immune status after duration is complete
                if pop.day_recovered + virus.i_duration == day:
                    pop.infected = False
                    pop.immune = False

        # creates a lists containing all homes and workplaces containing a currently infected pop
        infected_homes = []
        infected_workplaces = []
        for pop in pops_list:
            if pop.infected:
                for home in home_list:
                    if home.id == pop.home_id:
                        infected_homes.append(home)
                for workplace in workplace_list:
                    if workplace.id == pop.work_id:
                        infected_workplaces.append(workplace)

        # for every bob sharing a home with an infected bob they are potentially infected
        for infected_home in infected_homes:
            for pop in pops_list:
                if pop.home_id == infected_home.id:
                    if not pop.infected and not pop.immune and not pop.dead:
                        if random.randint(0, 100) < virus.infectivity_indoors:
                            pop.infected = True
                            pop.immune = False
                            pop.day_infected = day
        infected_homes.clear()

        # for every bob sharing a workplace with an infected bob they are potentially infected
        for infected_workplace in infected_workplaces:
            for pop in pops_list:
                if pop.work_id == infected_workplace.id:
                    if not pop.infected and not pop.immune and not pop.dead:
                        if random.randint(0, 100) < virus.infectivity_indoors:
                            pop.infected = True
                            pop.immune = False
                            pop.day_infected = day
        infected_homes.clear()

        # Generates random outside interactions that have a chance of creating new infections
        completed_interactions = 0
        while completed_interactions < random_interactions:

            # Holds pops in the interaction
            pop_1 = None
            pop_2 = None

            # Randomly chooses a pop that is not dead
            choosing_pop_1 = True
            while choosing_pop_1:
                pop_1 = random.choice(pops_list)
                if not pop_1.dead:
                    choosing_pop_1 = False

            # Randomly chooses a pop that is not dead or pop_1
            choosing_pop_2 = True
            while choosing_pop_2:
                pop_2 = random.choice(pops_list)
                if not pop_2.dead and pop_2.id != pop_1.id:
                    choosing_pop_2 = False

            # Chance of infecting pop_2 if pop_1 is infected
            if pop_1.infected and not pop_2.immune:
                if random.randint(0, 100) < virus.infectivity_outdoors:
                    current_pop_id = pop_2.id
                    for pop in pops_list:
                        if pop.id == current_pop_id:
                            pop.infected = True
                            pop.immune = False
                            pop.day_infected = day

            # Chance of infecting pop_1 if pop_2 is infected
            if pop_2.infected and not pop_1.immune:
                if random.randint(0, 100) < virus.infectivity_outdoors:
                    current_pop_id = pop_1.id
                    for pop in pops_list:
                        if pop.id == current_pop_id:
                            pop.infected = True
                            pop.immune = False
                            pop.day_infected = day

            completed_interactions += 1

        # increments day and ends simulation at specified day
        day += 1
        if day == 730:
            simulation_running = False

        # counts number of currently dead, infected and immune bobs
        dead_count = 0
        infected_count = 0
        immune_count = 0
        for pop in pops_list:
            if pop.dead:
                dead_count += 1
            if pop.infected:
                infected_count += 1
            if pop.immune:
                immune_count += 1

        # adds current days infected & immune count to their lists
        infected_count_list.append(infected_count)
        immune_count_list.append(immune_count)
        dead_count_list.append(dead_count)

        # calculates healthy bobs on current day & adds this to the list
        healthy_count = 1000 - infected_count - immune_count - dead_count
        healthy_count_list.append(healthy_count)

        print("\nDAY:" + str(day))
        print("INFECTED BOBS = " + str(infected_count) + "/1000")
        print("IMMUNE BOBS = " + str(immune_count) + "/1000")
        print("DEAD BOBS = " + str(dead_count) + "/1000")

        # text output colours
        green = '\033[32m'  # green is used to display infected pops
        red = '\033[31m'    # red is used to show infected pops
        blue = '\033[96m'   # blue is used to show immune pops
        default = '\033[m'

        # outputs all bob id's in colours representing their condition
        for pop in pops_list:

            if pop.infected:
                print(red + " #" + str(pop.id), default, end="")
                continue
            if pop.immune:
                print(blue + " #" + str(pop.id), default, end="")
                continue
            if pop.dead:
                print(" #" + str(pop.id), end="")
                continue
            else:
                print(green + " #" + str(pop.id), default, end="")

        if not simulation_running:
            print("\n")
            print("\nHEALTHY COUNT BY DAY - " + str(healthy_count_list))
            print("\nINFECTED COUNT BY DAY - " + str(infected_count_list))
            print("\nIMMUNE COUNT BY DAY - " + str(immune_count_list))
            print("\nDEAD COUNT BY DAY - " + str(dead_count_list))

            return [healthy_count_list, infected_count_list, immune_count_list, dead_count_list]

