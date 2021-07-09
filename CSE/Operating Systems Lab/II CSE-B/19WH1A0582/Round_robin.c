#include<stdio.h>
void sorting(int start, int end, int to_sort_acc[20], int to_change[20])
{
	int i , j, temp, t, t1;
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
	int qnt, n;//qnt = quantum
	printf("Enter the Number of processes : ");
	scanf("%d",&n);
	printf("Enter the Time Quantum : ");
	scanf("%d",&qnt);
	int i, at[n], bt[n], wt[n],rt[n], ct[n], tt[n];//st -> starting time, ct -> completion time 
	printf("Enter Accordingly:\n1.Arrival Time\n2.Burst Time\n\n");
	for(i=0;i<n;i++){
		printf("For Process %d\n", i+1);
		scanf("%d%d",&at[i],&bt[i]);
		rt[i] = bt[i];
	}
	sorting(0,n,at,bt);
	printf("After Sorting\nArrival Time\tBurst Time\n");
	for(i=0;i<n;i++)
		printf("%d\t\t%d\n",at[i],bt[i]);
	int time, done_pro = n, status = 0;//done_pro -> done processes
	for(i=0, time = 0;done_pro != 0;){
		if(rt[i] <= qnt && rt[i] > 0){
			time += rt[i];
			rt[i] = 0;
			status = 1;
		}
		else if(rt[i] > 0){
			rt[i] -= qnt;
			time += qnt;
		}
		if(rt[i] == 0 && status == 1){
			done_pro--;
			ct[i] = time;
			status = 0;}
		if(i == n - 1)
		i = 0;
		else if(at[i+1] <= time)
		i++;
		else
		i = 0;
	}
	float sum_wt = 0.0 , sum_tt = 0.0;
	for(i=0;i<n;i++){
		tt[i] = ct[i] - at[i];
		wt[i] = tt[i] - bt[i];
		sum_wt += wt[i];
		sum_tt += tt[i];
	}
	printf("AVG WAITING TIME = %.2f\nAVG TURNAROUND TIME = %.2f\n",(sum_wt/n), (sum_tt/n));
}
