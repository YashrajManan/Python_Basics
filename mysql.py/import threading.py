import threading

counter = 0

def inc(n):
    global counter
    for _ in range(n):
        # Non-atomic: read -> modify -> write (can interleave!)
        counter += 1
        
        
threads = [threading.Thread(target=inc, args=(100_000,)) for _ in range(2)]
[t.start() for t in threads]
[t.join() for t in threads]


print("Counter:",counter)