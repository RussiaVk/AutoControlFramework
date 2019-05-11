import stackless
def _init(_crack_Main,DEQUE):
	if DEQUE:run=lambda x:stackless.tasklet(_crack_Main)(x)
	else:run=lambda x:stackless.tasklet(_crack_Main)()
	return (run,('stackless.run()',))