import threading, queue, 

def producer(queue, event):

def consumer(queue,event, lock, exit):


q = queue.Queue()
lock = threading.Lock()
event = threading.Event()
poolsize = 2
consumers = []
exit = []

producer = threading.Thread(target=producer,args=(q,event))
producer.start()

for c in range(poolsize):
    consumer = threading.Thread(target =consumer, args=(q,event,lock,exit))

producer.join()
for consumer in consumers:
    consumer.join()

print(exit)