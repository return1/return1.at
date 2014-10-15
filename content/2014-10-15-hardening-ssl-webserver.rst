Hardening Your Web Server’s SSL Ciphers
#############################################
:date: 2014-10-15 18:03
:category: Server
:tags: apache2, nginx, ssl, security
:slug: hardening-your-web-servers-ssl-ciphers
:Status: draft

Just archiving the actual required web server configs:

* disable SSL 2.0 (FUBAR) and SSL 3.01 (POODLE),
* disable TLS 1.0 compression (CRIME),
* disable weak ciphers (DES, RC4), prefer modern ciphers (AES), modes (GCM), and protocols (TLS 1.2).

**Nginx**

.. code-block:: nginx
    
    ssl_prefer_server_ciphers On;
    ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
    ssl_ciphers ECDH+AESGCM:DH+AESGCM:ECDH+AES256:DH+AES256:ECDH+AES128:DH+AES:ECDH+3DES:DH+3DES:RSA+AESGCM:RSA+AES:RSA+3DES:!aNULL:!MD5:!DSS;

**Apache2**

.. code-block:: apache

    SSLProtocol ALL -SSLv2 -SSLv3
    SSLHonorCipherOrder On
    SSLCipherSuite ECDH+AESGCM:DH+AESGCM:ECDH+AES256:DH+AES256:ECDH+AES128:DH+AES:ECDH+3DES:DH+3DES:RSA+AESGCM:RSA+AES:RSA+3DES:!aNULL:!MD5:!DSS
    SSLCompression Off