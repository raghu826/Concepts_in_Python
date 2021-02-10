class Graph:
    def __init__(self, connections):
        self.connections = connections
        self.graph_dict = {}    # converting routes to dictionary
        for start, end in connections:                  # starting n destination in edge
            if start in self.graph_dict:                # dict[key] = value
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]
        print("Graph Dict:", self.graph_dict)

    def get_paths(self, start, end, path=[]):
        path = path + [start]

        if start == end:
            return [path]

        if start not in self.graph_dict:
            return []

        paths = []
        for node in self.graph_dict[start]:         # node represents pune n surat  for mumbai
            if node not in path:
                new_paths = self.get_paths(node, end, path)   # recursion
                for p in new_paths:
                    paths.append(p)

        return paths

    def get_shortest_path(self, start, end, path=[]):
        path = path + [start]

        if start == end:
            return path

        if start not in self.graph_dict:
            return None

        shortest_path = None
        for node in self.graph_dict[start]:
            if node not in path:
                sp = self.get_shortest_path(node, end, path)
                if sp:
                    if shortest_path is None or len(sp) < len(shortest_path):
                        shortest_path = sp

        return shortest_path


if __name__ == '__main__':
    routes = [
        ("Mumbai", "Pune"),
        ("Mumbai", "Surat"),
        ("Surat", "Bangaluru"),
        ("Pune", "Hyderabad"),
        ("Pune", "Mysuru"),
        ("Hyderabad", "Bangaluru"),
        ("Hyderabad", "Chennai"),
        ("Mysuru", "Bangaluru"),
        ("Chennai", "Bangaluru")
    ]
    route_graph = Graph(routes)         # instance of Graph

    start = "Mumbai"
    end = "Bangaluru"

    print(f"All paths between: {start} and {end}: ", route_graph.get_paths(start, end))
    print(f"Shortest path between {start} and {end}: ", route_graph.get_shortest_path(start, end))