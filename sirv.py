import argparse
import networkx as nx
import matplotlib.pyplot as plt
import random
import numpy as np


class Network:
    def __init__(self, number_of_nodes):
        self.N = number_of_nodes
        nodes = [i+1 for i in range(number_of_nodes)]
        self.G = nx.Graph()
        self.G.add_nodes_from(nodes)
        edges = [(i, i+1) for i in range(1, number_of_nodes)] + [(i, i + 2) for i in range(1, number_of_nodes - 1)]
        edges += [(number_of_nodes, 1), (number_of_nodes, 2), (number_of_nodes - 1, 1)]
        self.G.add_edges_from(edges)

    def small_word(self, beta):
        for edge in list(self.G.edges):
            prob = random.random()
            if prob < beta:
                node1 = edge[0]
                while True:
                    node2 = random.choice(list(self.G.nodes))
                    if node2 not in edge and (node1, node2) not in self.G.edges and (node2, node1) not in self.G.edges:
                        break
                self.G.remove_edge(*edge)
                self.G.add_edge(node1, node2)

def main():
    parser = argparse.ArgumentParser(description="SIRV Watts-Strogatz Network Simulation")
    parser.add_argument("--T", type=int, default=1000, help="Total simulation time")
    parser.add_argument("--L", type=int, default=50, help="Number of simulations")
    parser.add_argument("--N", type=int, default=500, help="Size of Society")
    parser.add_argument("--beta", type=float, default=0.1, help="Rewiring probability for Watts-Strogatz network")
    parser.add_argument("--v", type=float, default=0.004, help="Vaccination probability")
    parser.add_argument("--R", type=float, default=0.05, help="Recovery probability")
    parser.add_argument("--gamma", type=float, default=0.1, help="Infection probability")
    parser.add_argument("--ill_start", type=int, default=1, help="Initial number of infected")
    parser.add_argument("--vaccinated_start", type=int, default=0, help="Initial number of vaccinated")

    args = parser.parse_args()

    T = args.T
    L = args.L
    N = args.N
    beta = args.beta
    v = args.v
    R = args.R
    gamma = args.gamma
    ill_start = args.ill_start
    vaccinated_start = args.vaccinated_start

    ill_dist_all = []
    rec_dist_all = []
    s_dist_all = []
    vac_dist_all = []
    t_values_all = []

    for l in range(L):
        network = Network(N)
        network.small_word(beta)
        n_x = {node: list(network.G.neighbors(node)) for node in network.G.nodes()}
        Sx = [0] * N
        nodes = list(network.G.nodes)
        ill_at_the_beginning = random.sample(nodes, ill_start)
        nodes_no_ill = list(set(nodes) - set(ill_at_the_beginning))
        vacc_at_the_beginning = random.sample(nodes_no_ill, vaccinated_start)

        for node in ill_at_the_beginning:
            Sx[node-1] = 1
        for node in vacc_at_the_beginning:
            Sx[node-1] = 2

        t = 0
        ill_dist = []
        vac_dist = []
        rec_dist = []
        s_dist = []
        t_values = []

        while t <= T:
            ill_agent = [node for node in nodes if Sx[node-1] == 1]
            ill = sum(1 for agent in Sx if agent == 1)
            ill_dist.append(ill)
            rec = sum(1 for agent in Sx if agent == -1)
            rec_dist.append(rec)
            health_agent = [node for node in nodes if Sx[node-1] == 0]
            s = sum(1 for agent in Sx if agent == 0)
            s_dist.append(s)
            vaccinated = sum(1 for agent in Sx if agent == 2)
            vac_dist.append(vaccinated)
            t_values.append(t)

            for y in health_agent:
                rx = random.uniform(0, 1)
                if rx < v:
                    Sx[y-1] = 2

            for x in ill_agent:
                r1 = random.uniform(0, 1)
                if r1 < R:
                    Sx[x-1] = -1
                else:
                    kx = n_x[x]
                    for neighbor in kx:
                        if Sx[neighbor-1] == 0:
                            r2 = random.uniform(0, 1)
                            if r2 < gamma:
                                Sx[neighbor-1] = 1
            t += 1

        ill_dist_all.append(ill_dist)
        rec_dist_all.append(rec_dist)
        s_dist_all.append(s_dist)
        vac_dist_all.append(vac_dist)
        t_values_all.append(t_values)

    average_ill_dist = np.mean(ill_dist_all, axis=0)
    average_rec_dist = np.mean(rec_dist_all, axis=0)
    average_s_dist = np.mean(s_dist_all, axis=0)
    average_vac_dist = np.mean(vac_dist_all, axis=0)
    average_t_values = np.mean(t_values_all, axis=0)

    plt.plot(average_t_values, average_ill_dist, label="I", color='red')
    plt.plot(average_t_values, average_rec_dist, label="R", color='blue')
    plt.plot(average_t_values, average_s_dist, label="S", color='green')
    plt.plot(average_t_values, average_vac_dist, label="V", color='black')
    plt.xlabel("Time")
    plt.ylabel("Number of agents")
    plt.grid()
    plt.legend()
    plt.title("SIRV Simulation on Small-World Network")
    plt.show()

if __name__ == "__main__":
    main()
