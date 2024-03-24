from pkg import openConnection
import datastore

# import function datasore

def login(username: str, password: str):
    try:
        conn = openConnection()
        resLogin, err = datastore.login(conn, username, password)
        if err != None:
            raise Exception(err)
        
        if resLogin["username"] != username:
            raise Exception("username tidak ditemukan")
        print(resLogin)
        return resLogin, None
        
    except Exception as e:
        return None, e
            
    

    
