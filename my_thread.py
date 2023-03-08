import threading
import queue
import ast
import logging
import uuid

result_queue = {}
lock = threading.Lock()

logger = logging.getLogger("test")

def tally_dicts(rows: list, index: int, uuid: str):
    print("index={}, uuid={}, rows:{}".format(index, uuid, rows))
    tally = {}
    
    for row in rows:
        for key in row:
            
            value = row[key]

            logger.info("thread={}, value:{}, type={}".format(threading.current_thread().name,value, type(value)))

            try:

                if isinstance(value,list) or (isinstance(value,str) and (value[0:1] == '[' and value[-1:] == ']')):
                    if isinstance(value,str):
                        values = ast.literal_eval(value)

                    for val in values:
                        if val in tally:
                            tally[val] += 1
                        else:
                            tally[val] = 1

                else:
                    
                    if value in tally:
                        tally[value] += 1
                    else:
                        tally[value] = 1
            
            except Exception as ex:
                print("Current thread name: {}, error={}".format(threading.current_thread().name, ex))

    print("tally:{}".format(tally))
    # result_queue.put(tally)
    with lock:
        (result_queue[uuid]).insert(index,tally)

def tally_dicts_multithreaded(dicts, num_threads=4):

    new_uuid = uuid.uuid4()

    result_queue[new_uuid] = []

    # Split the list of dicts into equal-sized chunks
    chunk_size = int(len(dicts) / num_threads)
    chunks = [dicts[i:i + chunk_size] for i in range(0, len(dicts), chunk_size)]

    # Create a thread for each chunk of dicts
    threads = []
    for i in range(num_threads):
        chunk_data = chunks[i]
        print("i={}, chunk_data:{}".format(i,chunk_data))
        t = threading.Thread(name='tally-'+str(i), target=tally_dicts, args=([chunk_data]), kwargs={'index':i, 'uuid':new_uuid})
        threads.append(t)

    # Start all the threads
    for t in threads:
        t.start()

    # Wait for all the threads to finish
    for t in threads:
        t.join()
    

    # Combine the tallies from each thread
    tallies = {}
    # for t in threads:
    #     tally = tally_result[i]
    #     print("thread tally:{}".format(tally))
    #     for key, value in tally.items():
    #         tallies[key] = tallies.get(key, 0) + value

    print("result_queue.size:{}".format(len(result_queue[new_uuid])))

    for result in result_queue[new_uuid]:
        print("result:{}".format(result))

        for key, value in result.items():
            tallies[key] = tallies.get(key, 0) + value
    
    return tallies

tallies = tally_dicts_multithreaded([{'name':'folau','age':20,'city':['la','le']},{'name':'lisa','age':10,'city':'san'},
                           {'name':'folau','age':30,'city':'la'},{'name':'folau','age':20,'city':'la'},{'name':'folau','age':20,'city':'la'},{'name':'lisa','age':10,'city':'san'},
                           {'name':'folau','age':30,'city':'la'},{'name':'folau','age':20,'city':'la'}])

print("tallies:{}".format(tallies))