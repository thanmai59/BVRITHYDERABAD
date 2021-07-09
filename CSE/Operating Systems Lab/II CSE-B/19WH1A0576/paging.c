#include<stdio.h>
void main()
{
	int mem_size= 25;
	int pagesize,nofpage;
	int p[100];
	int frameno,offset;
	int logadd,phy_add;
	int i,choice=0;
	printf("\nYour memory size is %d ",mem_size);
	printf("\nEnter page size:");
	scanf("%d",&pagesize);

	nofpage = mem_size/pagesize;

	for(i=0;i<nofpage;i++)
	{
		printf("\nEnter the frame of page %d:",i+1);
		scanf("%d",&p[i]);
	}

	do
	{
		printf("\nEnter a logical address:");
		scanf("%d",&logadd);
		frameno=logadd/pagesize;
		offset=logadd%pagesize;
		phy_add=(p[frameno]*pagesize)+offset;
		printf("\nPhysical address is: %d",phy_add);
		printf("\nDo you want to continue(1/0)?:");
		scanf("%d",&choice);
	}while(choice==1);
}

