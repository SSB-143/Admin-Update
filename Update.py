import os, platform


os.system('git pull')

bit = platform.architecture()[0]

if bit == '64bit':

    import Sarfraz2

elif bit == '32bit':

    import Dump32
