def login (conn, username:str, password:str):
    try:
        conn.cursor()
        query = '''
            select username, password 
            from public.users
            where username = '{0}' and password = '{1}'
        '''.format(username, password)
        resQuery = conn.execute(query)
        resdata = resQuery.fectone()
        return resQuery, None
    except (Exception) as e:
        return None, e