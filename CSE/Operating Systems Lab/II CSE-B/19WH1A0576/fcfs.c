#include<stdio.h>
int main()
{
	int n,i;
	printf("Enter number of processes : ");
	scanf("%d",&n);
	int at[n],et[n];
	printf("Process\tArrival time\tExecution time\n");
	for(i=0;i<n;i++)
	{
		
		printf("P[%d]\t",i);
		scanf("%d\t\t%d",&at[i],&et[i]);
	}
	int st[n];
	st[0]=0;
	for(i=1;i<n;i++)
	{
		st[i] = st[i-1] + et[i-1];
	}
	float avwt;
	float sum = 0.0;
	for(i=0;i<n;i++)
	{
		sum = sum + (st[i] - at[i]);
	}
	printf("Process\tArrival time\tExecution time\tService time\n");
	for(i=0;i<n;i++)
	{
		printf("P[%d]\t\t",i);
		printf("%d\t\t%d\t\t%d\n",at[i],et[i],st[i]);
	}
	avwt = sum/n;
	printf("The average waste time = %f ", avwt);
	return 0;
	
}
