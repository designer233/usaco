#include <bits/stdc++.h>
using namespace std;

bool arr[10000000];

int main() {

    int N, M;

    cin>> N;
    for (int x=0; x<N; x++) {
        string txt;
        cin>> txt;
        arr[stoi(txt)] = 1;
    }

    cin>> M;
    for (int x=0; x<M; x++) {
        string txt;
        cin>> txt;
        if (arr[stoi(txt)] == 1) {
            cout<< 1 << " ";
        }
        else {
            cout<< 0 << " ";
        }
    }

}
