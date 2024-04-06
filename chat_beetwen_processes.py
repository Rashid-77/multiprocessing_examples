from multiprocessing import Process, Pipe
from time import sleep

  
def sender(conn, msgs): 
    """ 
    function to send messages to other end of pipe 
    """
    for msg in msgs: 
        conn.send(msg) 
        print(f"Sent the message: {msg}") 
        sleep(3)
    conn.close() 
  
def receiver(conn): 
    """ 
    function to print the messages received from other 
    end of pipe 
    """
    while True: 
        msg = conn.recv() 
        if msg == "END": 
            break
        print(f"Received the message: {msg}")
  
if __name__ == "__main__": 
    # messages to be sent 
    msgs = ["hello", "hey", "hru?", "END"] 
  
    # creating a pipe 
    parent_conn, child_conn = Pipe() 
  
    # creating new processes 
    p1 = Process(target=sender, args=(parent_conn,msgs)) 
    p2 = Process(target=receiver, args=(child_conn,)) 
  
    # running processes 
    p1.start() 
    p2.start() 
  
    # wait until processes finish 
    p1.join() 
    p2.join() 