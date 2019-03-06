import sys

sys.path.append("C:\Python27\Lib\site-packages")
import redis
from redis.client import Redis, StrictRedis

# Fetching Host+Port
new_endpoint = "$(endpoint)".split(":")
host = new_endpoint[0]
port = new_endpoint[1]
print ("The host (of current DB) is: " + host)
print ("The port (of current DB) is: " + port)

# Connecting to the database and verifying
is_connected = False

try:
    r = redis.Redis(host=str(host), port=int(port), db=0, socket_timeout=10)
    # r = redis.Redis(host=str("pub-redis-10483.qa-us-east-1a.staging.redislabs.com"), port=int(19005), db=0,  socket_timeout=10)

    if r.ping():
        print("SUCCESS! A connection has been opened")
        assert r.set('foo', '123')
        assert r.get('foo') == ('123')
        print ("VERIFIED! A key has been added")
        is_connected = True
    ##set 100 keys##
    for i in range(0, 100):
        r.set(i, i)
except:
    print("FAILURE! A connection could not be opened")
    f1 = open('C:\\Program Files (x86)\\qfs\\qftest\\SIP.txt', 'w')
    f1.write('FAILURE! A connection could not be opened\n')
    sys.exit(1)
    f1.close()

# There is Enough keys?
if is_connected:
    DBsize = r.dbsize()
    print ("The number of keys: ", DBsize)
    if DBsize < 100:
        print ("There are not  enough keys in the DB")
        sys.exit(1)
    else:
        print ("All the expected keys exist in the DB")
