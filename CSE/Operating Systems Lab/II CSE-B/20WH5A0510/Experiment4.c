//Round robin preemptive


#include<stdio.h>
int main()
{
	int n, temp;
	printf("Enter number of processes\n");
	scanf("%d", &n);
	int BT[n], P[n], tq,lT[n],flag = 0, ST[n];	
	printf("Enter BT\n");
	for(int i =0;i<n;i++)
	{
		scanf("%d", &BT[i]);
		P[i] = i+1;
		lT[i] = BT[i];
		ST[i] = 0;
	}

	printf("Enter Time Quantum: \n");
	scanf("%d", &tq);
	
	int p=0, current_time = 0;
	while(flag < n)
	{
		if(lT[p] <= tq)
		{
			ST[p] = current_time - ST[p];
			current_time += lT[p];
			lT[p] = 0;
			flag = flag + 1;
		}
		else
		{
			//printf("Else block \n");
			ST[p] = ST[p] + tq;
			current_time += tq;
			lT[p] = lT[p] - tq;	
		}
		//printf("%d %d  %d\n",p+1, current_time, ST[0]);
		if(p == n-1 && lT[0] != 0)
			p = 0;
		else
		{
			int temp = 0;
			while(p != n-1)
			{
				p = p+1;
				if(lT[p] != 0)
				{	temp = 1;
					break;
				}
			}
			if(temp == 0)
				p = 0;
		}
}

	printf("Process BT    ST \n");
	for(int i=0;i<n;i++)
		printf("P%d       %d    %d\n", P[i], BT[i], ST[i]);
	printf("Time Quantum : %d", tq);

	float avg_wait_time = 0.0;
	for(int i=0;i<n;i++)
		avg_wait_time += ST[i];
	avg_wait_time = avg_wait_time / n;
	printf("\nAverage wait time = %f \n", avg_wait_time);
return 0;
}