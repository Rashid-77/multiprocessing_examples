'''
Depending on the platform, multiprocessing supports three ways to start 
a process. These start methods are:
- spawn. The child process will only inherit those resources necessary to run 
    the process object’s run() method. Available on POSIX and Windows platforms.
- fork. All resources of the parent are inherited by the child process. Note 
    that safely forking a multithreaded process is problematic.
    Available on POSIX systems.
- forkserver. When the program starts and selects the forkserver start method, 
    a server process is spawned. From then on, whenever a new process is needed,
    the parent process connects to the server and requests that it fork a new 
    process. The fork server process is single threaded unless system libraries 
    or preloaded imports spawn threads as a side-effect so it is generally safe 
    for it to use os.fork(). No unnecessary resources are inherited.Available 
    on POSIX platforms which support passing file descriptors over Unix pipes 
    such as Linux.
'''

import multiprocessing as mp


def foo(q):
    q.put('hello')

if __name__ == '__main__':
    mp.set_start_method('spawn')  # use only once in a program
    q = mp.Queue()
    p = mp.Process(target=foo, args=(q,))
    p.start()
    print(q.get())
    p.join()


''' Alternatively, you can use get_context() to obtain a context object. 
 Context objects have the same API as the multiprocessing module, 
 and allow one to use multiple start methods in the same program.
'''
# if __name__ == '__main__':
#     ctx = mp.get_context('spawn')
#     q = ctx.Queue()
#     p = ctx.Process(target=foo, args=(q,))
#     p.start()
#     print(q.get())
#     p.join()