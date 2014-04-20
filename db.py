import sqlite3 as lite
import random


class Database:
    def __init__(self, db_file):
        self.conn = lite.connect(db_file)
        self.cur = self.conn.cursor()
        with self.conn:
            try:
                print "Creating Tables"
                self.cur.execute(
                    'CREATE TABLE IF NOT EXISTS outlets (ip VARCHAR(16) PRIMARY KEY, name VARCHAR(64) UNIQUE, state1 Boolean, state2 Boolean, power VARCHAR(16));')

            except Exception, err:
                print ('Sqlite error creating tables: %s' % str(err))

    def IsOutlet(self, ip):
        with self.conn:
            try:
                self.cur.execute('INSERT INTO outlets VALUES(?,?,?,?,?)', [ip, 'New Outlet'+ str(random.randrange(99)),True, True, 0 ])
                return True
            except Exception, err:
                print ('Sqlite error in IsOutlet: %s' % str(err))
                return False

    def UpdatePower(self, ip, power):
        with self.conn:
            try:
                self.cur.execute('update outlets set power=(?) where ip=(?);', [power, ip])
                return True
            except Exception, err:
                print ('Sqlite error in UpdatePower: %s' % str(err))
                return False

    def GetState(self, ip):
        with self.conn:
            try:
                self.cur.execute('SELECT state1 FROM outlets where ip=(?);', [ip])
                data = self.cur.fetchall()
                return data[0][0]
            except Exception, err:
                print ('Sqlite error in GetAllMovies: %s\n' % str(err))

    def UpdateState(self, rowid, state):
        with self.conn:
            try:
                self.cur.execute('update outlets set state1=(?) where ROWID=(?);', [state, rowid])
                return True
            except Exception, err:
                print ('Sqlite error in UpdatePower: %s' % str(err))
                return False

    def GetOutlets(self):
        with self.conn:
            try:
                self.cur.execute('SELECT *, ROWID FROM outlets;')
                data = self.cur.fetchall()
                return data
            except Exception, err:
                print ('Sqlite error in GetAllMovies: %s\n' % str(err))

