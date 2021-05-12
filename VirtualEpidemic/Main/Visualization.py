import matplotlib.pyplot as plt


def visualization(data):

    # Aesthetic attributes
    colours = ["green", "lime", "red", "black"]
    plt.tight_layout()
    plt.style.use("fivethirtyeight")

    # Data presentation
    plt.title("Simulated Transmission")
    plt.legend()
    labels = ["Healthy", "Immune", "Infected", "dead"]
    plt.xlabel("Days")
    plt.ylabel("Population")

    # Construct and display stack graph
    plt.stackplot(range(365), data[0], data[2], data[1], data[3], labels=labels, colors=colours)
    plt.show()
