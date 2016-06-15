#!/usr/bin/python
# -*- coding: utf-8 -*-

from ldap3 import Server, Connection, SUBTREE, ALL, ALL_ATTRIBUTES, \
    ALL_OPERATIONAL_ATTRIBUTES


total_entries = 0
total_ou = 0

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
    c.search(search_base='dc=naanal,dc=local',
             search_filter='(objectClass=OrganizationalUnit)',
             search_scope=SUBTREE, attributes=[ALL_ATTRIBUTES,
             ALL_OPERATIONAL_ATTRIBUTES])

    total_entries += len(c.response)

    for entry in c.response:
        if entry.has_key('attributes'):
            total_ou += 1
            print entry['attributes']['ou']

    print ('Total entries retrieved:', total_entries)
    print ('Total Oraganizational Units:', total_ou)
