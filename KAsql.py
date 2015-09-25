import pymysql

def query_SQL(sql):
    con = False
    rows = []
    try:
        con = pymysql.connect(host='localhost', port=3307, user='root', passwd='', db='ortho')
        with con:
            cur = con.cursor()
            database = 'USE ortho;'
            print database
            cur.execute(database)
            #sql = 'SELECT DISTINCT(yelp_id) FROM business;' 
            #print(sql)
            cur.execute(sql)
            rows = cur.fetchall()
            #print('business id from table: ',rows, type(rows))
    except pymysql.Error, e:
        print "Error %d: %s" % (e.args[0],e.args[1])
        sys.exit(1)
    finally:
        if con:
            con.close()
    return rows  
