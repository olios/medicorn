from sys import argv
from subprocess import Popen

if argv[1] == "start":
    Popen(['/usr/bin/python', 'run_service.py', 'start', '&', '>>', '/dev/null'])
#    print("starting")
else:
    Popen(['/usr/bin/python', 'run_service.py', 'stop'])
#    print("stopping")
    Popen(['/usr/bin/killall', 'python'])

