import hashlib

event_ids = [123, 456]
cache_key = "cloudapp_eois_"+str(hashlib.md5(','.join(map(str, event_ids)).encode('utf-8')).hexdigest())

print("cache_key:{}".format(','.join(map(str, event_ids)).encode('utf-8')))
print("cache_key:{}".format(cache_key))