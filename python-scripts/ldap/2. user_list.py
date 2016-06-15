#!/usr/bin/python
# -*- coding: utf-8 -*-
from ldap3 import Server, Connection, SUBTREE, ALL, ALL_ATTRIBUTES, \
    ALL_OPERATIONAL_ATTRIBUTES

total_entries = 0
total_user = 0

# define the server

s = Server('172.30.1.197', port=389, use_ssl=False, get_info=ALL)

admin_username = raw_input('Enter Admin Username....')
admin_password = raw_input('Enter Admin Password....')

# admin_username = "Administrator@naanal.local"
# admin_password = "p@ssw0rd1"

# define the connection

c = Connection(s, user=admin_username, password=admin_password)

c.bind()

if not c.bind():
    print 'Admin username/password Wrong'
else:
    c.search(search_base='dc=naanal,dc=local',
             search_filter='(&(objectCategory=person)(objectClass=user))',
             search_scope=SUBTREE, attributes=[ALL_ATTRIBUTES,
             ALL_OPERATIONAL_ATTRIBUTES])

    total_entries += len(c.response)

    for entry in c.response:
        if entry.has_key('attributes'):
            total_user += 1
            print entry['attributes']['cn']
    print ('Total entries retrieved:', total_entries)
    print ('Total Users retrieved:', total_user)
    c.unbind()