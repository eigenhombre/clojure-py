from threading import Lock, local


def synchronized(f):
    """ Synchronization decorator. """
    lock = Lock()

    def synchronized_closure(*args, **kw):
        with lock:
            return f(*args, **kw)
    return synchronized_closure


class ThreadLocal(local):
    def __init__(self):
        pass

    def get(self, defaultfn):
        if not hasattr(self, "value"):
            self.value = defaultfn()
        return self.value

    def set(self, value):
        self.value = value


class AtomicInteger:### FIXME: old style class?!
    def __init__(self, v=0):
        self.v = v

    def getAndIncrement(self):
        self.v += 1
        return self.v
