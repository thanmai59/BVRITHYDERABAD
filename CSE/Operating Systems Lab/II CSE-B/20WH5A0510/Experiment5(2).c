//Bankers Resource Allocation Algorithm
#include<stdio.h>
int main()
{
int p, n=3, resA, resB, resC, avA, avB, avC;
printf("Enter number of processes\n");
scanf("%d", &p);
printf("Enter instances of 3 resources \n");
scanf("%d %d %d", &resA, &resB, &resC);
avA = resA;
avB = resB;
avC = resC;
int maxA[p], maxB[p], maxC[p], allocA[p], allocB[p], allocC[p], ndA[p], ndB[p], ndC[p];
printf("Enter Max needs of resources followed by allocation of resources \n");
for(int i=0;i<p;i++)
{
	scanf("%d %d %d %d %d %d", &maxA[i], &maxB[i], &maxC[i], &allocA[i], &allocB[i], &allocC[i]);
	ndA[i] = maxA[i] - allocA[i];
	ndB[i] = maxB[i] - allocB[i];
	ndC[i] = maxC[i] - allocC[i];
	avA = avA - allocA[i];
	avB = avB - allocB[i];
	avC = avC - allocC[i];
}

int j, reqA, reqB, reqC;
printf("Enter process who need resource allocation(0-n)\n");
scanf("%d", &j);
printf("Enter resources for request\n");
scanf("%d %d %d", &reqA, &reqB, &reqC);
if((reqA<=ndA[j]) && (reqB<=ndB[j]) && (reqC <= ndC[j])&&(reqA<=avA) && (reqB<=avB) && (reqC <= avC))
{
	allocA[j] = allocA[j] + reqA;
	allocB[j] = allocB[j] + reqB;
	allocC[j] = allocC[j] + reqC;
	ndA[j] = ndA[j] - reqA;
	ndB[j] = ndB[j] - reqB;
	ndC[j] = ndC[j] - reqC;	
	avA = avA - reqA;
	avB = avB - reqB;
	avC = avC - reqC;
}


printf("Number of processes : %d \n", p);
printf("Available:  %d,  %d,  %d \n", avA, avB, avC);
printf("    |Max|   |Alloc|  |Need|\n");
for(int i=0;i<p;i++)
	printf("P%d |%d %d %d| |%d %d %d| |%d %d %d|\n",i,  maxA[i], maxB[i], maxC[i], allocA[i], allocB[i], allocC[i], ndA[i], ndB[i], ndC[i]); 



int flag = 0, pr = 0, i = 0;
while(flag < p)
{
	if((avA >= ndA[pr]) && (avB >= ndB[pr]) && (avB >= ndB[pr]) && ((ndA[pr] != 0) || (ndB[pr] != 0) || (ndC[pr] != 0)))
	{
		flag = flag + 1;
		avA = avA + allocA[pr];
		avB = avB + allocB[pr];
		avC = avC + allocC[pr];
		ndA[pr] = ndB[pr]  = ndC[pr] = 0;	
		printf("Safety sequence P%d \n", pr);
	}
	else
	{
		if(pr == (p-1))
			pr = 0;
		else
			pr += 1;
	}
	if(i == 25)	
		break;
	else
		i++;
}

if(i == 25)
	printf("Request Not Granted\n");
else
	printf("Request Granted\n");

return 0;
}