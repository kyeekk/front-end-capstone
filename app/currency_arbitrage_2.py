from typing import Tuple, List
from math import log


class Arbitrage:
    currencies = ['JMD','USD', 'CAD', 'GBP', 'EUR', 'TTD', 'KYD', 'CHF']

    rates = [
        [1, 140.0167, 99.9917, 175.0981, 154.4037, 20.7681, 170.7521, 144.01687],
        [0.0106, 1, 0.71, 1.2412, 1.0826, 0.1516, 1.2091, 1.0345],
        [0.106, 1.4092, 1, 1.7469, 1.5289, 0.2128, 1.6843, 1.4453],
        [0.0058, 0.8137, 0.5844, 1, 0.876, 0.125, 0.9711, 0.8321],
        [0.0066, 0.9231, 0.6662, 1.1481, 1 , 0.1465, 1.1115, 0.9549],
        [0.0483, 6.6254, 4.6556, 8.8163, 7.3246, 1 , 8.1245, 6.9619],
        [0.006, 0.8325, 0.5833, 1.0349, 0.9026, 0.1230, 1 , 0.8614],
        [0.0070, 0.9732, 0.6971, 1.2036, 1.0564, 0.1462, 1.1762, 1]
    ]

    def negate_logarithm_convertor(self,graph: Tuple[Tuple[float]]) -> List[List[float]]:
        ''' log of each rate in graph and negate it'''
        result = [[-log(edge) for edge in row] for row in graph]
        return result


    def arbitrage(self,currency_tuple: tuple, rates_matrix: Tuple[Tuple[float, ...]]):
        ''' Calculates arbitrage situations and prints out the details of this calculations'''

        trans_graph = self.negate_logarithm_convertor(rates_matrix)

        # Pick any source vertex -- we can run Bellman-Ford from any vertex and get the right result

        source = 0
        n = len(trans_graph)
        min_dist = [float('inf')] * n

        pre = [-1] * n
        
        min_dist[source] = source

        # 'Relax edges |V-1| times'
        for _ in range(n-1):
            for source_curr in range(n):
                for dest_curr in range(n):
                    if min_dist[dest_curr] > min_dist[source_curr] + trans_graph[source_curr][dest_curr]:
                        min_dist[dest_curr] = min_dist[source_curr] + trans_graph[source_curr][dest_curr]
                        pre[dest_curr] = source_curr

        # if we can still relax edges, then we have a negative cycle
        for source_curr in range(n):
            for dest_curr in range(n):
                if min_dist[dest_curr] > min_dist[source_curr] + trans_graph[source_curr][dest_curr]:
                    # negative cycle exists, and use the predecessor chain to print the cycle
                    print_cycle = [dest_curr, source_curr]
                    # Start from the source and go backwards until you see the source vertex again or any vertex that already exists in print_cycle array
                    while pre[source_curr] not in  print_cycle:
                        print_cycle.append(pre[source_curr])
                        source_curr = pre[source_curr]    
                    print_cycle.append(pre[source_curr])
                    k = len(print_cycle)
                    if k> 3:
                        print ('\n', print_cycle)
                        print("Arbitrage Opportunity:")
                        print(" --> ".join([self.currencies[p] for p in print_cycle[::-1]]))

    def preamble(self,currencies, rates, x):
        index = currencies.index(x)
        if currencies[index] != currencies[len(currencies)-1]:
            print ('true')
            j = currencies[len(currencies)-1]
            currencies[len(currencies)-1] = currencies[index]
            currencies[index] = j
            print(currencies)
            print (rates[index])
            print (rates)
            i = rates[len(rates)-1]
            rates[len(rates)-1] = rates[index]
            rates[index] = i
            print(rates)
        self.arbitrage(currencies, rates)

    def run(self,x):
        self.preamble(self.currencies, self.rates, x)
        


##if __name__ == "__main__":
##    x =  input("Enter Source currency code: ")
##    #y =  input("Enter Destination currency code: ")
##    preamble(currencies, rates, x)
    
    
# Time Complexity: O(N^3)
# Space Complexity: O(N^2)
