#include<stdio.h>
int main(){
	int n;
	printf("Enter the number of processes\n");
	scanf("%d",&n);
	int  i;
	int p[n],arr[n],exe[n],wait[n],ser[n];
	for(i=0;i<n;i++){
		printf("Enter the values for the process %d in the order\n1.Arrival Time\n2.Execution Time\n",i);
		scanf("%d",&arr[i]);
		scanf("%d",&exe[i]);
	}
	wait[0] = 0;
	float sum = 0; ser[0] = 0;
	for(i= 1;i<n;i++){
		ser[i] = ser[i-1] + exe[i-1]; 
		wait[i] = ser[i] - arr[i];
		sum += wait[i];}
	printf("Avg Wait time is %.2f",sum / n);
}
	
	
