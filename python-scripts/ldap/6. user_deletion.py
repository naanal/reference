#!/usr/bin/python
# -*- coding: utf-8 -*-
from ldap3 import Connection, Server, ALL, MODIFY_REPLACE

# define the server

s = Server('172.30.1.197', port=636, use_ssl=True, get_info=ALL)

admin_username = raw_input('Enter Admin Username....')
admin_password = raw_input('Enter Admin Password....')

#admin_username = 'Administrator@naanal.local'
#admin_password = 'p@ssw0rd1'

# define the connection

c = Connection(s, user=admin_username, password=admin_password)

c.bind()

c.start_tls()

if not c.bind():
    print 'Admin username/password Wrong'
else:
    username = raw_input('Enter Username to delete...')
    dn = 'cn= %s,ou=Police,dc=naanal,dc=local' % username
    c.delete(dn)
    print c.result

    c.unbind()
