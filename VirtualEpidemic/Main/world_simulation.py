import random


def run_simulation(bobs_list, home_list, workplace_list, virus):

    bob_list = bobs_list
    home_list = home_list
    workplace_list = workplace_list
    virus = virus
    random_interations = 500

    # lists holding count of number of bobs in each state for each day
    healthy_count_list = []
    infected_count_list = []
    immune_count_list = []
    dead_count_list = []
    '''recovered_count_list = []'''

    # creates patient 0
    bob_list[0].infected = True
    bob_list[0].day_infected = 0

    simulation_running = True
    day = 0

    # iterates through days
    while simulation_running:

        # clears infection from bobs which have been infected for the length of pathogen duration
        for bob in bob_list:
            if bob.infected:
                if bob.day_infected + virus.v_duration == day:
                    bob.infected = False

                    # % chance of bobs dying after completing its infection duration
                    if random.randint(0, 100) < virus.mortality:
                        bob.dead = True

                    # surviving bobs are given immunity for set duration
                    else:
                        bob.recovered = True
                        bob.immune = True
                        bob.day_recovered = day

        # clears immunity from bobs which have been infected for the length of pathogen duration
        for bob in bob_list:
            if bob.immune:
                if bob.day_recovered + virus.i_duration == day:
                    bob.infected = False
                    bob.recovered = True
                    bob.immune = False

        # ???
        '''for bob in bob_list:
            if bob.immune:
                if bob.day_recovered + virus.i_duration == day:
                    bob.immune = False'''

        # creates a list containing all homes with an infected bob
        infected_homes = []
        for bob in bob_list:
            if bob.infected:
                for home in home_list:
                    if home.id == bob.id:
                        infected_homes.append(home)

        # for every bob sharing a home with an infected bob they are potentially infected
        for infected_home in infected_homes:
            for bob in bob_list:
                if bob.home_id == infected_home.id:
                    if not bob.infected and not bob.immune and not bob.dead:
                        if random.randint(0, 100) < virus.infectivity_indoors:
                            bob.infected = True
                            bob.recovered = False
                            bob.immune = False
                            bob.day_infected = day
        infected_homes.clear()

        # creates a list containing all workplaces with an infected bob
        infected_workplaces = []
        for bob in bob_list:
            if bob.infected:
                for workplace in workplace_list:
                    if workplace.id == bob.id:
                        infected_workplaces.append(workplace)

        # for every bob sharing a workplace with an infected bob they are potentially infected
        for infected_workplace in infected_workplaces:
            for bob in bob_list:
                if bob.work_id == infected_workplace.id:
                    if not bob.infected and not bob.immune and not bob.dead:
                        if random.randint(0, 100) < virus.infectivity_indoors:
                            bob.infected = True
                            bob.recovered = False
                            bob.immune = False
                            bob.day_infected = day
        infected_homes.clear()

        # Random Interactions
        completed_interactions = 0
        while completed_interactions < random_interations:

            bob_1 = None
            bob_2 = None

            choosing_bob_1 = True
            while choosing_bob_1:
                bob_1 = random.choice(bobs_list)
                if not bob_1.dead:
                    choosing_bob_1 = False

            choosing_bob_2 = True
            while choosing_bob_2:
                bob_2 = random.choice(bobs_list)
                if not bob_2.dead:
                    choosing_bob_2 = False

            if bob_1.infected and not bob_1.immune:
                if random.randint(0, 100) < virus.infectivity_outdoors:
                    current_bob_id = bob_2.id
                    for bob in bobs_list:
                        if bob.id == current_bob_id:
                            bob.infected = True
                            bob.recovered = False
                            bob.immune = False
                            bob.day_infected = day

            if bob_2.infected and not bob_2.immune:
                if random.randint(0, 100) < virus.infectivity_outdoors:
                    current_bob_id = bob_1.id
                    for bob in bobs_list:
                        if bob.id == current_bob_id:
                            bob.infected = True
                            bob.recovered = False
                            bob.immune = False
                            bob.day_infected = day

            completed_interactions += 1

        # increments day and ends simulation at specified day
        day += 1
        if day == 365:
            simulation_running = False

        # counts number of currently dead bobs
        dead_count = 0
        for bob in bob_list:
            if bob.dead:
                dead_count += 1

        # counts number of currently infected bobs
        infected_count = 0
        for bob in bob_list:
            if bob.infected:
                infected_count += 1

        '''
        # counts number of currently recovered bobs
        recovered_count = 0
        for bob in bob_list:
            if bob.recovered:
                recovered_count += 1
        '''

        # counts number of currently immune bobs
        immune_count = 0
        for bob in bob_list:
            if bob.immune:
                immune_count += 1

        # adds current days infected & immune count to their lists
        infected_count_list.append(infected_count)
        immune_count_list.append(immune_count)
        dead_count_list.append(dead_count)
        '''recovered_count_list.append(recovered_count)'''

        # calculates healthy bobs on current day & adds this to the list
        healthy_count = 1000 - infected_count - immune_count - dead_count
        healthy_count_list.append(healthy_count)

        print("\nDAY:" + str(day))
        print("INFECTED BOBS = " + str(infected_count) + "/1000")
        print("IMMUNE BOBS = " + str(immune_count) + "/1000")
        print("DEAD BOBS = " + str(dead_count) + "/1000")
        '''print("RECOVERED BOBS = " + str(recovered_count) + "/1000")'''

        # text output colours
        green = '\033[32m'
        red = '\033[31m'
        default = '\033[m'
        yellow = '\033[33m'

        # outputs all bob id's in colours representing their condition
        for bob in bob_list:

            # breaks lines for readability
            if bob.id == 45:
                print(" ")
            if bob.id == 90:
                print(" ")

            if bob.recovered:
                print(yellow + "#" + str(bob.id), default, end="")
                continue
            if bob.infected:
                print(red + "#" + str(bob.id), default, end="")
            else:
                print(green + "#" + str(bob.id), default, end="")

        if not simulation_running:
            print("\n")
            print("\nHEALTHY COUNT BY DAY - " + str(healthy_count_list))
            print("\nINFECTED COUNT BY DAY - " + str(infected_count_list))
            print("\nDEAD COUNT BY DAY - " + str(dead_count_list))
            '''print("\nRECOVERED COUNT BY DAY - " + str(recovered_count_list))'''

            return [healthy_count_list, infected_count_list, immune_count_list, dead_count_list]

