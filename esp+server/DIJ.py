# Python program for Dijkstra's
# single source shortest
# path algorithm. The program
# is for adjacency matrix
# representation of the graph

from collections import defaultdict
from importlib.util import source_from_cache
import json
import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import db as bd
# Class to represent a graph


def run():
    cred = credentials.Certificate("serviceAccountKey.json")
    firebase_admin.initialize_app(cred)

    db = firestore.client()
    while True:
        class Graph:

            # A utility function to find the
            # vertex with minimum dist value, from
            # the set of vertices still in queue
            def minDistance(self, dist, queue, source):
                # Initialize min value and min_index as -1
                minimum = float("Inf")
                min_index = -1

                # from the dist array,pick one which
                # has min value and is till in queue
                for i in range(len(dist)):
                    if dist[i] < minimum and i in queue:
                        minimum = dist[i]
                        min_index = i
                return min_index

            # Function to print shortest path
            # from source to j
            # using parent array

            def printPath(self, parent, j, fp):

                # Base Case : If j is source
                if parent[j] == -1:
                    # print(j, end=" ")
                    fp.write(str(j) + " ")

                    return
                self.printPath(parent, parent[j], fp)
                # print(j, end=" ")
                fp.write(str(j) + " ")

            # A utility function to print
            # the constructed distance
            # array

            def printSolution(self, dist, parent, src):
                fp = open("path.txt", "w")
                fp1 = open("path.txt", "a")

                # print("Vertex \t\tDistance from Source\tPath")
                for i in [4, 5]:
                    if i == 4:
                        fp.write("\n%d --> %d,%d," % (src, i, dist[i]))
                        self.printPath(parent, i, fp1)
                        # print()
                    else:
                        fp1.write("\n%d --> %d,%d," % (src, i, dist[i]))
                        self.printPath(parent, i, fp1)

                fp.close()

            '''Function that implements Dijkstra's single source shortest path
            algorithm for a graph represented using adjacency matrix
            representation'''

            def dijkstra(self, graph, src):

                row = len(graph)
                col = len(graph[0])

                # The output array. dist[i] will hold
                # the shortest distance from src to i
                # Initialize all distances as INFINITE
                dist = [float("Inf")] * row

                # Parent array to store
                # shortest path tree
                parent = [-1] * row

                # Distance of source vertex
                # from itself is always 0
                dist[src] = 0

                # Add all vertices in queue
                queue = []
                for i in range(row):
                    queue.append(i)

                # Find shortest path for all vertices
                while queue:

                    # Pick the minimum dist vertex
                    # from the set of vertices
                    # still in queue
                    u = self.minDistance(dist, queue, src)

                    # remove min element
                    queue.remove(u)

                    # Update dist value and parent
                    # index of the adjacent vertices of
                    # the picked vertex. Consider only
                    # those vertices which are still in
                    # queue
                    for i in range(col):
                        '''Update dist[i] only if it is in queue, there is
                        an edge from u to i, and total weight of path from
                        src to i through u is smaller than current value of
                        dist[i]'''
                        if graph[u][i][0] and i in queue:
                            weight = graph[u][i][1] + graph[u][i][2]
                            if dist[u] + weight < dist[i]:
                                dist[i] = dist[u] + weight
                                parent[i] = u

                # print the constructed distance array
                self.printSolution(dist, parent, src)

        g = Graph()
        f = open('Weights.json')

        # returns JSON object as
        # a dictionary
        data = json.load(f)
        l = ['Karan\r\n', 'Urmil\r\n', 'Kumkum\r\n']
        # Closing file
        f.close()
        # print(data)
        temp = max(data.values())
        # print(temp)
        res = [key for key in data if data[key] == temp]
        # print("hehe", res)
        # print(res[0])
        if(res[0] == l[0]):
            source = 1
        elif(res[0] == l[1]):
            source = 2
        elif(res[0] == l[2]):
            source = 3

        print("src:", source)
        db_ref = db.collection("Nodes")
        room1 = db_ref.document("A-1").get().to_dict()
        room2 = db_ref.document("A-2").get().to_dict()
        room3 = db_ref.document("A-3").get().to_dict()
        r1 = list(room1.values())
        r2 = list(room2.values())
        r3 = list(room3.values())

        # [reachable,smoke, temp]
        graph = [[[1, 0, 0], [0, 0, 10], [1, 100, 100], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
                 [[0, 0, 0], [1, 0, 0], [1, r1[0]+r2[0], r1[1]+r2[1]],
                  [0, 0, 0], [1, 0, 0], [0, 0, 0]],
                 [[1, 1, 1], [1, r1[0]+r2[0], r1[1]+r2[1]], [1, 0, 0], [
                     1, r3[0]+r2[0], r3[1]+r2[1]], [0, 0, 0], [0, 0, 0]],
                 [[0, 0, 0], [0, 0, 0], [1, r3[0]+r2[0], r3[1]+r2[1]], [
                     1, 0, 0], [0, 0, 0], [1, 0, 0]],
                 [[0, 0, 0], [1, 0, 0], [0, 0, 0], [
                     0, 0, 0], [1, 0, 0], [0, 0, 0]],
                 [[0, 0, 0], [0, 0, 0], [0, 0, 0], [1, 0, 0], [0, 0, 0], [1, 0, 0]]]

        # Print the solution

        g.dijkstra(graph, source)

        time.sleep(5)
