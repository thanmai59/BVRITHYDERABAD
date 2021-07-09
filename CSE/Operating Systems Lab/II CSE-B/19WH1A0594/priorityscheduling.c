#include<stdio.h>
int main()
{
	int n, t;
	printf("Enter number of processes : ");
	scanf("%d", &n);
	int pr[n], bt[n], p[n], st[n];	
	printf("Enter Burst time and Priority \n");
	for(int i =0;i<n;i++)
	{
		scanf("%d %d", &bt[i], &pr[i]);
		p[i] = i+1;
	}

	for(int i=0;i<n-1;i++)
	{
		for(int j=0;j<n-i-1;j++)
		{
			if(pr[j] < pr[j+1])
			{
				t = pr[j];	
				pr[j] = pr[j+1];
				pr[j+1] = t;	

				t = bt[j];	
				bt[j] = bt[j+1];
				bt[j+1] = t;

				t = p[j];	
				p[j] = p[j+1];
				p[j+1] = t;			
			}
		}
	}
	st[0] = 0;
	for(int i=1;i<n;i++)
	{	
		st[i] = st[i-1] + bt[i-1];
	}
	float tat=0.0;
	for(int i=0;i<n;i++)
	{
		tat += st[i] + bt[i];
	}
	printf("Process\tBurstTime\tPriority\tServiceTime\n");
	for(int i=0;i<n;i++)
	{
		printf("p%d\t\t%d\t\t%d\t\t%d\n", p[i], bt[i], pr[i], st[i]);
	}
	float avg_wait_time = 0.0; 
	for(int i=0; i<n; i++)
	{
		avg_wait_time += (st[i]);
	}
	avg_wait_time = avg_wait_time / n;
	tat = tat/n;
	printf("Average Wait Time = %f\n", avg_wait_time);
	printf("Average Turn around time = %f\n",tat);
	return 0;
}