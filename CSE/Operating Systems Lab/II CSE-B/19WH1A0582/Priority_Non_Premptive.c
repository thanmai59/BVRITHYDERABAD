#include<stdio.h>
void sorting(int start, int end, int to_sort_acc[20], int to_change[20])
{
	int i , j, temp, t, t1;
	for(i = start; i< end - 1; i++){
		for(j = start; j< end - i -1; j++){
			if(to_sort_acc[j] < to_sort_acc[j+1]){
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
	int n, i;
	printf("ENTER THE NUMBER OF PROCESSES\n");
	scanf("%d", &n);
	int bt[n], pri[n], wt[n], tat[n];
	printf("Give the inputs in the order\n1.Burst time\n2.Priority\n");
	printf("Note : Greater Priority Number will get executed 1st\n");
	for(i=0;i<n;i++){
		scanf("%d%d", &bt[i], &pri[i]);
	}
	sorting(0, n, pri, bt);
	printf("After sorting the priorities\nBT \t Priority\n");
	for(i=0;i<n;i++)
	printf("%d \t %d\n", bt[i], pri[i]);
	wt[0] = 0, tat[0] = bt[0];
	float sum = 0.0, sum_tat = tat[0];
	for(i=1;i<n;i++){
		wt[i] = bt[i - 1] + wt[i - 1];
		sum += wt[i];
		tat[i] = tat[i -1] + bt[i];
		sum_tat += tat[i];
	}
	printf("Avg Waiting Time = %.2f\n", sum / n);
	printf("Turn Around Time = %.2f", sum_tat / n);
}
