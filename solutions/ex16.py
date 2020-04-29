'''
Given an undirected graph, determine if a cycle exists in the graph
'''


def find_cycle(graph):
    def helper(path, graph):
        print(path)
        if len(path) > 0:
            if path[0] in path[1:]:
                return True
            elif len(graph) == 0:
                return False
        for node in graph:
            path.append(node)
            if helper(path, graph[node]):
                return True
            else:
                path.pop(-1)
    return helper([], graph)


graph = {
        'a': {'a2': {}, 'a3':{}},
        'b': {'b2': {}},
        'c': {}
        }

print(find_cycle(graph))
# False
graph['c'] = graph
print(find_cycle(graph))
# True
