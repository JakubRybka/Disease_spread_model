# Disease spread model
I have implemented susceptible-infected-removed with vaccination model (SIRV) which shows dynamics of epidemics in society with random graph approach.
## Society network modelling
Society is a collection of people, who have interaction between each other. In model people can be represented as nodes and interactions as edges connecting them. Real life society characterizes with high clustering as we tend to keep ourselves to goup of friends who also are friends to each other. However we also meet a lot of people that are in other clusters of people and are not familiar with our acquaintances. Example of such society may be a village, where you interact with your neighbours and your neighbours interact with each other, but you also interact with people from another neighbourhood who don't interact with people in your neighbourhood. Good depiction of such society is Watts-Strogatz model.

There is also property of society which describes how many people seperates you from any other chosen at random person. It is average shortest path and in real society it have been shown that it is about 6 steps to get every other man.
### Watts-Strogatz model
It is random graph generation model, which allows generation of networks with high clustering, while allowing the shortest average path to be accurate. 
Generation random network using framework provided by this model consists of two steps:
* Initialization: generate graph where each node has $k$ neighbours resulting in circular like network (for $k=2$: node 5 is connected to nodes 3,4,6 and 7, node 6 is connected to 4,5,7 and 8 etc.).
* Evolution: each edge connecting two nodes with probability $\beta$ will change one of the nodes.

Initialized network             |  Evolved Network ($\beta = 0.2$)
:-------------------------:|:-------------------------:
![Obraz1](https://github.com/user-attachments/assets/2309d1cc-82ed-44f0-b346-cd44c928a288)  |  ![Obraz2](https://github.com/user-attachments/assets/d1857bd6-e019-4d4f-ad52-898a3cebf307)

## SIRV model
SIRV depicts how epidemy of some illness evolves in time. Given contagiousness and recovery rate one can predict how will the dynamics proceed. This will also depend on how dense society is.

## Visualization

The final output is a plot showing the number of:
- Susceptible (S)
- Infected (I)
- Recovered (R)
- Vaccinated (V)  
... agents over time.

---

### Exemplary output:

![Figure_1](https://github.com/user-attachments/assets/c1c2275f-6022-40b3-bcc5-5072bc0fd343)


## Requirements

Install the required Python packages:

```bash
pip install networkx matplotlib numpy
```

### Available Arguments

| Argument              | Type    | Default | Description                                     |
|-----------------------|---------|---------|-------------------------------------------------|
| `--T`                 | int     | `1000`  | Total simulation time                           |
| `--L`                 | int     | `50`    | Number of simulation runs (to average)          |
| `--N`                 | int     | `500`   | Number of nodes (agents) in the network         |
| `--beta`              | float   | `0.1`   | Rewiring probability for small-world network    |
| `--v`                 | float   | `0.004` | Probability of vaccination for healthy agents   |
| `--R`                 | float   | `0.05`  | Probability of recovery                         |
| `--gamma`             | float   | `0.1`   | Probability of infection per contact            |
| `--ill_start`         | int     | `1`     | Number of initially infected agents             |
| `--vaccinated_start`  | int     | `0`     | Number of initially vaccinated agents           |

### Example

```bash
python sirv_simulation.py --T 500 --N 300 --L 20 --beta 0.2 --v 0.01 --R 0.1 --gamma 0.2
```
