from django.db import connection


def GetParams(self):
    sql = ("select :dbid, name, value from v$parameter")
    named_params = {'dbid': self.dbid}
    self.cur.execute(sql, named_params)
    res = self.cur.fetchall()
    cursor = connection.cursor()
    cursor.executemany('INSERT OR REPLACE\n'
                       'INTO Parameters(dbid, name, value)\n'
                       'VALUES( ?, ?, ?)', res
                       )
