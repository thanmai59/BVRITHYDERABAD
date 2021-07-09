#include<stdio.h>
int main()
{
	int n;
	printf("Enter number of processes\n");
	scanf("%d", &n);
	int AT[n], BT[n], P[n], ST[n];
	printf("Enter AT and BT\n");
	for(int i =0;i<n;i++)
	{
		scanf("%d %d", &AT[i], &BT[i]);
		P[i] = i+1;
	}
	ST[0] = 0;
	int completion = BT[0], temp;
	for(int i=0;i<n;i++)
	{
		for(int j=1;j<n-i-1; j++)
			if(BT[j] > BT[j+1] && AT[j] <= completion)
			{
				temp = BT[j];
				BT[j] = BT[j+1];
				BT[j+1] = temp;

				temp = AT[j];
				AT[j] = AT[j+1];
				AT[j+1] = temp;

				temp = P[j];
				P[j] = P[j+1];
				P[j+1] = temp;

			} 
	}
	
	for(int i=1;i<n;i++)	
		ST[i] = ST[i-1] + BT[i-1];

	for(int i=0;i<n;i++)
		printf("P%d    %d     %d       %d\n", P[i], AT[i], BT[i], ST[i]);	
	
	float avg_wait_time = 0.0; 
	for(int i=0; i<n; i++)
	{
		avg_wait_time += (ST[i] - AT[i]);
	}
	avg_wait_time = avg_wait_time / n;

	printf("Average Wait Time = %f\n", avg_wait_time);
	return 0;
}