#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <queue>
#include <algorithm>

using namespace std;

// Structs
struct NetworkResult {
    int number_of_components;
    int size_of_maximum_component;
};

// Problem
NetworkResult analyze_social_network(int N, const vector<vector<int>>& adj) {
    vector<bool> visited(N, false);
    int components_count = 0;
    int max_component_size = 0;

    for (int i = 0; i < N; ++i) {
        if (!visited[i]) {
            components_count++;
            int current_size = 0;
            
            queue<int> q;
            q.push(i);
            visited[i] = true;

            while (!q.empty()) {
                int curr = q.front();
                q.pop();
                current_size++;

                for (int neighbor : adj[curr]) {
                    if (!visited[neighbor]) {
                        visited[neighbor] = true;
                        q.push(neighbor);
                    }
                }
            }
            max_component_size = max(max_component_size, current_size);
        }
    }
    return {components_count, max_component_size};
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    string raw_input;
    if (!getline(cin, raw_input)) return 0;

    stringstream ss(raw_input);
    int N, M;
    if (!(ss >> N >> M)) return 0;

    vector<vector<int>> adj(N);
    int edges_read = 0;

    while (edges_read < M && getline(cin, raw_input)) {
        if (raw_input.empty()) continue;
        stringstream edge_ss(raw_input);
        int u, v;
        if (edge_ss >> u >> v) {
            adj[u].push_back(v);
            adj[v].push_back(u);
            edges_read++;
        }
    }

    NetworkResult output = analyze_social_network(N, adj);
    cout << output.number_of_components << " " << output.size_of_maximum_component << "\n";

    return 0;
}
