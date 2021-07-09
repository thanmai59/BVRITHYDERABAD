#include<stdio.h>
void wait(int *s)
{
	while(*s<=0);
	*s--;	
}

void signal(int *s)
{
	*s++;
}

void dinning(int n)
{
	int chopstick[n];
	for(int i=0;i<n;i++)
		chopstick[i] = 1;
	int i=0;
	do
	{
		wait(&chopstick[i]);
		wait(&chopstick[(i+1)%n]);
		printf("Process %d Eating\n", i+1);
		signal(&chopstick[i]);
		signal(&chopstick[(i+1)%n]);
		printf("Process %d Thinking\n", i+1);
		i = ((i+1)%n);
	}while(1);
}

int main()
{
	int n;
	printf("Enter number of processes:     ");
	scanf("%d", &n);
	dinning(n);
}