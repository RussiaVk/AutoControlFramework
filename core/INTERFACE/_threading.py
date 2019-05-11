import threading
def _init(_crack_Main,DEQUE):
	if DEQUE:run=lambda x:threading.Thread(target=_crack_Main,args=(x,)).start()
	else:run=lambda x:threading.Thread(target=_crack_Main).start()
	return (run,('pass',))