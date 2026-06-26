import sys
from collections import deque

def analyze_social_network(num_users: int, adj_list: list[list[int]]) -> tuple[int, int]:
    visited = [False] * num_users
    components_count = 0
    max_component_size = 0

    for user_id in range(num_users):
        if not visited[user_id]:
            components_count += 1
            current_size = 0
            
            # Pythonic inline BFS using a deque
            queue = deque([user_id])
            visited[user_id] = True

            while queue:
                current_user = queue.popleft()
                current_size += 1

                for neighbor in adj_list[current_user]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append(neighbor)

            max_component_size = max(max_component_size, current_size)

    return components_count, max_component_size

def main():
    input_tokens = sys.stdin.read().split()
    if not input_tokens:
        return
        
    tokens_iter = iter(input_tokens)
    n = int(next(tokens_iter))
    m = int(next(tokens_iter))

    # Pythonic list comprehension to initialize adjacency lists
    adj = [[] for _ in range(n)]
    
    for _ in range(m):
        try:
            u, v = int(next(tokens_iter)), int(next(tokens_iter))
            adj[u].append(v)
            adj[v].append(u)
        except StopIteration:
            break

    components, max_size = analyze_social_network(n, adj)
    print(f"{components} {max_size}")

if __name__ == '__main__':
    main()
