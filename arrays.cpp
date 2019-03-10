#include <iostream>
using namespace std;

/*This is a function that takes in two sorted arrays (a is size M and b is size 2M)
and merges the two arrays into b with all elements sorted*/
void sorted_functions(int a[], int b[], int M) {
    int a_index = 0;
    int b_index = 0;
    int tot_index = 0;
    int temp[2*M];
	
	//Iterate adding minimum elements until the end of one array is reached
    while(a_index < M && b_index < M){
        if(a[a_index] <= b[b_index]){
            temp[tot_index] = a[a_index];
            a_index++;
        }
        else{
            temp[tot_index] = b[b_index];
            b_index++;
        }
        tot_index++;
    }
	//If all elements of b have been inserted, insert the rest of a
    while(a_index < M){
        temp[tot_index] = a[a_index];
        a_index++;
        tot_index++;
    }
	//If all elements of a have been inserted, insert the rest of b
    while(b_index < M){
        temp[tot_index] = b[b_index];
        b_index++;
        tot_index++;
    }
	//Copy elements from temporary array into b
    for(int i = 0; i < 2*M; i++) {
        b[i] = temp[i];
    }
}

int main()
{
    //Test Case
    int M = 10;
    int a[10] = {0, 2, 4, 6, 8, 10, 12, 14, 16, 18};
    int b[20] = {1, 3, 5, 7, 9, 11, 13, 15, 17, 19};
    sorted_functions(a, b, M);
    for(int i = 0; i < 2*M; i++){
        cout << b[i] << endl;
    }
    return(0);
}