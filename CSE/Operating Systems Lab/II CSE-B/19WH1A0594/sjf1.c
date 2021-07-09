#include<stdio.h>
int main()
{
	int n, i, j;
	printf("Enter number of processes\n");
	scanf("%d", &n);
	int at[n], bt[n], p[n], st[n];
	printf("Enter arrival and burst time\n");
	for(i =0;i<n;i++)
	{
		scanf("%d %d", &at[i], &bt[i]);
		p[i] = i+1;
	}
	st[0] = 0;
	int completion = bt[0], t;
	for(i=0;i<n;i++)
	{
		for(j=1;j<n-i-1; j++)
			if(bt[j] > bt[j+1] && at[j] <= completion)
			{
				t = bt[j];
				bt[j] = bt[j+1];
				bt[j+1] = t;

				t = p[j];
				p[j] = p[j+1];
				p[j+1] = t;

			} 
	}
	
	for(i=1;i<n;i++)	
		st[i] = st[i-1] + bt[i-1];

	for(i=0;i<n;i++)
		printf("p%d    %d     %d       %d\n", p[i], at[i], bt[i], st[i]);	
	
	float avg_waiting_time = 0.0; 
	for(i=0; i<n; i++)
	{
		avg_waiting_time += (st[i] - at[i]);
	}

	printf("Average Wait Time = %f\n", avg_waiting_time / n);
	return 0;
}
