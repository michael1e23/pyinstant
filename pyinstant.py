#!/usr/bin/env python

"""
	author : 'Michael Isik'
"""

import os
import inspect
import signal
import time
import logging
#from pprint import pprint


is_host = True
break_child = False
pipename = 'pyinstant_pipe'

class Launcher(object):
    def __init__(self):
        self.child_pids = []

    def show_help(self):
        help_string = """
    s : start new process (kills already started ones)
    k : kill started processes
"""
        print(help_string)

    def get_command(self):
        if False:
            read_pipe = open(pipename, 'r')
            s = read_pipe.read(1)
            read_pipe.read()
            read_pipe.close()
        else:
            #print("\n   type h-<enter> for help")
            s = raw_input('\npyinstant (h for help) :> ')
            s = s.strip()
        return s

    def kill(self):
        pids = self.child_pids
        print('killing old processes: {0}'.format(pids) )
        for pid in pids:
            os.kill(
                pid,
                signal.SIGTERM
            )


    def run(self,_level=0):
        global pipename
        global break_child
        global is_host
        logging.debug( "run(), ishost =", is_host )

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
            com = self.get_command()

            if com == '':
                continue
            elif 'kill'.startswith(com):
                self.kill()
                continue
            elif 'help'.startswith(com):
                self.show_help()
            elif s in ('s','sb'):
                logger.debug('spawning child')
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

                    a = stack[_level+1]
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








def run():
    l = Launcher()
    l.run(_level=1)


def trigger(condition,_level=0):
    if condition:
        global pipename
        write_pipe = open(pipename, 'w')
        write_pipe.write('\n')
        exit(0)
    else:
        run(_level=_level+1)




#def run(_level=0):
    #global pipename
    #global break_child
    #global is_host
    #print("run(), ishost =",is_host)

    #if not is_host:
        #if break_child:
            #import wingdbstub
        #return


    #try:
        #os.mkfifo(pipename)
    #except OSError:
        #pass


    #old_pid = None
    #while True:
        #if False:
            #read_pipe = open(pipename, 'r')
            #s = read_pipe.read(1)
            #read_pipe.read()
            #read_pipe.close()
        #else:
            #print("\n   type h-<enter> for help")
            #s = raw_input('MIC:> ')
            #s = s.strip()

        #if s == 'k':
            #print('killing old process: {0}'.format(old_pid) )
            #os.kill(old_pid,signal.SIGTERM)
            #continue
        #elif s in ('s','sb'):
            #print('spawning child')
            ##print('wait for short');time.sleep(1)
            #if old_pid is not None:
                #print('killing old process: ', old_pid )
                #os.kill(old_pid,signal.SIGTERM)
            #pid = os.fork()
            #if pid == 0:
                #is_host = False
                #if s == 'sb':
                    #break_child = True
                #stack = a = inspect.stack()
                #print('child stack')
                #for i in range(len(stack)):
                    #print(i,stack[i][1])

                #a = stack[_level+1]
                #fname = a[1]
                #frame = a[0]
                #globs = frame.f_globals
                #locs  = frame.f_locals
                #print( 'executing file:', fname )
                #execfile(
                    #fname,
                    #globs,
                    #locs,
                #)

            #elif pid > 0:
                #old_pid = pid






