from multiprocessing import Pool
def _init(_crack_Main,DEQUE,THREADS_NUM):
	pool=Pool(THREADS_NUM)
	return (lambda x:pool.apply_async(_crack_Main),('pool.close();pool.join()',))