import matplotlib.pyplot as plt


# Plots and displays a stack graph showing the health status of the population
def visualization(data, v_name):

    # Aesthetic attributes
    colours = ["green", "lime", "red", "black"]
    plt.tight_layout()
    plt.style.use("fivethirtyeight")

    # Data presentation
    plt.title("Simulated Transmission Of " + v_name)
    labels = ["Healthy", "Immune", "Infected", "dead"]
    plt.xlabel("Days")
    plt.ylabel("Population")

    # Construct and display stack graph
    plt.stackplot(range(730), data[0], data[2], data[1], data[3], labels=labels, colors=colours)
    plt.show()


# Plots and displays line graphs showing total cases and deaths
def line_visualization(data):

    plt.title("Cases & Deaths")
    plt.plot(data[3], color="black")
    plt.plot(data[1], color="red")
    plt.show()


# Prints Title
def startup():

    print("")
    print("|]   [|   [][|][]    [][][]|   [][|][]   []   []    []|[]    []")
    print("|]   [|     [|]      []   [|     [|]     []   []   []   []   []")
    print("[]   []     [|]      [][]]       [|]     []   []   [][|][]   []")
    print(" [] []      [|]      []  []      [|]     []   []   []   []   []")
    print("  [|]     [][|][]    []   [|     [|]     [][|][]   []   []   [][][]| ")
    print("")
    print("|[][][]   |[][][]   [][|][]   [][]|     |[][][]   []\   /[]   [][|][]   |[][][]")
    print("|]        |]   []     [|]     []|  []   |]        [] \ / []     [|]     |] ")
    print("|[][][]   |[][][]     [|]     []|  []   |[][][]   []  '  []     [|]     |]")
    print("|]        |]          [|]     []|  []   |]        []     []     [|]     |]")
    print("|[][][]   |]        [][|][]   [][]|     |[][][]   []     []   [][|][]   |[][][]")
    print("")

