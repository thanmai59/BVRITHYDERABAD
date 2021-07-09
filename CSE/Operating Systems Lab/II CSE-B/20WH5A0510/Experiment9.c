#include<stdio.h>
int main()
{
int MMsize = 15, PGsize, pages;
int a[100];
int frameno,offset;
int logadd,phyadd;
int c;
printf("Your Memory Size is %d\n",MMsize);
printf("Enter Page Size or Frame Size : ");
scanf("%d", &PGsize);
pages = MMsize / PGsize;
for(int i=0; i < pages ; i++)
{
	printf("\nEnter the Frame of the Page%d: ",i+1);
	scanf("%d",&a[i]);
}

do
{
	printf("\nEnter a Logical address / Hard Disk address :");
	scanf("%d",&logadd);
	frameno = logadd / PGsize;
	offset = logadd % PGsize;
	phyadd = (a[frameno] * PGsize) + offset;
	printf("\nPhysical address is : %d",phyadd);	
	printf("\nDo you want to continue(0/1)? : ");
	scanf("%d",&c);
}while(c == 1);
return 0;
}