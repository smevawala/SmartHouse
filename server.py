from socket import *
# import threading
import thread
import db


def handler(clientsock, addr):
    D = db.Database('db.db')
    ip = addr[0]
    print ip
    D.IsOutlet(ip)
    while 1:
        msg = clientsock.recv(BUFSIZ)
        while msg.find("e") == -1:
            print "last charater is", msg[-1]
            print len(msg)
            print 'Getting', str(msg)
            tempmsg = clientsock.recv(BUFSIZ)
            print tempmsg
            msg = msg+tempmsg
        print "recieved everything"
        msg = msg[:msg.find("e")]
        print 'Got', str(msg)
        D.UpdatePower(ip, msg)
        statemsg = D.GetState(ip)
        print statemsg
        if statemsg:
            sm = "1"
        else:
            sm = "0"
        sm = sm+'e'
        clientsock.send(sm)
        print sm
    # clientsock.close()
    # print "closing"

if __name__ == '__main__':
    PORT = 3000
    BUFSIZ = 4096
    serversock = socket(AF_INET, SOCK_STREAM)
    serversock.bind((gethostname(), PORT))
    serversock.listen(2)

    while 1:
        print 'waiting for connection...'
        clientsock, addr = serversock.accept()
        print '...connected from:', addr
        thread.start_new_thread(handler, (clientsock, addr))
