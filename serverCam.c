/*
    Socket du server Camera

    compilation : gcc -o serveurCam serverCam.c (remplacer gcc par le cross-compilateur pour le faire fonctionner depuis la Rapsberry
*/

#include<stdio.h>
#include<string.h>    
#include<sys/socket.h>
#include<arpa/inet.h> 
#include<unistd.h>   

#define PORT 8002


int main(int argc , char *argv[])
{
    int socket_desc , client_sock , c , read_size;
    struct sockaddr_in server , client;
    char client_message[5 * sizeof(char)];

    //Create socket
    socket_desc = socket(AF_INET , SOCK_STREAM , 0);
    if (socket_desc == -1)
    {
        printf("Could not create socket");
    }
    puts("Socket created");

    //Prepare the sockaddr_in structure
    server.sin_family = AF_INET;
    server.sin_addr.s_addr = INADDR_ANY;
    server.sin_port = htons( PORT );

    //Bind
    if( bind(socket_desc,(struct sockaddr *)&server , sizeof(server)) < 0)
    {
        //print the error message
        perror("bind failed. Error");
        return 1;
    }
    puts("bind done");

    //Listen
    listen(socket_desc , 3);

    //Accept and incoming connection
    puts("Waiting for incoming connections...");
    c = sizeof(struct sockaddr_in);

    //accept connection from an incoming client
    client_sock = accept(socket_desc, (struct sockaddr *)&client, (socklen_t*)&c);
    if (client_sock < 0)
    {
        perror("accept failed");
        return 1;
    }
    puts("Connection accepted");

    //Receive a message from client
    while( (read_size = read(client_sock , client_message , sizeof(client_message))) > 0 )
    {
        //Get Picture Size
        FILE *picture;
        picture = fopen("image.jpg", "r");
        int size;

        fseek(picture, 0, SEEK_END);
        size = ftell(picture);

        //First message sent to the client is the Picture Size
        write(client_sock, &size, sizeof(size));

        //Return to the beginning of the picture
        fseek(picture, 0, SEEK_SET);

        int size_bis = 1;
        char send_buffer[size_bis];
        //Send Picture as Byte Array

        while(!feof(picture)) {
            //Reading a byte of the picture, and sending it through the socket
            fread(send_buffer, 1, sizeof(send_buffer), picture);
            write(client_sock, send_buffer, sizeof(send_buffer));
            bzero(send_buffer, sizeof(send_buffer));
        }
    }

    if(read_size == 0)
    {
        puts("Client disconnected");
        fflush(stdout);
    }
    else if(read_size == -1)
    {
        perror("recv failed");
    }

    return 0;
}
