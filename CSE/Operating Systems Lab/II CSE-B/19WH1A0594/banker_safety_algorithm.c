#include<stdio.h>
int main()
{
	int p, n=3, rA, rB, rC, avA, avB, avC;
	printf("Enter number of processes\n");
	scanf("%d", &p);
	printf("Enter instances of 3 resources \n");
	scanf("%d %d %d", &rA, &rB, &rC);
	avA = rA;
	avB = rB;
	avC = rC;
	int maxA[p], maxB[p], maxC[p], allocA[p], allocB[p], allocC[p], needA[p], needB[p], needC[p];
	printf("Enter Max needs of resources followed by allocation of resources \n");
	for(int i=0;i<p;i++)
	{
		scanf("%d %d %d %d %d %d", &maxA[i], &maxB[i], &maxC[i], &allocA[i], &allocB[i], &allocC[i]);
		needA[i] = maxA[i] - allocA[i];
		needB[i] = maxB[i] - allocB[i];
		needC[i] = maxC[i] - allocC[i];
		avA = avA - allocA[i];
		avB = avB - allocB[i];
		avC = avC - allocC[i];
	}
	printf("Number of processes : %d \n", p);
	printf("Available:  %d,  %d,  %d \n", avA, avB, avC);
	printf("    |Max| |Alloc| |Need|\n");
	for(int i=0;i<p;i++)
		printf("P%d |%d %d %d| |%d %d %d| |%d %d %d|\n",i,  maxA[i], maxB[i], maxC[i], allocA[i], allocB[i], allocC[i], needA[i], needB[i], needC[i]); 
	int flag = 0, pr = 0;
	while(flag < p)
	{
		if((avA >= needA[pr]) && (avB >= needB[pr]) && (avB >= needB[pr]) && ((needA[pr] != 0) || (needB[pr] != 0) || (needC[pr] != 0)))
		{
			flag = flag + 1;
			avA = avA + allocA[pr];
			avB = avB + allocB[pr];
			avC = avC + allocC[pr];
			needA[pr] = needB[pr]  = needC[pr] = 0;	
			printf("Safety sequence P%d \n", pr);
		}
		else
		{
			if(pr == (p-1))
				pr = 0;
			else
				pr += 1;
		}
	}
	return 0;
}