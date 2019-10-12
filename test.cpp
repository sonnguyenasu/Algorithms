#include<iostream>
using namespace std;

void swap(int *x, int *y){
	int temp = *y;
	*y = *x;
	*x = temp;
}

int partition(int* arr,int p, int r){
	int i = p-1;
	int x = arr[r];
	for(int j = 0; j < r-p; j++){
		if(arr[p+j] <= x){
			i++;
			swap(&arr[i],&arr[p+j]);
		}
	}
	swap(&arr[i+1],&arr[r]);
	return i+1;
}

void quickSort(int *arr, int p, int r){
	if(r==p){
		return;
	}
	int q = partition(arr, p, r);
	quickSort(arr,p,q-1);
	quickSort(arr,q,r);
}

int main(){
	int array[5] = {1,4,6,2,5};
	quickSort(array,0,4);
	for(int i = 0; i < 5; i++)
		cout << array[i] << " ";
	return 0;
}