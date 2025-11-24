from queue import Queue

def pageFaults(pages, n, capacity):

    frames = set()      # To quickly check if page exists
    q = Queue()         # FIFO queue
    faults = 0

    for i in range(n):

        page = pages[i]

        # HIT → already present
        if page in frames:
            continue

      
        faults += 1

        if len(frames) < capacity:
            frames.add(page)
            q.put(page)

        else:
            oldest = q.get()
            frames.remove(oldest)

            frames.add(page)
            q.put(page)

    return faults


if __name__ == '__main__':
    pages = [7, 0, 1, 2, 0, 3, 0, 
                4, 2, 3, 0, 3, 2]
    n = len(pages)
    capacity = 4

    print(pageFaults(pages, n, capacity))

