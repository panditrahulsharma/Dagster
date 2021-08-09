
udp_sink_sdk
=====================

Class udp_sink_sdk.client() 
---------------

    This is the Lambda API Reference . The Lambda Developer Guide provides additional information. For the service overview,
    see What is Lambda , and for   information about how the service works, see Lambda: How it Works in the Lambda Developer Guide::
    
            import udp_sink_sdk
            ------------------------
                A Python interface for the udp_sink_sdk API.
                :param enviroment:
                    env. **REQUIRED**
                :param username:
                    The user_id of this API user. **REQUIRED**
                :param password:
                    The user_password of this API user. **REQUIRED**
                :param ssl_path:
                    The ssl_path for secure Authentication. **REQUIRED**
            ------------------------
            obj_sdk = udp_sink_sdk.client('env','username','password')
----------------
* These are the available methods:
     * _udp_sink_conn()
     * udp_sink_writer()

