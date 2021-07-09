//Non premptive priority scheduling
 
#include<stdio.h>
int main()
{
	int n, temp;
	printf("Enter number of processes\n");
	scanf("%d", &n);
	int priority[n], BT[n], P[n], ST[n];	
	printf("Enter BT and Priority \n");
	for(int i =0;i<n;i++)
	{
		scanf("%d %d", &BT[i], &priority[i]);
		P[i] = i+1;
	}

	for(int i=0;i<n-1;i++)
		for(int j=0;j<n-i-1;j++)
			if(priority[j] < priority[j+1])
			{
			temp = priority[j];	
			priority[j] = priority[j+1];
			priority[j+1] = temp;	

			temp = BT[j];	
			BT[j] = BT[j+1];
			BT[j+1] = temp;

			temp = P[j];	
			P[j] = P[j+1];
			P[j+1] = temp;			
			}

	ST[0] = 0;
	for(int i=1;i<n;i++)	
		ST[i] = ST[i-1] + BT[i-1];
	float tat=0.0;
	for(int i=0;i<n;i++)
		tat += ST[i] + BT[i];
	
	printf("Process BT   Priority   Service_time\n");
	for(int i=0;i<n;i++)
		printf("P%d       %d       %d         %d\n", P[i], BT[i], priority[i], ST[i]);

	float avg_wait_time = 0.0; 
	for(int i=0; i<n; i++)
	{
		avg_wait_time += (ST[i]);
	}
	avg_wait_time = avg_wait_time / n;
	tat = tat/n;
	printf("Average Wait Time = %f\n", avg_wait_time);
	printf("Average TAT = %f\n",tat);
return 0;
}