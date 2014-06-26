#!/usr/bin/env python

"""
	__author__ = 'Michael Isik'
"""

from pprint import pprint
import os
import inspect
import signal
import time

is_host = True
break_child = False
pipename = 'quickstarterpipe'

def trigger(condition,level=0):
    if condition:
        global pipename
        write_pipe = open(pipename, 'w')
        write_pipe.write('\n')
        exit(0)
    else:
        run(level=level+1)
    
    


def run(level=0):
    global pipename
    global break_child
    global is_host
    print("run(), ishost =",is_host)
    
    
    if not is_host:
        if break_child:
            import wingdbstub
        return
    
        
    try:
        os.mkfifo(pipename)
    except OSError:    
        pass
    
    
    old_pid = None
    while True:
        if False:
            read_pipe = open(pipename, 'r')
            s = read_pipe.read(1)
            read_pipe.read()
            read_pipe.close()
        else:
            s = raw_input('\nMIC:>')
            s = s.strip()

        if s == 'k':
            print('killing old process: ', old_pid )
            os.kill(old_pid,signal.SIGTERM)
            continue
        elif s in ('s','sb'):            
            print('spawning child')
            #print('wait for short');time.sleep(1)
            if old_pid is not None:
                print('killing old process: ', old_pid )
                os.kill(old_pid,signal.SIGTERM)
            pid = os.fork()
            if pid == 0:
                is_host = False
                if s == 'sb':
                    break_child = True
                stack = a = inspect.stack()
                print('child stack')
                for i in range(len(stack)):
                    print(i,stack[i][1])
                    
                a = stack[level+1]
                fname = a[1]
                frame = a[0]
                globs = frame.f_globals
                locs  = frame.f_locals
                print( 'executing file:', fname )
                execfile(
                    fname,
                    globs,
                    locs,
                )
            
            elif pid > 0:
                old_pid = pid
                time.sleep(.2)
                pass




    
        
