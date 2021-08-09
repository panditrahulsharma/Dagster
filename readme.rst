udp_sink_sdk
=====================

1. Class udp_sink_sdk.client(env,username,password,ssl_cert)
---------------
    * A Python interface for the udp_sink_sdk API
        :param enviroment:
            env. **REQUIRED**
        :param username:
            The user_id of this API user. **REQUIRED**
        :param password:
            The user_password of this API user. **REQUIRED**
        :param ssl_path:
            The ssl_path for secure Authentication. **REQUIRED**


2. These are the available methods
--------------------
     * _udp_sink_conn(**kwargs)
     * udp_sink_writer(**kwargs)

3. _udp_sink_conn(self,database_name,schema_name)
--------------------
      Create a connection,
      
      parameters endpoints
         A dictionary containing host,port,protocol connection information. **REQUIRED**
      param host
         extracting the host from udp endpoints according to the env. **REQUIRED**
      param port
         extracting the port from udp endpoints according to the env. **REQUIRED**
      param protocol
         extracting the protocol from udp endpoints according to the env. **REQUIRED**
      param user_id
         The user_id of this API user. **REQUIRED**
      param user_password
         The user_password of this API user. **REQUIRED**
      param database_name
         The name for your database of up to 64 alphanumeric characters. If you do not provide a name,
         sdk doesn't create a connection in presto that you are creating.  **REQUIRED**
      param schema_name
         The name for your schema of up to 64 alphanumeric characters. **REQUIRED**
      param ssl_path
         The ssl_path for secure Authentication according to the env. **REQUIRED**
      returns
         A sqlalchemy_engine connection.

      _udp_sink_conn function will return presto_engine connection::

          return {"is_conn":True,"msg":"connection established Success..","engine_presto":engine_presto}

         

            
