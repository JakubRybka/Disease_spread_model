# Disease spread model
I have implemented susceptible-infected-removed model (SIR) which shows dynamics of epidemics in society with random graph approach.
## Society network modelling
Society is a collection of people, who have interaction between each other. In model people can be represented as nodes and interactions as edges connecting them. Real life society characterizes with high clustering as we tend to keep ourselves to goup of friends who also are friends to each other. However we also meet a lot of people that are in other clusters of people and are not familiar with our acquaintances. Example of such society may be a village, where you interact with your neighbours and your neighbours interact with each other, but you also interact with people from another neighbourhood who don't interact with people in your neighbourhood. Good depiction of such society is Watts-Strogatz model.

There is also property of society which describes how many people seperates you from any other chosen at random person. It is average shortest path and in real society it have been shown that it is about 6 steps to get every other man.
## Watts-Strogatz model
It is random graph generation model, which allows generation of networks with high clustering, while allowing the shortest average path to be accurate. 
Generation random network using framework provided by this model consists of two steps:
* Initialization: generate graph where each node has $k$ neighbours resulting in circular like network (for $k=2$: node 5 is connected to nodes 3,4,6 and 7, node 6 is connected to 4,5,7 and 8 etc.).
* Evolution: each edge connecting two nodes with probability $\beta$ will change one of the nodes.

