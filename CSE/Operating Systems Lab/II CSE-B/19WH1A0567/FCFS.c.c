#include<stdio.h>
int n, arrival[10], execution[10], service[10];

void get_values()
{
	int i;
	for(i=0; i<n; i++)
	{
		printf("Enter arrival and execution time for processor %d", i+1);
		scanf("%d %d",&arrival[i], &execution[i]);
		if(i == 0)
			service[i] = 0;
		else
			service[i] = service[i-1] + execution[i-1];
	}	
}

float calc_wait_time()
{
	float avg_wait_time = 0.0; 
	for(int i=0; i<n; i++)
	{
		avg_wait_time += (service[i] - arrival[i]);
	}
	avg_wait_time = avg_wait_time / n;
	return avg_wait_time;
}

int main()
{
	float time;
	printf("Enter number of process: ");
	scanf("%d", &n);
	get_values();
	
	printf("\nProcess  Arrival Execute Service\n");
	for(int i=0; i<n; i++)
	{
		printf("   %d     %d	   %d	   %d\n",i+1, arrival[i], execution[i], service[i]);
	}
	time = calc_wait_time();
	printf("\nAverage Wait Time = %f", time);
	
	
	
	return 0;
}
