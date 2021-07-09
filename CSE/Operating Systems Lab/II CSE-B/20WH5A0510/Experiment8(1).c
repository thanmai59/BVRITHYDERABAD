#include <stdio.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <errno.h>
#include <stdlib.h>

int main()
{
    int mkret;
    mknod("myfif0",S_IFIFO|0666,0);
    if((mkret == -1) && (errno != EEXIST))
    {
        perror("mknod creation failed\n");
        exit(0);
    }
    printf("MyFIFO Created Successfully\n");
    int fifofd = open("myfifo",O_WRONLY);
    write(fifofd,"Hello World",sizeof("Hello World"));
    close(fifofd);
    
    return 0;
}