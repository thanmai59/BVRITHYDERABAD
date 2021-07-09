#include<stdio.h>
#include<string.h>
int main()
{
    char pn[10][10],t[10];
    int arr[10],bur[10],serv[10],finish[10],tat[10],wt[10],i,j,n,temp;
    int totwt=0;
    printf("Enter the number of processes:");
    scanf("%d",&n);
    for(i=0; i<n; i++)
    {
        printf("Enter the ProcessName, Arrival Time& Execution Time:");
        scanf("%s%d%d",&pn[i],&arr[i],&bur[i]);
    }
    for(i=0; i<n; i++)
    {
        for(j=0; j<n; j++)
        {
            if(arr[i]<arr[j])
            {
                temp=arr[i];
                arr[i]=arr[j];
                arr[j]=temp;
                temp=bur[i];
                bur[i]=bur[j];
                bur[j]=temp;
                strcpy(t,pn[i]);
                strcpy(pn[i],pn[j]);
                strcpy(pn[j],t);
            }
	}
    }
    for(i=0; i<n; i++)
    {
        if(i==0)
            serv[i]=arr[i];
        else
        serv[i]=finish[i-1];
        wt[i]=serv[i]-arr[i];
        finish[i]=serv[i]+bur[i];
        tat[i]=finish[i]-arr[i];
    }
    printf("\nPName \tArrival time\t Execution time \t Service Time");
    for(i=0; i<n; i++)
    {
        printf("\n%s\t\t%d\t\t%d\t\t%d\t\t",pn[i],arr[i],bur[i],serv[i]);
        totwt+=wt[i];
     }
    printf("\nAverage Waiting time:%f\n",(float)totwt/n);
    return 0;
}
