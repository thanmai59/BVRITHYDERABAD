#include<stdio.h>
void sorting(int start, int end, int to_sort_acc[20], int to_change[20])
{
	int i , j, temp, t;
	for(i = start; i< end - 1; i++){
		for(j = start; j< end - i -1; j++){
			if(to_sort_acc[j] > to_sort_acc[j+1]){
				temp = to_sort_acc[j];
				to_sort_acc[j] = to_sort_acc[j+1];
				to_sort_acc[j+1] = temp;

				t = to_change[j];
				to_change[j] = to_change[j+1];
				to_change[j+1] = t;
			}
		}
	}
	
}
int main(){
	printf("Enter the number of processes\n");
	int n, i;
	float sum = 0.0;
	scanf("%d",&n);
	int arr_time[n], bst_time[n], wtg_time[n];
	printf("Input order: Arrival Time, Burst Time\n");
	for(i =0; i<n; i++){
		printf("For Process %d: ", i);
		scanf("%d%d",&arr_time[i], &bst_time[i]);}
	sorting(0,n,arr_time,bst_time);
	printf("After sorting the Arrival time\n");
	for(i =0; i<n; i++)
	printf("%d %d\n",arr_time[i], bst_time[i]);
	wtg_time[0] = 0;
	int s_time = bst_time[0];
	// for sorting the burst times
	sorting(1,n+1,bst_time,arr_time);
	for(i = 1; i<n ; i++){
		wtg_time[i] = s_time - arr_time[i];
		sum += wtg_time[i];
		s_time += bst_time[i];}
	printf("AVG WAITING TIME : %.2f",sum/n);
}
	
	
