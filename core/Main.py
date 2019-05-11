#!/usr/bin/env python
# -*- coding: utf-8 -*-
from types import FunctionType,MethodType     
from colorama import Fore, Back, Style
from greenlet import greenlet
from retry import retry
from tqdm import tqdm
import stackless,time,sys,datetime
DEBUG,INFO,ERROR,ERRORRESULT,TRAFFIC_IN,TRAFFIC_OUT,WARNING =Fore.GREEN+"[DEBUG] ",Fore.GREEN+"[INFO] ",Fore.RED+"[ERROR] ",Style.BRIGHT+Fore.CYAN+"[RESULT] ",Back.MAGENTA + "[TRAFFIC IN] ",Fore.MAGENTA+"[TRAFFIC OUT] ",Fore.YELLOW + "[WARNING] "
class AutoControlFramework(object):
	def __init__(self,THREADS_NUM=10,CONCURRENCY_TYPE=1,VERBOSE=True):
		self.CONCURRENCY_TYPE,self.THREADS_NUM,self.verbose=CONCURRENCY_TYPE,THREADS_NUM,VERBOSE

	def _initPbar(self,*args,**kwargs):self._returnPbar=tqdm(kwargs);return self.returnPbar

	@property   
	def returnPbar(self):return self._returnPbar

	@staticmethod
	def _showPbar(pbarObject,fontType='DEBUG',value='',info='cracking：\t'):
		try:pbarObject.write(''.join((eval(fontType),str(value),Style.RESET_ALL)))
		except AttributeError:sys.stdout.write(''.join(('\r',eval(fontType),info,str(value),Style.RESET_ALL)))
		except Exception as e:sys.stdout.write(type(e))
		else:pbarObject.update() 

	def _AutoMain(self,_crack_Main,DEQUE,initPbarArgs={},CRACK_QEQUE_SLICE=False,END_FOUC=None,END_FOUCArgs=(),verbose=True):
		StartTime=time.perf_counter()
		if verbose:print("[*] starting at "+str(StartTime))
		if initPbarArgs:
			if  isinstance(initPbarArgs['returnPbarFouc'],greenlet):initPbarArgs['returnPbarFouc'].switch(self._initPbar(initPbarArgsx.pop('returnPbarFouc'))) 
			elif isinstance(initPbarArgs['returnPbarFouc'],FunctionType):initPbarArgs['returnPbarFouc'](self._initPbar(initPbarArgs.pop('returnPbarFouc')))
			
		import sys,os
		sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
##################################################################      
		if self.CONCURRENCY_TYPE is 1:#run,EXECUTE=lambda x:stackless.tasklet(_crack_Main)(x),('stackless.run()',)
			from .INTERFACE._stackless import _init
##################################################################      
		elif self.CONCURRENCY_TYPE is 2:#run,EXECUTE=lambda x:threading.Thread(target=_crack_Main,args=(x,)).start(),('pass',)
			from .INTERFACE._threading import _init
##################################################################      
		elif self.CONCURRENCY_TYPE is 3:pass# windows system are not support multiprocessing
################################################################## 
		run,EXECUTE= _init(_crack_Main,DEQUE)
		try:
			if CRACK_QEQUE_SLICE:[run(DEQUE[i]) for i in range(self.THREADS_NUM)]
			else:[run(0) for i in range(self.THREADS_NUM)]
		#except IndexError as e:
		except Exception as e:
			if verbose:print(sys._getframe().f_code.co_name,e)
		else:
			try:exec(EXECUTE[0])
			except IndexError as e:print(e);pass
			except NameError as e:
				print(locals())
				print(e);pass
			except Exception as e:
				if self.verbose:print(sys._getframe().f_code.co_name,e)
			#else:
			finally:
				if not END_FOUC is None:
					if isinstance(END_FOUC,greenlet):EXECUTE='END_FOUC.switch()'
					elif isinstance(END_FOUC,FunctionType):EXECUTE='END_FOUC()'
					if END_FOUCArgs:EXECUTE=EXECUTE.replace(')','END_FOUCArgs)')
					try:exec(EXECUTE)
					except Exception as e:
						if self.verbose:print(sys._getframe().f_code.co_name,e)
					#else:
					#finally:
		finally:FinishedTime=time.perf_counter();print(''.join(("[*] finished at",str(FinishedTime),'==========total take ',str(FinishedTime-StartTime),'S')))

if __name__ == '__main__' :

	def a(a):
		print(a)
	b=[15,456,76,58,798,679,436666]
	AutoControlFramework(3,1)._AutoMain(a,b,CRACK_QEQUE_SLICE=True)

