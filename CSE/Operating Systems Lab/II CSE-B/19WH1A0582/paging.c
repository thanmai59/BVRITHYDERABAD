#include<stdio.h>
#define MAX 50
int main(){
	int memsize = MAX;
	int pagesize, nofpage;
	int p[100];
	int framenum, offset,logadd, phyadd;
	//logadd -> logical address, phyadd -> physical address
	int choice = 0;
	printf("Your Memory Size is %d\n",memsize);
	printf("\nEnter Page Size : ");
	scanf("%d",&pagesize);
	nofpage = memsize / pagesize;//nofpage is num of frames
	int i;
	for(i=0;i<nofpage;i++){
		printf("\nEnter the frame of page%d:",i+1);
		scanf("%d",&p[i]);
	}
	do
	{
		printf("\nEnter a logical address:");
		scanf("%d",&logadd);
		framenum = logadd/pagesize;
		offset = logadd % pagesize;
		phyadd=(p[framenum]*pagesize)+offset;
		printf("\nPhysical address is:%d",phyadd);
		printf("\nDo you want to continue(1/0)?:");
		scanf("%d",&choice);
		}while(choice==1);
		
}
