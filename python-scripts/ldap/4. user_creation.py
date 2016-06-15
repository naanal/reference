#!/usr/bin/python
# -*- coding: utf-8 -*-
from ldap3 import Connection, Server, ALL, MODIFY_REPLACE



s = Server('172.30.1.197', port=636, use_ssl=True, get_info=ALL)
admin_username = raw_input('Enter Admin Username....')
admin_password = raw_input('Enter Admin Password....')


#admin_username = 'Administrator@naanal.local'
#admin_password = 'p@ssw0rd1'

c = Connection(s, user=admin_username, password=admin_password)
c.bind()
c.start_tls()

if not c.bind():
    print 'Admin username/password Wrong'
else:
    username = raw_input('Enter Username for new user...')
    password = raw_input('Enter Password for %s ....' % username)

    dn = 'cn= %s,ou=Police,dc=naanal,dc=local' % username

    c.add(dn, ['Top', 'person', 'user'],
          {'cn': username, 'userPrincipalName': '%s@naanal.local'
          % username, 'sAMAccountName': username})

    unicode_pass = unicode('"' + password + '"', 'iso-8859-1')
    password_value = unicode_pass.encode('utf-16-le')

    c.modify(dn, {'unicodePwd': [(MODIFY_REPLACE, [password_value])]})

    c.modify(dn, {'userAccountControl': [(MODIFY_REPLACE, ['512'])]})

    print c.result

    c.unbind()
