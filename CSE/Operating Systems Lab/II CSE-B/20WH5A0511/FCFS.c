#include<stdio.h>
int main()
{
	int arrival[100],exe[100],n,i;
	float awt,wt=0;
	printf("enter no.of processors:");
	scanf("%d",&n);
	int s[n];
	s[0]=0;
	for(i=0;i<n;i++)
	{
	
	     printf("\nenter processor arrival time :");
	      scanf("%d",&arrival[i]);
	}

	for(i=0;i<n;i++)
	{
	
		printf("\nenter processor execution time:");
		scanf("%d",&exe[i]);
	}
	for(i=1;i<n;i++)
	{	
		s[i]=s[i-1]+exe[i-1];
		printf("service time of processor :%d\n",s[i]);
	}
	
	for(i=1;i<n;i++)
	{
		wt+=s[i]-arrival[i];
	}
	awt=wt/n;
	printf("average waiting time:%f",awt);
	
return 0;

	}
