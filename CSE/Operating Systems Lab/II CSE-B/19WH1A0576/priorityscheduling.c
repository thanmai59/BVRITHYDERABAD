#include<stdio.h>
int main()
{
	int bt[10],p[10],wt[20],tat[20],pr[20],i,j,n,total=0,pos,temp;
	float avg_wt,avg_tat;
	printf("Enter number of processes:");
	scanf("%d",&n);
	printf("Process\tBurst time\tPriority");
	for(i=0;i<n;i++)
	{
		printf("\nP[%d]\t",i+1);
		scanf("%d\t\t%d",&bt[i],&pr[i]);
		p[i]=i+1;
	}
	//sorting
	for(i=0;i<n;i++)
	{
		pos=i;
		for(j=i+1;j<n;j++)
		{
			if(pr[j]==pr[pos])
				if(pr[j]<pr[pos])
					pos=j;
		}
		temp=pr[i];
		pr[i]=pr[pos];
		pr[pos]=temp;
		
		temp=bt[i];
		bt[i]=bt[pos];
		bt[pos]=temp;
		
		temp=p[i];
		p[i]=p[pos];
		p[pos]=temp;
	}
	wt[0]=0;
	//calculating waiting time
	for(i=1;i<n;i++)
	{
		wt[i]=0;
		for(j=0;j<i;j++)
			wt[i]+=bt[j];
		
		total+=wt[i];
	}
	avg_wt=(float)total/n;
	total=0;
	
	for(i=0;i<n;i++)
	{
		tat[i]=bt[i]+wt[i];
		total+=tat[i];
	}
	avg_tat=(float)total/n;
	printf("Process\tBurst time\tWaiting time\tTurn around time\n");
	for(i=0;i<n;i++)
	{
		printf("P[%d]\t",i+1);
		printf("%d\t\t%d\t\t%d",bt[i],wt[i],tat[i]);
		printf("\n");
	}
	printf("Average waiting time is %f\n",avg_wt);
	printf("Average turn around time is %f\n",avg_tat);
	
	return 0;
	
}
