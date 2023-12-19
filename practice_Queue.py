from queue import Queue
import time
import uuid
queue = Queue()

def generate_request():
    request = {'id':uuid.uuid4()}
    queue.put(request)
    print (f"Request with id: {request['id']} is succesfuly addet to Queue")
 


def process_request():
    if not queue.empty():
        request = queue.get()
        print (f"Request with id: {request['id']} is processed")
    else:
        print ('Queue is empty')

while True:
    generate_request()
    time.sleep(1) #додав зупинку 1 сек, для повільнішого потоку
    process_request()    
    time.sleep (2) #додав зупинку 2 сек, для повільнішого потоку
