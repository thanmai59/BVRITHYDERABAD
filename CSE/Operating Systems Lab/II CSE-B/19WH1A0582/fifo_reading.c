#include <stdio.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <errno.h>
#include <stdlib.h>

int main()
{
    if(mkfifo("myfifo",0777) == -1)
        printf("Fifo Creation Error\n");
    printf("MYFIFO Created Successfully \n");
    
    int fd = open("myfifo",O_RDONLY);
    if(fd == -1)
    return 1;
    int x;
    if(read(fd,&x,sizeof(x)) == -1)
    return 2;
    printf("x value read from myfifo is : %d\n",x);
    close(fd);
}