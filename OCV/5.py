import sys

class DisjointSet:
    def __init__(self, size: int):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, vertex: int) -> int:
        # Path compression using a concise Pythonic assignment loop
        path = []
        while vertex != self.parent[vertex]:
            path.append(vertex)
            vertex = self.parent[vertex]
        for node in path:
            self.parent[node] = vertex
        return vertex

    def union(self, vertex_a: int, vertex_b: int) -> bool:
        root_a, root_b = self.find(vertex_a), self.find(vertex_b)
        if root_a == root_b:
            return False
            
        if self.rank[root_a] < self.rank[root_b]:
            root_a, root_b = root_b, root_a
        self.parent[root_b] = root_a
        if self.rank[root_a] == self.rank[root_b]:
            self.rank[root_a] += 1
        return True

def calculate_mst_weight(num_vertices: int, edges: list[tuple[int, int, int]]) -> int:
    # Sort inline by the weight property (index 2 of the tuple)
    edges.sort(key=lambda edge: edge[2])
    
    dsu = DisjointSet(num_vertices)
    total_weight = 0
    edges_added = 0
    
    for u, v, w in edges:
        if dsu.union(u, v):
            total_weight += w
            edges_added += 1
            if edges_added == num_vertices - 1:
                break
                
    return total_weight

def main():
    input_tokens = sys.stdin.read().split()
    if not input_tokens:
        return
        
    tokens_iter = iter(input_tokens)
    v_count = int(next(tokens_iter))
    e_count = int(next(tokens_iter))
    
    # Process graph layout directly from stream iterator
    raw_nums = [int(x) for x in tokens_iter]
    edges = list(zip(raw_nums[0::3], raw_nums[1::3], raw_nums[2::3]))[:e_count]
    
    print(calculate_mst_weight(v_count, edges))

if __name__ == '__main__':
    main()
