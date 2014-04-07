from socket import *
import threading
import thread



def handler(clientsock,addr):
    while 1:
        msg=clientsock.recv(BUFSIZ)
        if not data:
            break
        print 'Got', msg
        clientsock.send("turn relay on")
    clientsock.close()

if __name__=='__main__':
    SPORT = 3000
    BUFSIZ = 4096
    # ADDR = (HOST, PORT)
    serversock = socket(AF_INET, SOCK_STREAM)
    serversock.bind((gethostname(), SPORT))
    serversock.listen(2)

    while 1:
        print 'waiting for connection...'
        clientsock, addr = serversock.accept()
        print '...connected from:', addr
        # msg=clientsock.recv(BUFSIZ)
        # print 'Got', msg
        # clientsock.send("turn relay on")
        # clientsock.close();
        thread.start_new_thread(handler, (clientsock, addr))
