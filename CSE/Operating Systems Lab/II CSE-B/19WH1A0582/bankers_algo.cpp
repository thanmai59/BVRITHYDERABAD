#include<stdio.h>
int main(){
	int p, r;//p - processes , r = resources
	printf("Enter\n1.Number of processes\n2.Number of resources\n");
	scanf("%d%d",&p,&r);
	int alloc[p][r], max[p][r], avail[r], need[p][r], finish[p], result[p];
	int i,j;
	printf("Enter\n1.Allocated Resources  2.Maximum Resources\n");
	for(i=0;i<p;i++){
		printf("For Process %d :\n", i);
		for(j=0;j<r;j++){
		printf("\tFor Resource %d : ", j);	
		scanf("%d%d",&alloc[i][j], &max[i][j]);
		need[i][j] = max[i][j] - alloc[i][j];
		}
		finish[i] = 0;
	}
	for(i=0;i<r;i++){
		printf("Enter the number of available resources for R%d: ",i);
		scanf("%d",&avail[i]);
	}
	int k = 0, res = 0;
    int y = 0, temp_status = 0;//temp_status is used if there is no safe seq
    for (k = 0; k < p; k++) {
    	int safe = 0;
        for (int i = 0; i < p; i++) {
            if (finish[i] == 0) {
  
                int flag = 0;
                for (int j = 0; j < r; j++) {
                    if (need[i][j] > avail[j]){
                        flag = 1;
                        safe = 1;
                        break;
                    }
                }
                if (flag == 0) {
                    result[res++] = i;
                    for (y = 0; y < r; y++)
                        avail[y] += alloc[i][y];
                    finish[i] = 1;
                    safe = 1;
                }
            }
        }
        if(safe == 0){
        printf("It is not SAFE\n");
        temp_status = 1;}
        break;
    }
    if(temp_status != 1){
    printf("SAFE Sequence\n");
    for (i = 0; i < p - 1; i++)
        printf(" P%d ->", result[i]);
    printf(" P%d", result[p - 1]);}
}

