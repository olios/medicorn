from sys import argv
from subprocess import Popen

if argv[1] == "start":
    Popen(['/usr/bin/mplayer', 'siren.mp3'])
    Popen(['firefox','emerg.html'])
#    print("starting")
else:
    Popen(['/usr/bin/killall', 'mplayer'])
    Popen(['/usr/bin/killall', 'firefox'])

