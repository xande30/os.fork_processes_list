import os, time
from colorama import Fore
def counter(count):
	for i in range(count):
		time.sleep(1)
		print(Fore.MAGENTA,'[%s] ==> %s' %(os.getpid(),i))

for i in range(5):
	pid = os.fork()
	if pid != 0:
		print(Fore.MAGENTA,"Process %d spawned" % pid)
	else:
		counter(5)
		os._exit(0)

print(Fore.MAGENTA,"Main process exiting!")
