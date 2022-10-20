
import redis
from datetime import timedelta

r = redis.Redis(host='127.0.0.1', port=6379, db=0)

key = 'test-name'
name = 'Folau'

r.setex(key, timedelta(hours=12),  value=name)

response = r.get(key)

print("response:{}".format(response))