import psycopg2


class PgDataStore:
    def __init__(self, host: str = 'localhost',
                 port: int = 5432,
                 user: str = 'postgres',
                 db_name='python_list_dev',
                 pwd: str = None):
        self._host = host
        self._port = port
        self._user = user
        self._pwd = pwd
        self._db_name = db_name
        self._conn = psycopg2.connect(host=self._host,
                                      database=self._db_name,
                                      user=self._user,
                                      password='admin123')

    def close(self):
        self._conn.close()

    def store_pylint(self, data):
        sql = '''insert into 
                    pylint_metrics(name, module_name, n_refactor, n_convention, statement, global_note)
                values
                    (%(name)s,
                    %(module_name)s,
                    %(n_refactor)s,
                    %(n_convention)s,
                    %(statement)s,
                    %(global_note)s)
                    '''
        cur = self._conn.cursor()
        cur.executemany(sql, data)
        self._conn.commit()

    def store_pylint_by_msg(self, data: dict):
        sql = '''insert into 
        pylint_metrics_by_msg  
        (name, module_name, msg, code, n)
        values
        (%(name)s, %(module_name)s, %(msg)s, %(code)s, %(n)s)'''

        cur = self._conn.cursor()
        cur.executemany(sql, data)
        self._conn.commit()

    def store_git_metrics(self, data: dict):
        sql = '''
        insert into git_metrics
        (name, module_name, commit_digest, author, commited_at, commit_msg, lines_added, lines_removed, bug)
        VALUES
        (%(name)s, 
        %(module_name)s, 
        %(commit_digest)s, 
        %(author)s, 
        %(commited_at)s, 
        %(commit_msg)s, 
        %(lines_added)s, 
        %(lines_removed)s, 
        %(bug)s)'''

        cur = self._conn.cursor()
        cur.executemany(sql, data)
        self._conn.commit()

    def store_radon_raw_metrics(self, data: dict):
        sql = '''
            insert into 
                radon_raw_metrics (name, module_name, loc, lloc, single_comments, sloc, multi, comments, blank)
            values
                (%(name)s,
                %(module_name)s,
                %(loc)s,
                %(lloc)s,
                %(single_comments)s,
                %(sloc)s,
                %(multi)s,
                %(comments)s,
                %(blank)s
                )
                '''
        cur = self._conn.cursor()
        cur.executemany(sql, data)
        self._conn.commit()

    def store_radon_mi_metric(self, data: dict):
        sql = '''
            insert into 
                radon_mi_metric (name, module_name, mi)
            values
                (%(name)s,
                %(module_name)s,
                %(mi)s
                )
                '''
        cur = self._conn.cursor()
        cur.execute(sql, data)
        self._conn.commit()

    def store_radon_complexity_metrics(self, data: dict):
        sql = '''insert into 
                    radon_complexity_details(name, module_name, entity_name, type, complexity, rank, indentation, classname)
                values
                    (%(name)s,
                    %(module_name)s,
                    %(entity_name)s,
                    %(type)s,
                    %(complexity)s,
                    %(rank)s,
                    %(indentation)s,
                    %(classname)s
                    )'''
        cur = self._conn.cursor()
        cur.executemany(sql, data)
        self._conn.commit()

    def retrieve_v_by_msg_bugs(self, module_name):
        sql = """select module_name, msg, n, n_bugs from v_pylint_by_msg_to_bugs where module_name = '{module_name}'"""

        cur = self._conn.cursor()
        cur.execute(sql.format(module_name=module_name))
        data = cur.fetchall()
        return data


    def retrieve_distinct_msgs(self):
        sql = '''select distinct(msg) from v_pylint_by_msg_to_bugs'''
        cur = self._conn.cursor()
        cur.execute(sql)
        return cur.fetchall()

    def retrieve_distinct_module_names(self):
        sql = '''select distinct(module_name) from v_pylint_by_msg_to_bugs'''
        cur = self._conn.cursor()
        cur.execute(sql)
        return cur.fetchall()
