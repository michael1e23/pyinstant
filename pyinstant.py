#!/usr/bin/env python

__author__ = "Michael Isik"


import os
import inspect
import signal
import time
import logging
#from pprint import pprint


is_host = True
debug_child = False
pipename = 'pyinstant_pipe'

class Launcher(object):
    def __init__(self):
        self.child_pids = []

    def show_help(self):
        help_string = """
    s : start new process (kills already started ones)
    k : kill started processes
    v : toggle verbosity
    h : show this help string
    q : quit
    d : (experimental) debug new process
        kills already started ones
        currently only wingide is supported
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
        for pid in pids:
            os.kill(
                pid,
                signal.SIGTERM
            )

        self.child_pids = []


    def run( self, _level ):
        global debug_child
        global is_host
        global pipename

        #logging.debug( "run(), ishost =", is_host )

        if not is_host:
            if debug_child:
                import wingdbstub
            return


        if False:
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
                print( 'killing old processes: {0}'.format(self.child_pids) )
                self.kill()
                continue


            elif 'quit'.startswith(com):
                print( 'killing old processes: {0}'.format(self.child_pids) )
                self.kill()
                print( 'shutting down session' )
                exit(0)

            elif 'help'.startswith(com):
                self.show_help()

            elif 'verbose'.startswith(com):
                l = logging.getLogger()
                if l.level == logging.DEBUG:
                    l.setLevel(logging.WARN)
                    print('verbose mode disabled')
                else:
                    l.setLevel(logging.DEBUG)
                    print('verbose mode enabled')
                #self.show_help()

            elif 'start'.startswith(com):
                logging.debug('killing old processes')
                self.kill()
                logging.debug( 'spawning new child' )
                self.launch_child( _level=_level+1 )

            elif 'debug'.startswith(com):
                logging.debug('killing old processes')
                self.kill()
                logging.debug('spawning new child in debug mode')
                self.launch_child( _level=_level+1, debug=True )



    def launch_child(self,_level,debug=False):
        global is_host
        global debug_child

        pid = os.fork()
        if pid == 0:
            is_host = False

            if debug:
                debug_child = True

            stack = inspect.stack()

            #print('child stack')
            #for i in range(len(stack)):
            #    print(i,stack[i][1])

            rec = stack[_level+1]
            fname = rec[1]
            frame = rec[0]
            globs = frame.f_globals
            locs  = frame.f_locals

            logging.debug( 'executing file: ' + fname )

            print(
                '\n\n   *** new child spawned{0} ***'.format(
                    ' (debug mode)' if debug else ''
                )
            )
            execfile(
                fname,
                globs,
                locs,
            )
        elif pid > 0:
            self.child_pids.append(pid)




def run():
    l = Launcher()
    l.run(_level=1)


class _initcode_class:
    def __enter__(self):
        raise Exception('skipit')
        return None

    def __exit__(self, type, value, traceback):
        l = Launcher()
        l.run(_level=1)

        return False

    def __call__(self):
        return self


initcode = _initcode_class()


#def trigger(condition,_level=0):
    #if condition:
        #global pipename
        #write_pipe = open(pipename, 'w')
        #write_pipe.write('\n')
        #exit(0)
    #else:
        #run(_level=_level+1)





