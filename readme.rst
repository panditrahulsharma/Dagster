udp_sink_sdk
=====================

1. Class udp_sink_sdk.client(env,username,password,ssl_cert)
---------------
     A Python interface for the udp_sink_sdk API
        enviroment:
            env. **REQUIRED**
        username:
            The user_id of this API user. **REQUIRED**
        password:
            The user_password of this API user. **REQUIRED**
        ssl_path:
            The ssl_path for secure Authentication. **REQUIRED**


2. These are the available methods
--------------------
     * _udp_sink_conn(**kwargs)
     * udp_sink_writer(**kwargs)

3. _udp_sink_conn(database_name,schema_name):
--------------------
      Create a connection,
      
      parameters endpoints
         A dictionary containing the connection information that is host,port and protocol. **REQUIRED**
      database_name
         The name of your database of up to 64 alphanumeric characters. If you do not provide a name,
         sdk doesn't create a connection in presto.  **REQUIRED**
      schema_name
         The name for your schema of up to 64 alphanumeric characters. **REQUIRED**
      returns
         A sqlalchemy_engine connection.

      _udp_sink_conn function will return presto_engine connection::

          return {"is_conn":True,"msg":"connection established Success..","engine_presto":engine_presto}

         
4. udp_sink_write(database_name,schema_name,table_name,df,mode="append"):
--------------------
      insert dataframe into deltatable::
      
         obj.udp_sink_write(database_name,
            schema_name,
            table_name,
            df,
            mode="append"
            )      

      database_name
         The name of your database of up to 64 alphanumeric characters. If you do not provide a name,
         sdk doesn't create a connection in presto.  **REQUIRED**
      schema_name
         The name for your schema of up to 64 alphanumeric characters. **REQUIRED**
      table_name
         The name of your table_name in which you are creating or inserting the data. **REQUIRED**
      df(pandas Dataframe)
         The Dataframe that you want to insert into the table **REQUIRED**
      mode::
      
         provide mode according to the requirement **REQUIRED**
          - fail If table exists, do nothing.
          - replace If table exists, drop it, recreate it, and insert data.
          - append If table exists, insert data. Create if does not exist.



            
