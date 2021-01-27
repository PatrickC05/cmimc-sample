file = 'mmsd3.in'
out = 'mmsd3.out'
from dijkstar import Graph, find_path
def get_min(K):
    if K == 1:
        return 1
    graph = Graph()
    for i in range(K):
        graph.add_edge(i,(i+1)%K,1)
        graph.add_edge(i,(10*i)%K,0)
    path = find_path(graph,1,0)
    nodes = path.nodes
    costs = path.costs
    num = 1
    print(done)
    for i in costs:
        if i == 0:
            num *=10
        else:
            num +=1
    return num//K
with open(file, 'r') as f:
    f.readline()
    with open(out, 'w') as o:
        for line in f:
            print(line)
            o.write(str(get_min(int(line)))+'\n')
