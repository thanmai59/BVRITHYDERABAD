#include<stdio.h>
int main()
{
	int i,n = 4;
	int arrival_time[n], exec_time[n], service_time[n];
	float avg_waiting_time = 0;
	service_time[0]=0;
	for(i=0; i<n; i++)
	{ 	
		printf("Enter arrival and execution time %d", i+1);
		scanf("%d %d",&arrival_time[i], &exec_time[i]);
		service_time[i] = service_time[i-1] + exec_time[i-1];
	}
	for(i=0;i<n;i++)
	{
		printf("%d	%d	%d\n", arrival_time[i], exec_time[i], service_time[i]);
		avg_waiting_time += (service_time[i] - arrival_time[i]);
	}
	printf("Average Waiting Time = %f", avg_waiting_time / n);
	return 0;
}
