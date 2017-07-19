#include <iostream>
#include <algorithm>
#include<vector>
#include<chrono>
#include<stdlib.h>
#include<time.h>
using namespace std;

int N = 10000000;
int * queensLocation = new int[N];
int * slopeQueens1 = new int[2*N];
int * slopeQueens2 = new int[2*N];
int queensConflictNum = 0;

void removeQueen(int x);
void addQueen(int x);
int myrandom (int i) { return rand()%i;}

void resetBoard(){
    cout<<"reset"<<endl;

    queensConflictNum = 0;
    for(int i = 0; i < 2 * N; i++){
        slopeQueens1[i] = 0;
        slopeQueens2[i] = 0;
    }
    vector<int> col_vector1;
    vector<int> col_vector2;
    for(int i = 0; i < N; i++)
        col_vector1.push_back(i);
    random_shuffle(col_vector1.begin(), col_vector1.end(), myrandom);

    int index = 0;
    int col;
    bool col1orcol2 = true;
    while(index < N - 100){
        if(col1orcol2){
            if(col_vector1.empty()){
                col1orcol2 = false;
                continue;
            }
            col = col_vector1.back();
            col_vector1.pop_back();
        }else{
            if(col_vector2.empty()){
                col1orcol2 = true;
                continue;
            }
            col = col_vector2.back();
            col_vector2.pop_back();
        }
        if(slopeQueens1[index - col +N] == 0 && slopeQueens2[index + col] == 0){
            queensLocation[index] = col;
            addQueen(index);
            index++;
            continue;
        }else{
            if(col1orcol2){
                col_vector2.push_back(col);
            }else{
                col_vector1.push_back(col);
            }
        }
    }
    for(int i = 0; i < col_vector1.size(); i++){
        queensLocation[index] = col_vector1[i];
        addQueen(index);
        index++;
    }
    for(int i = 0; i < col_vector2.size(); i++){
        queensLocation[index] = col_vector2[i];
        addQueen(index);
        index++;
    }
}
int getConflictNum(){
    return queensConflictNum;
}

void addQueen(int x){
    int slope1 = x - queensLocation[x] + N;
    int slope2 = x + queensLocation[x];
    slopeQueens1[slope1] ++;
    if(slopeQueens1[slope1] > 1)
        queensConflictNum ++;
    if(slope1 == slope2){
        return;
    }
    slopeQueens2[slope2] ++;
    if(slopeQueens2[slope2] > 1)
        queensConflictNum ++;
}

void removeQueen(int x){
    int slope1 = x - queensLocation[x] + N;
    int slope2 = x + queensLocation[x];
    slopeQueens1[slope1] --;
    if(slopeQueens1[slope1] > 0)
        queensConflictNum --;
    if(slope1 == slope2){
        return;
    }
    slopeQueens2[slope2] --;
    if(slopeQueens2[slope2] > 0)
        queensConflictNum --;
}

bool swap(int x, int y){
    if(x == y)
        return false;
    int fx = queensLocation[x];
    int fy = queensLocation[y];
    int xyConflictNum = getConflictNum();
    removeQueen(x);
    removeQueen(y);
    queensLocation[x] = fy;
    queensLocation[y] = fx;
    addQueen(x);
    addQueen(y);
    int yxConflictNum = getConflictNum();
    if(xyConflictNum <= yxConflictNum){
        removeQueen(x);
        removeQueen(y);
        queensLocation[x] = fx;
        queensLocation[y] = fy;
        addQueen(x);
        addQueen(y);
        return false;
    }
    return true;
}
void solve(){
    resetBoard();
    int lastConflictNum = 0;
    int times = 0;
    int count = 0;
    while (queensConflictNum != 0) {
        if(lastConflictNum == queensConflictNum){
            count++;
        }else{
            count = 0;
        }
        if(count > 3){
            resetBoard();
            count = 0;
            times ++;
        }
        lastConflictNum = queensConflictNum;
        vector<int> conflictQueens;
        for(int i = 0; i < N; i++){
            int slope1 = i - queensLocation[i] + N;
            int slope2 = i + queensLocation[i];
            if(slopeQueens1[slope1] > 1 || slopeQueens2[slope2] > 1)
                conflictQueens.push_back(i);
        }
        for(int i = 0;i < conflictQueens.size();i++){
            for(int j = 0; j < N; j++){
                if(swap(conflictQueens[i],j))
                    break;
            }
        }
    }
    cout<<"true"<<endl;
    cout<<times<<endl;
}

int main()
{
    srand((unsigned)time(NULL));
    cout<<N<<endl;
    for(int i = 0; i < N; i++)
        queensLocation[i] = 0;
    long start, end;
    start = clock();
    solve();
    end = clock();
    double duration = (double)(end - start) / CLOCKS_PER_SEC;
    cout<<duration<<endl;
    return 0;
}
