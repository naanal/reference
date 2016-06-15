from ldap3 import Connection, Server, ALL
s = Server('172.30.1.197', get_info=ALL)
username = raw_input("Enter Username....")
password = raw_input("Enter Password....")
c = Connection(s, user=username, password=password)
if not c.bind():
    print('Failed', c.result)
else:
    print('Successful')
