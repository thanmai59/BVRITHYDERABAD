//Producer consumer using Semaphore

#include<stdio.h>
#include<stdlib.h>
int full = 0, empty = 5, mutex =1, i = 0;
void wait(int *s)
{
	//while(*s<=0);
	*s--;
}

void signal(int *s)
{
 *s++;
}

void producer()
{
	wait(&mutex);
	signal(&full);
	wait(&empty);
	i++;
	printf("\nProducer produces item : %d \n", i);
	signal(&mutex);
}

void consumer()
{
	wait(&mutex);
	wait(&full);
	signal(&empty);
	printf("\nConsumed item : %d",i);
	i --; 
	signal(&mutex);
}

int main()
{
	int n;
	printf("\n1.Producer\n2.Consumer\n3.Exit");
	while(1)
	{	
		printf("\nEnter your choice:");
		scanf("%d",&n);
		switch(n)
		{
		case 1: if(i != 5)
			producer();
		             else
			printf("Buffer is full!!");
		            break;
		case 2: if(i != 0)
			consumer();
		              else
			printf("Buffer is empty!!");	
                                                    break;
		case 3:
			exit(0);
		}
	}
return 0;
}