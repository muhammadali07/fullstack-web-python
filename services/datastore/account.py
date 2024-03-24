def login (conn, username:str, password:str):
    try:
        print(username, password)
        cur = conn.cursor()
        query = '''
            select username, password 
            from public.users
            where username = '{0}' and password = '{1}'
        '''.format(username, password)
        resQuery = cur.execute(query)
        resdata = resQuery.fetchone()
        print(resdata)
        return resdata, None
    except Exception as e:
        return None, e