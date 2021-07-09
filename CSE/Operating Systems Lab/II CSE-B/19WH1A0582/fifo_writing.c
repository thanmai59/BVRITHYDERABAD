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
    
    int fd = open("myfifo",O_WRONLY);
    if(fd == -1)
    return 1;
    int x = 97;
    if(write(fd,&x,sizeof(x)) == -1)
    return 2;
    printf("x value written into myfifo\n");
    close(fd);
}