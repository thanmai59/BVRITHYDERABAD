#include<stdio.h> 
int main() 
{ 
      int i, n, sum = 0, x, c = 0, time_quantum; 
      int wait_time = 0, turnaround_time = 0, at[10], bt[10], t[10]; 
      float average_wait_time, average_turnaround_time;
      printf("\nEnter Total Number of Processes:\t"); 
      scanf("%d", &n); 
      x = n; 
      for(i = 0; i < n; i++) 
      {
            printf("\nEnter Details of Process[%d]\n", i + 1);
            printf("Arrival Time:\t");
            scanf("%d", &at[i]);
            printf("Burst Time:\t");
            scanf("%d", &bt[i]); 
            t[i] = bt[i];
      } 
      printf("\nEnter Time Quantum:\t"); 
      scanf("%d", &time_quantum); 
      printf("\nProcess ID\t\tBurst Time\t Turnaround Time\t Waiting Time\n");
      for(sum = 0, i = 0; x != 0;) 
      { 
            if(t[i] <= time_quantum && t[i] > 0) 
            { 
                  sum = sum + t[i]; 
                  t[i] = 0; 
                  c = 1; 
            } 
            else if(t[i] > 0) 
            { 
                  t[i] = t[i] - time_quantum; 
                  sum = sum + time_quantum; 
            } 
            if(t[i] == 0 && c == 1) 
            { 
                  x--; 
                  printf("\nProcess[%d]\t\t%d\t\t %d\t\t\t %d", i + 1, bt[i], sum - at[i], sum - at[i] - bt[i]);
                  wait_time = wait_time + sum - at[i] - bt[i]; 
                  turnaround_time = turnaround_time + sum - at[i]; 
                  c = 0; 
            } 
            if(i == n - 1) 
            {
                  i = 0; 
            }
            else if(at[i + 1] <= sum) 
            {
                  i++;
            }
            else 
            {
                  i = 0;
            }
      } 
      printf("\n\nAverage Waiting Time:\t%f", wait_time * 1.0 / n); 
      printf("\nAvg Turnaround Time:\t%f\n", turnaround_time * 1.0 / n); 
      return 0; 
}