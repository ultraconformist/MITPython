# 6.0002 Problem Set 5
# Graph optimization
# Name: Morgan

#
# Finding shortest paths through MIT buildings
#
import unittest
from graph import Digraph, Node, WeightedEdge

#
# Problem 2: Building up the Campus Map
#
# Problem 2a: Designing your graph
#
# What do the graph's nodes represent in this problem? What
# do the graph's edges represent? Where are the distances
# represented?
#
# Answer:
# The nodes in this problem are the buildings on campus;
# the edges are the paths between the buildings.
# The distances are, color-coded, the meters of distance it will take to travel
# from one building to another, with the blue numbers showing total distance,
# and the green numbers showing distance spent outdoors. (Thus, logically, the
# distance traveled indoors = total_distance - outdoor-distance.)


# Problem 2b: Implementing load_map
def load_map(map_filename):
    """
    Parses the map file and constructs a directed graph

    Parameters:
        map_filename : name of the map file

    Assumes:
        Each entry in the map file consists of the following four positive
        integers, separated by a blank space:
            From To TotalDistance DistanceOutdoors
        e.g.
            32 76 54 23
        This entry would become an edge from 32 to 76.

    Returns:
        a Digraph representing the map
    """
    map_file = open(map_filename, 'r')
    map_list = map_file.read().lower().splitlines()
    loaded_map = Digraph()
    for edge in map_list:
        edge_list = edge.split()
        node_a = Node(edge_list[0])
        node_b = Node(edge_list[1])
        total_dist = int(edge_list[2])
        outdoor_dist = int(edge_list[3])
        if not loaded_map.has_node(node_a):
            loaded_map.add_node(node_a)
        if not loaded_map.has_node(node_b):
            loaded_map.add_node(node_b)
        edge_temp = WeightedEdge(node_a, node_b, total_dist, outdoor_dist)
        loaded_map.add_edge(edge_temp)
    print("Loading map from file...")
    map_file.close()
    return loaded_map
# Problem 2c: Testing load_map
# Include the lines used to test load_map below, but comment them out
#test_map = load_map('test_load_map.txt')
#expected_string = 'a->b (5, 2)\na->c (5, 2)\nb->a (9, 4)\nb->c (3, 1)'
#print('Expecting:\n' + expected_string)
#print('Got:\n' + str(test_map))
#if expected_string == str(test_map):
#    print('Map loaded correctly.')
#else:
#    print('Map loaded incorrectly.')

#
# Problem 3: Finding the Shorest Path using Optimized Search Method
#
# Problem 3a: Objective function
#
# What is the objective function for this problem? What are the constraints?
#
# Answer:
# The objective function is to minimize the weighted sum of n edges from source
# to destination, thus sum of i to n X of i, where X is the weight of node i
# where the first i is the source and the final i is the destination node.
# 

# Problem 3b: Implement get_best_path
def get_best_path(digraph, start, end, path, max_dist_outdoors, best_dist,
                  best_path):
    """
    Finds the shortest path between buildings subject to constraints.

    Parameters:
        digraph: Digraph instance
            The graph on which to carry out the search
        start: string
            Building number at which to start
        end: string
            Building number at which to end
        path: list composed of [[list of strings], int, int]
            Represents the current path of nodes being traversed. Contains
            a list of node names, total distance traveled, and total
            distance outdoors.
        max_dist_outdoors: int
            Maximum distance spent outdoors on a path
        best_dist: int
            The smallest distance between the original start and end node
            for the initial problem that you are trying to solve
        best_path: list of strings
            The shortest path found so far between the original start
            and end node.

    Returns:
        A tuple with the shortest-path from start to end, represented by
        a list of building numbers (in strings), [n_1, n_2, ..., n_k],
        where there exists an edge from n_i to n_(i+1) in digraph,
        for all 1 <= i < k and the distance of that path.

        If there exists no path that satisfies max_total_dist and
        max_dist_outdoors constraints, then return None.
    """
    path = [path[0] + [start], path[1], path[2]]
    start_node = Node(start)
    end_node = Node(end)
    # if start and end are not valid nodes:
    #   raise an error
    if not (digraph.has_node(start_node) and digraph.has_node(end_node)):
        raise ValueError('Start or End node do not exist')
    # elif start and end are the same node:
    #   update the global variables appropriately
    elif start == end:
        return path
        
    # else:
    #   for all the child nodes of start
    #       construct a path including that node
    #       recursively solve the rest of the path, from the child node 
    #       to the end node
    for edge in digraph.get_edges_for_node(start_node):
        dest_str = str(edge.get_destination())   # Get destination node as str
        if dest_str not in path[0]:  #No cycles            
            updated_total_dist = path[1] + edge.get_total_distance()
            updated_total_outdoor = path[2] + edge.get_outdoor_distance()
            if best_path == None or updated_total_dist < best_dist:
                if updated_total_outdoor <= max_dist_outdoors:
                    path = [path[0], updated_total_dist, updated_total_outdoor]                    
                    updated_pathlist = get_best_path(digraph, dest_str, end, \
                                                 path, max_dist_outdoors, \
                                                 best_dist, best_path)
                    #print(updated_pathlist, 'updated pathlist')
                    # Backtrack and update the best path
                    if updated_pathlist != None:
                        #print(path, updated_pathlist)
                        best_path = updated_pathlist[0]
                        best_dist = updated_pathlist[1]
                        path[1] = path[1] - edge.get_total_distance()
                        path[2] = path[2] - edge.get_outdoor_distance()
                        
    return (best_path, best_dist, path[2])
    
# Problem 3c: Implement directed_dfs
def directed_dfs(digraph, start, end, max_total_dist, max_dist_outdoors):
    """
    Finds the shortest path from start to end using a directed depth-first
    search. The total distance traveled on the path must not
    exceed max_total_dist, and the distance spent outdoors on this path must
    not exceed max_dist_outdoors.

    Parameters:
        digraph: Digraph instance
            The graph on which to carry out the search
        start: string
            Building number at which to start
        end: string
            Building number at which to end
        max_total_dist: int
            Maximum total distance on a path
        max_dist_outdoors: int
            Maximum distance spent outdoors on a path

    Returns:
        The shortest-path from start to end, represented by
        a list of building numbers (in strings), [n_1, n_2, ..., n_k],
        where there exists an edge from n_i to n_(i+1) in digraph,
        for all 1 <= i < k

        If there exists no path that satisfies max_total_dist and
        max_dist_outdoors constraints, then raises a ValueError.
    """
    path = [[], 0, 0]
    best_path = None
    best_dist = max_total_dist
    solution = get_best_path(digraph, start, end, path, max_dist_outdoors,\
                  best_dist, best_path)
    if solution[0] != None and solution[1] <= max_total_dist:
        return solution[0]
    else:
        raise ValueError('No path that satisfies constraints')    


# ================================================================
# Begin tests -- you do not need to modify anything below this line
# ================================================================

class Ps2Test(unittest.TestCase):
    LARGE_DIST = 99999

    def setUp(self):
        self.graph = load_map("mit_map.txt")

    def test_load_map_basic(self):
        self.assertTrue(isinstance(self.graph, Digraph))
        self.assertEqual(len(self.graph.nodes), 37)
        all_edges = []
        for _, edges in self.graph.edges.items():
            all_edges += edges  # edges must be dict of node -> list of edges
        all_edges = set(all_edges)
        self.assertEqual(len(all_edges), 129)

    def _print_path_description(self, start, end, total_dist, outdoor_dist):
        constraint = ""
        if outdoor_dist != Ps2Test.LARGE_DIST:
            constraint = "without walking more than {}m outdoors".format(
                outdoor_dist)
        if total_dist != Ps2Test.LARGE_DIST:
            if constraint:
                constraint += ' or {}m total'.format(total_dist)
            else:
                constraint = "without walking more than {}m total".format(
                    total_dist)

        print("------------------------")
        print("Shortest path from Building {} to {} {}".format(
            start, end, constraint))

    def _test_path(self,
                   expectedPath,
                   total_dist=LARGE_DIST,
                   outdoor_dist=LARGE_DIST):
        start, end = expectedPath[0], expectedPath[-1]
        self._print_path_description(start, end, total_dist, outdoor_dist)
        dfsPath = directed_dfs(self.graph, start, end, total_dist, outdoor_dist)
        print("Expected: ", expectedPath)
        print("DFS: ", dfsPath)
        self.assertEqual(expectedPath, dfsPath)

    def _test_impossible_path(self,
                              start,
                              end,
                              total_dist=LARGE_DIST,
                              outdoor_dist=LARGE_DIST):
        self._print_path_description(start, end, total_dist, outdoor_dist)
        with self.assertRaises(ValueError):
            directed_dfs(self.graph, start, end, total_dist, outdoor_dist)

    def test_path_one_step(self):
        self._test_path(expectedPath=['32', '56'])

    def test_path_no_outdoors(self):
        self._test_path(
            expectedPath=['32', '36', '26', '16', '56'], outdoor_dist=0)

    def test_path_multi_step(self):
        self._test_path(expectedPath=['2', '3', '7', '9'])

    def test_path_multi_step_no_outdoors(self):
        self._test_path(
            expectedPath=['2', '4', '10', '13', '9'], outdoor_dist=0)

    def test_path_multi_step2(self):
        self._test_path(expectedPath=['1', '4', '12', '32'])

    def test_path_multi_step_no_outdoors2(self):
        self._test_path(
            expectedPath=['1', '3', '10', '4', '12', '24', '34', '36', '32'],
            outdoor_dist=0)

    def test_impossible_path1(self):
        self._test_impossible_path('8', '50', outdoor_dist=0)

    def test_impossible_path2(self):
        self._test_impossible_path('10', '32', total_dist=100)


if __name__ == "__main__":
    unittest.main()
