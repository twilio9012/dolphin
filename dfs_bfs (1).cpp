#include<bits/stdc++.h>
using namespace std;

class Graph {
    public:

    map<int, list<int>> adjlist;
    map<int, bool> visited, visited1;
    queue<int> q;

    void addEdge(int s, int d){
        adjlist[s].push_back(d);
        adjlist[d].push_back(s);
    }

    void dfs(int node){

        visited1[node] = true;

        cout<<node<<" ";

        for(int i : adjlist[node]){
            if(!visited1[i]){
                dfs(i);
            }
        }
    }

    void bfs(){
        if(q.empty()){
            return ;
        }

        int node = q.front();
        q.pop();

        cout<<node<<" ";

        for(int i : adjlist[node]){
            if(!visited[i]){
                visited[i] = true;
                q.push(i);
            }
        }
        bfs();
    }
};


int main(){
    Graph g;

    int n;
    cout<<"Enter total number of edges: ";
    cin>>n;

    for(int i = 0; i < n; i++){
        int a, b;
        cout<<"\nEnter nodes joining Edge: ";
        cin>>a>>b;
        g.addEdge(a, b);
        
    }


    int ch = 0;
   

    while(ch != 3){

    cout << "\nEnter \n 1 to perform DFS \n 2 to perform BFS \n 3 to exit";
    cin >> ch;

    switch(ch){
        case 1:
            cout << "\nDFS on the given graph is :";
            g.dfs(1);
            break;
        
        case 2:
            cout << "\nBFS on the given graph is: ";
            g.q.push(1);
            g.visited[1] = true;
            g.bfs();  
            break;
        
        case 3:
            ch = 3;
    }

    }
    return 0;
}