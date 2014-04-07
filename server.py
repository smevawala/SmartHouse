from socket import *
import threading
import thread
import db



def handler(clientsock,addr):
    D=db.Database('db.db')
    ip=addr[0]
    D.IsOutlet(ip)
    while 1:
        msg=clientsock.recv(BUFSIZ)
        if not msg:
            break
        print 'Got', msg
        D.UpdatePower(ip, msg)
        clientsock.send("turn relay on")
    clientsock.close()

if __name__=='__main__':
    PORT = 3000
    BUFSIZ = 4096
    # ADDR = (HOST, PORT)
    serversock = socket(AF_INET, SOCK_STREAM)
    serversock.bind((gethostname(), PORT))
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
