# VIRTUAL EPIDEMIC

Simulates the spread of a customizable pathogen within a customizable environment and visualizes the result. 

Constructs an enviroment populated with "pops", each represent an individual.
Pops are assigned a household & workplace.
A single pop is infected with a customizable pathogen which spreads throughout the population over the duration of 2 years.
Everyday infected pops have a chance of passing the pathogen to pops within their household and workplace.
A specified number (Hardcoded as of now) of random interactions take place daily, with the possibility of creating new infections.
After duration of infection pops have a % chance of dying, essentially removing them from the simulation.
If a infected pop does not die, they can become immune for a specified duration.

World and pathogen attributes are customizable. (Can result in error with invalid input)

Customizable attribues include:

Population =             Total number of pops

Home Count  =            Number of homes

Work Count =             Number of workplaces

Home Size   =            Number of pops assigned to each home

Work Size   =            Number of pops assigned to each workplace

Pathogen   =             Name Name of the pathogen

Indoor Infectivity  =    % chance of infecting pops within a shared home or workplace

Outdoor Infectivity  =   % chance of infecting pops in random interactions

Infection Duration   =   Number of days a pop remains infected

Immunity duration   =    Number of days a pop remains immune infected duration

Mortality      =         % chance of pop dying after infected duration

Two graphs are generated with the produced data.

Firstly a stack graph showing the proportion of the population in diffrent health states over time 

(GREEN=HEALTHY, RED=INFECTED, LIME=IMMUNE, BLACK=DEAD)

Additionally a line graph showing the number of infected and dead over time


