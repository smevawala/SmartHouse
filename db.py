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
                self.cur.execute('INSERT INTO outlets VALUES(?,?,?,?,?)', [ip, 'New Outlet'+ str(random.randrange(99)),True, True ])
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

    # def AddGenre(self, movie_id, genre_id, genre_name):
    #     with self.conn:
    #         try:
    #             self.cur.execute('INSERT INTO genres VALUES(?,?,?)', [movie_id, genre_id, genre_name])
    #             return True
    #         except Exception, err:
    #             print ('Sqlite error in AddGenre: %s' % str(err))
    #             return False

    # def AddPerson(self, person_id, person_name):
    #     with self.conn:
    #         try:
    #             self.cur.execute('INSERT INTO people VALUES(?,?,?,?,?)', [person_id, person_name, None, None, None])
    #             return True
    #         except Exception, err:
    #             print ('Sqlite error in AddPerson: %s' % str(err))
    #             return False

    # def AddCast(self, movie_id, person_id, order_num):
    #     with self.conn:
    #         try:
    #             self.cur.execute('INSERT INTO cast VALUES(?,?,?)', [movie_id, person_id, order_num])
    #             return True
    #         except Exception, err:
    #             print ('Sqlite error in AddCast: %s' % str(err))
    #             return False

    # def AddRottenCast(self, person_id, movie_id):
    #     with self.conn:
    #         try:
    #             self.cur.execute('INSERT INTO rottencast VALUES(?,?)', [person_id, movie_id])
    #             return True
    #         except Exception, err:
    #             print ('Sqlite error in AddRottenCast: %s' % str(err))
    #             return False

    # def AddRottenMovie(self, movie_id, movie_title, score, rotten_id, rotten_title, release_date):
    #     with self.conn:
    #         try:
    #             self.cur.execute('INSERT INTO rottenmovies VALUES(?,?,?,?,?,?)', [movie_id, movie_title, score, rotten_id, rotten_title, release_date])
    #             return True
    #         except Exception, err:
    #             print ('Sqlite error in AddRottenMovie: %s' % str(err))
    #             return False

    # def AddFeatureForMovie(self, movie_id, score, genre, release_date, production_id, director_mean, director_std, cast1_mean, cast1_std, cast2_mean, cast2_std, cast3_mean, cast3_std, cast4_mean, cast4_std, genre_mean, genre_std):
    #     with self.conn:
    #         try:
    #             self.cur.execute('INSERT INTO features VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',
    #                 [movie_id, score, genre, release_date, production_id, director_mean, director_std, cast1_mean, cast1_std, cast2_mean, cast2_std, cast3_mean, cast3_std, cast4_mean, cast4_std, genre_mean, genre_std])
    #             return True
    #         except Exception, err:
    #             print ('Sqlite error in AddFeatureForMovie: %s' % str(err))
    #             return False

    # def GetAllMovies(self):
    #     with self.conn:
    #         try:
    #             self.cur.execute('SELECT * FROM movies;')
    #             data = self.cur.fetchall()
    #             return data
    #         except Exception, err:
    #             print ('Sqlite error in GetAllMovies: %s\n' % str(err))

    # def GetAllPersonIdsNames(self):
    #     with self.conn:
    #         try:
    #             self.cur.execute('SELECT person_id, person_name FROM people;')
    #             data = self.cur.fetchall()
    #             return data
    #         except Exception, err:
    #             print ('Sqlite error in GetAllPersonIdsNames: %s\n' % str(err))

    # def GetAllGenreIdsNames(self):
    #     with self.conn:
    #         try:
    #             self.cur.execute('SELECT distinct genre_id, genre_name FROM genres;')
    #             data = self.cur.fetchall()
    #             return data
    #         except Exception, err:
    #             print ('Sqlite error in GetAllPersonIdsNames: %s\n' % str(err))

    # def GetGenresByMovieId(self, movie_id):
    #     with self.conn:
    #         try:
    #             self.cur.execute('SELECT genre_id FROM genres where movie_id = (?);', [movie_id])
    #             data = self.cur.fetchall()
    #             return data
    #         except Exception, err:
    #             print ('Sqlite error in GetAllPersonIdsNames: %s\n' % str(err))

    # def GetRottenCastByPersonId(self, person_id):
    #     with self.conn:
    #         try:
    #             self.cur.execute('SELECT person_id, movie_id FROM rottencast WHERE person_id = (?);', [person_id])
    #             data = self.cur.fetchall()
    #             return data
    #         except Exception, err:
    #             print ('Sqlite error in GetRottenCastByPersonId: %s\n' % str(err))


    # def GetRottenMovieByMovieId(self, movie_id):
    #     with self.conn:
    #         try:
    #             self.cur.execute('SELECT movie_id FROM rottenmovies WHERE movie_id = (?);', [movie_id])
    #             data = self.cur.fetchall()
    #             return data
    #         except Exception, err:
    #             print ('Sqlite error in GetRottenMovieByMovieId: %s\n' % str(err))

    # def GetRottenScoreByMovieId(self, movie_id):
    #     with self.conn:
    #         try:
    #             self.cur.execute('SELECT score FROM rottenmovies WHERE movie_id = (?);', [movie_id])
    #             data = self.cur.fetchall()
    #             return data
    #         except Exception, err:
    #             print ('Sqlite error in GetRottenScoreByMovieId: %s\n' % str(err))

    # def GetRottenScoresByPersonId(self, person_id):
    #     with self.conn:
    #         try:
    #             self.cur.execute('SELECT rottenmovies.score FROM rottenmovies inner join rottencast on rottenmovies.movie_id=rottencast.movie_id where rottencast.person_id = (?);', [person_id])
    #             data = self.cur.fetchall()
    #             return data
    #         except Exception, err:
    #             print ('Sqlite error in GetRottenScoresByPersonId: %s\n' % str(err))

    # def GetRottenScoresByGenreId(self, genre_id):
    #     with self.conn:
    #         try:
    #             self.cur.execute('SELECT rottenmovies.score FROM rottenmovies inner join genres on rottenmovies.movie_id=genres.movie_id where genres.genre_id = (?);', [genre_id])
    #             data = self.cur.fetchall()
    #             return data
    #         except Exception, err:
    #             print ('Sqlite error in GetRottenScoresByPersonId: %s\n' % str(err))

    # def GetCastStatsByMovieId(self, movie_id):
    #     with self.conn:
    #         try:
    #             self.cur.execute('SELECT c.order_num, p.mean_rating, p.std_rating FROM people p inner join cast c on p.person_id=c.person_id where c.movie_id = (?) order by c.order_num;', [movie_id])
    #             data = self.cur.fetchall()
    #             return data
    #         except Exception, err:
    #             print ('Sqlite error in GetCastStatsByMovieId: %s\n' % str(err))

    # def GetAllGenreStats(self):
    #     with self.conn:
    #         try:
    #             self.cur.execute('SELECT genre_id, count(*), mean_rating, std_rating from genres group by genre_id;')
    #             data = self.cur.fetchall()
    #             return data
    #         except Exception, err:
    #             print ('Sqlite error in GetAllFeatures: %s\n' % str(err))

    # def GetAllFeatures(self):
    #     with self.conn:
    #         try:
    #             self.cur.execute('SELECT * FROM features;')
    #             data = self.cur.fetchall()
    #             return data
    #         except Exception, err:
    #             print ('Sqlite error in GetAllFeatures: %s\n' % str(err))

    # def UpdatePersonScore(self, person_id, mean, std):
    #     with self.conn:
    #         try:
    #             self.cur.execute('update people set mean_rating=(?), std_rating=(?) where person_id=(?);', [mean, std, person_id])
    #             return True
    #         except Exception, err:
    #             print ('Sqlite error in UpdatePersonScore: %s' % str(err))
    #             return False

    # def UpdateGenreScore(self, genre_id, mean, std):
    #     with self.conn:
    #         try:
    #             self.cur.execute('update genres set mean_rating=(?), std_rating=(?) where genre_id=(?);', [mean, std, genre_id])
    #             return True
    #         except Exception, err:
    #             print ('Sqlite error in UpdatePersonScore: %s' % str(err))
    #             return False