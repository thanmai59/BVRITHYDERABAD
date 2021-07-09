#include<stdio.h>
int main()
{
	int n,i,j,temp,pos,p[10],wt[10],btime=0,min,k=1,sum=0;
	float awt=0,wsum=0;
	printf("Enter number of processes : ");
	scanf("%d",&n);
	int at[n],bt[n];
	printf("Process\tArrival time\tBurst time\n");
	for(i=0;i<n;i++)
	{
		
		printf("P[%d]\t",i+1);
		scanf("%d\t\t%d",&at[i],&bt[i]);
	}
	for(i=0;i<n;i++)
	{
		for(j=0;j<n;j++)
		{
			if(at[i]<at[j])
			{
				temp=p[j];
				p[j]=p[i];
				p[i]=temp;
				temp=at[j];
				at[j]=at[i];
				at[i]=temp;
				temp=bt[j];
				bt[j]=bt[i];
				bt[i]=temp;
			}
		}
	}
	for(j=0;j<n;j++)
	{
		btime=btime+bt[j];
		min=bt[k];
		for(i=k;i<n;i++)
		{
			if (btime>=at[i] && bt[i]<min)
			{
				temp=p[k];
				p[k]=p[i];
				p[i]=temp;
				temp=at[k];
				at[k]=at[i];
				at[i]=temp;
				temp=bt[k];
				bt[k]=bt[i];
				bt[i]=temp;
			}
		}	
		k++;
	}
	wt[0]=0;
	for(i=1;i<n;i++)
	{
		sum=sum+bt[i-1];
		wt[i]=sum-at[i];
		wsum=wsum+wt[i];
	}
	printf("\nProcess\tBurst time\tArrivaltime\tWaiting time\n");
	for(i=0;i<n;i++)
	{
		printf("P[%d]\t\t%d\t\t%d\t\t%d\n",i+1,bt[i],at[i],wt[i]);
	}
	awt = wsum/n;
	printf("The average waiting time = %f",awt);
 	
		
	
	return 0;
	
}
