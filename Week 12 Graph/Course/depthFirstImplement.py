def depthFirst(graph, source):
    stack = [source]
    while stack:
        current = stack.pop()
        print(current)
        for i in graph[current]:
            stack.append(i)

def breadthFirst(graph, source):
    queue = [source]
    while queue:
        current = queue.pop()
        print(current)
        for i in graph[current]:
            queue.insert(0, i)


graph = {
    'a' : ['b', 'c'],
    'b' : ['d'],
    'c' : ['e'],
    'd' : ['f'],
    'e' : [],
    'f' : []
}
depthFirst(graph , 'a') #a c e b d f
print('*' * 18)
breadthFirst(graph, 'a') #a c b e d f     or  a b c d e f <
