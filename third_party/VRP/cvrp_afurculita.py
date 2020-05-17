from matplotlib import pyplot as plt
import numpy as np
from third_party.VRP.read_vrp import read_input_cvrp
import math

class Vehicle():
    def __init__(self, Q):
        '''
        Vehicle object that carries the goods
        :param Q: maximum number of items carried by the vehicle.
        '''
        self.Q = Q
        self.nodes = []
        self.load = 0
        self.currentNode = 0 # starting location is depot
    
    def addNode(self, customer):
        '''
        Add customer to vehicle route
        :param customer: Object of class Node
        '''
        self.nodes.append(customer)
        self.load += customer.demand
        self.currentNode = customer.id

    def checkConstraint(self, new):
        return self.load + new <= self.Q

class Node():
    def __init__(self, id, demand):
        self.id = id
        self.demand = demand
        self.isRouted = False

class Greedy_VRP():
    def __init__(self, vrp_file, n_vehicles=None):
        self.n_cust, self.cust_locations, Q, self.dist_matrix, self.dist_warehouse, demands = read_input_cvrp(vrp_file)
        if n_vehicles is None: n_vehicles = self.n_cust
        self.vehicles = [Vehicle(Q) for _ in range(n_vehicles)]
        self.nodes = [Node(i, demands[i]) for i in range(self.n_cust)]
        self.cost = 0

    def unassignedCustomerExists(self):
        for node in self.nodes:
            if not node.isRouted:
                return True
        return False
    
    def run(self):
        vehicle_id = 0

        while self.unassignedCustomerExists():
            custId = 0
            candidate = None
            minCost = math.inf

            if len(self.vehicles[vehicle_id].nodes) == 0:   # vehicle route is empty
                self.vehicles[vehicle_id].addNode(self.nodes[0])
                self.nodes[0].isRouted = True

            for i in range(self.n_cust):
                if not self.nodes[i].isRouted and self.vehicles[vehicle_id].checkConstraint(self.nodes[i].demand):
                    candCost = self.dist_matrix[self.vehicles[vehicle_id].currentNode, i]
                    if minCost > candCost:
                        minCost = candCost
                        custId = i
                        candidate = self.nodes[i]

            if candidate is None:       # if no customer fits the vehicle
                if vehicle_id + 1 < len(self.vehicles): # Still vehicles left to assign
                    if self.vehicles[vehicle_id].currentNode != 0:
                        endCost = self.dist_matrix[self.vehicles[vehicle_id].currentNode, 0]
                        self.vehicles[vehicle_id].addNode(self.nodes[0])
                        self.cost += endCost
                    vehicle_id += 1
                else:   # no more vehicles left, nut customers still exists. No solution can be found
                    raise Exception("A Solution cannot be found under the given constraints. Not enough vehicles to cater to all customers!")
            else:
                self.vehicles[vehicle_id].addNode(candidate)
                self.nodes[custId].isRouted = True
                self.cost += minCost

        endCost = self.dist_matrix[self.vehicles[vehicle_id].currentNode, 0]
        self.vehicles[vehicle_id].addNode(self.nodes[0])
        self.cost += endCost
        self.n_vehicles = vehicle_id +1
        return self.vehicles, self.cost
                        
    def __str__(self):
        if self.cost == 0:
            return "Optimization not run yet. Run by calling Greedy_VRP.run()."
        string = "=================================================================\n"
        for v_id in range(len(self.vehicles)):
            if len(self.vehicles[v_id].nodes) != 0:
                string += "Vehicle {}:\n\t".format(v_id)
                n_nodes = len(self.vehicles[v_id].nodes)
                for i in range(n_nodes):
                    if i == n_nodes - 1:
                        string += str(self.vehicles[v_id].nodes[i].id)
                    else:
                        string += '{}->'.format(self.vehicles[v_id].nodes[i].id)
                string += '\n'

        string += 'Best Cost: {}\n'.format(self.cost)
        return string

    def plot(self):
        plt.scatter(self.cust_locations[0, 0], self.cust_locations[0, 1], marker='*', c='r')
        plt.scatter(self.cust_locations[1:, 0], self.cust_locations[1:, 1], c='b')
        if self.cost == 0:
            print("Optimization not yet run. Run by calling Greedy_VRP.run().")
            return
        cmap = plt.cm.get_cmap('hsv', self.n_vehicles+1)
        for v_id in range(len(self.vehicles)):
            if len(self.vehicles[v_id].nodes) != 0:
                c = np.random.rand(3,)
                node_ids = [node.id for node in self.vehicles[v_id].nodes]
                lx, ly = self.cust_locations[node_ids, 0], self.cust_locations[node_ids, 1]
                plt.plot(lx.T, ly.T, c=cmap(v_id))
        plt.text(-0.05, -0.05, "Total distance=%.2f" % self.cost, fontdict={'size': 10, 'color': 'red'})
        plt.legend(['Vehicle {}'.format(i+1) for i in range(self.n_vehicles)]+['Depot', 'Customers'])
        plt.title('Greedy solution to CVRP')

