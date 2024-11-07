import matplotlib.pyplot as plt
import networkx as nx
import random
import datafile
"""
These are Function Headers
Complete the functions to ensure they return expected results
Replace these comments with documenation about the program
@author Jennie Lin
"""

def mybfs(G, source, target):
    """
    Return the searched edges as list of tuples
    """
    
    visited = {node: False for node in G.nodes}
    queue = [source]
    visited[source] = True
    ls = []
    while queue:
        cur_node = queue.pop(0)
        for node in sorted(G.neighbors(cur_node)):
          if not visited[node]:
              queue.append(node)
              visited[node] = True
              ls.append((cur_node, node))
          if node == target:
              queue = []
              break
    
    return ls
    
def mydfs(G, source, target):
    """
    Return the searched edges as list of tuples
    """
    nodes = [source]
    depth_limit = len(G)

    ls = []

    visited = set()
    for start in nodes:
        if start in visited:
            continue
        visited.add(start)
        stack = [(start, sorted(G.neighbors(start)))]
        depth_now = 1
        while stack:
            parent, children = stack[-1]
            for child in children:
                if child not in visited:
                    ls.append((parent, child))
                    if child == target:
                        stack = []
                        break
                    visited.add(child)
                    if depth_now < depth_limit:
                        stack.append((child, sorted(G.neighbors(child))))
                        depth_now += 1
                        break
            else:
                stack.pop()
                depth_now -= 1
    return ls

def myastar(G, source, target):
    """
    Return the list of nodes in the path and total cost like ([1,2,3],9)
    """
    def dist(a, b):
      (x1,y1) = (datafile.positions[a][0], datafile.positions[a][1])
      (x2,y2) = (datafile.positions[b][0], datafile.positions[b][1])
      return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    return (nx.astar_path(G, source, target, heuristic=dist, weight='weight'),nx.astar_path_length(G, source, target, heuristic=dist, weight='weight'))

def main():
    """
    Main body of your code below.
    """
    G = datafile.G
    positions = datafile.positions
    edges_weight = {(u,v): d['weight'] for u,v,d in G.edges(data=True)}
    
    # find final path funciton
    def finalPath(target, path_traversed):
        find = target
        ls = [target]
        for p in path_traversed[::-1]:
            if find == p[1]:
                ls.append(p[0])
                find = p[0]
        return ls
    
    # calculate final path's cost
    def finalCost(path):
        cost = 0
        for i in range(len(path)-1):
            if (path[i],path[i+1]) in edges_weight:
                cost += edges_weight[(path[i],path[i+1])]
            else:
                cost += edges_weight[(path[i+1],path[i])]
        return cost
    
    # print plot function
    def print_plot(title, method, path_traversed, final_path, final_cost, map_color = "lightblue", edge_color = "blue", finalPath_color = "green"):
        colors = [edge_color if (edge in path_traversed or (edge[1],edge[0]) in path_traversed) else map_color for edge in G.edges()]
        markers = [finalPath_color if node in final_path else map_color for node in G.nodes()]
        
        nx.draw(G, pos = positions, node_size = 1000, font_size = 6, edge_color = colors, node_color = markers, with_labels=True)
        plt.title(title+method)
        plt.grid(True)
        plt.get_current_fig_manager().canvas.set_window_title(title+method)
        plt.show() 
        # plt.savefig(title+method+".png", format="png")
        
        # show one with edge weight
        nx.draw(G, pos = positions, node_size = 1000, font_size = 6, edge_color = colors, node_color = markers, with_labels=True)
        nx.draw_networkx_edge_labels(G, pos=positions, edge_labels=edges_weight, font_size=6)
        plt.title(title+method)
        plt.figtext(0.5, 0.01, "Final Cost = " + str(final_cost), ha="center", fontsize=8)
        plt.grid(True)
        plt.get_current_fig_manager().canvas.set_window_title(title+method+"_weighted")
        plt.show() 
        # plt.savefig(title+method+"_weighted.png", format="png")
            
    # Connect Ballard to Columbia City
    source, target = "Ballard", "Columbia City"
    title = source + " to " + target + " - "
    bfs = mybfs(G, source, target)
    bfs_final = finalPath(target, bfs)
    dfs = mydfs(G, source, target)
    dfs_final = finalPath(target, dfs)
    astar = myastar(G, source, target)
    astar_path = [(astar[0][i],astar[0][i+1]) for i in range(len(astar[0])-1)]
    
    print_plot(title, "BFS", bfs, bfs_final, finalCost(bfs_final))
    print_plot(title, "DFS", dfs, dfs_final, finalCost(dfs_final))
    print_plot(title, "A*", astar_path, astar[0], astar[1])
    
    # Part 3 - Q4 reversing directions and going from Columbia City to Ballard
    title = target + " to " + source + " - "
    bfs = mybfs(G, target, source)
    bfs_final = finalPath(source, bfs)
    dfs = mydfs(G, target, source)
    dfs_final = finalPath(source, dfs)
    astar = myastar(G, target, source)
    astar_path = [(astar[0][i],astar[0][i+1]) for i in range(len(astar[0])-1)]
    
    print_plot(title, "BFS", bfs, bfs_final, finalCost(bfs_final))
    print_plot(title, "DFS", dfs, dfs_final, finalCost(dfs_final))
    print_plot(title, "A*", astar_path, astar[0], astar[1])
    
    # Connect West Seattle to Magnolia
    source, target = "West Seattle", "Magnolia"
    title = source + " to " + target + " - "
    bfs = mybfs(G, source, target)
    bfs_final = finalPath(target, bfs)
    dfs = mydfs(G, source, target)
    dfs_final = finalPath(target, dfs)
    astar = myastar(G, source, target)
    astar_path = [(astar[0][i],astar[0][i+1]) for i in range(len(astar[0])-1)]
    
    print_plot(title, "BFS", bfs, bfs_final, finalCost(bfs_final))
    print_plot(title, "DFS", dfs, dfs_final, finalCost(dfs_final))
    print_plot(title, "A*", astar_path, astar[0], astar[1])
    

### Do NOT remove the following lines of code
if __name__ == "__main__":
    main()