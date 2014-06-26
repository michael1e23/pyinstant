pyinstant
======

**Instantly start python script by skipping initialization procedures**

Your initialization will be run just once.
After that, you can fork children that are already initialized.
You can even modify the scripts main code without
needing to restart your script.
It will be dynamically reloaded and
no repeated initialization will be executed.
Only restart your script if initialization code changed.

::

  import pyinstant

  if pyinstant.is_host:
      # my slow initialization

  pyinstant.run()

  # main code


Example::

  import pyinstant

  if pyinstant.is_host:
      import time,os
      print('this is the host session process, pid={0}'.format(os.getpid()))
      print('slow initialization')
      time.sleep(3)

  # will start a host loop that waits for user input
  pyinstant.run()

  # only forked children will come this far
  for i in range(3):
      print('child process at work: {0} {1}'.format(os.getpid(),i)
      time.sleep(1)



Workflow
------------

First you have a bare script.

dostuff.py::

  import time,os
  print('slow initialization')
  time.sleep(3)

  for i in range(3):
      print('process at work: {0} {1}'.format(os.getpid(),i))
      time.sleep(1)
  print('exiting')

When you call it::

  > python dostuff.py
  slow initialization
  process at work: 10922 0
  process at work: 10922 1
  process at work: 10922 2
  exiting

(Step 1) Then you instantify it to::

  import pyinstant                    # <- line 1 of 3
  if pyinstant.is_host:               # <- line 2 of 3
      import time,os
      print('slow initialization')
      time.sleep(3)

  pyinstant.run()                     # <- line 3 of 3

  for i in range(3):
      print('process at work: {0} {1}'.format(os.getpid(),i))
      time.sleep(1)
  print('exiting')


(Step 2) Then you run the new script::

  > python dostuff.py
  slow initialization

  pyinstant (h for help) :> h

      s : start new process (kills already started ones)
      k : kill started processes
      v : toggle verbosity
      h : show this help string
      q : quit
      d : (experimental) debug new process
          kills already started ones
          currently only wingide is supported


  pyinstant (h for help) :> s

     *** new child spawned ***
  process at work: 10946 0
  process at work: 10946 1
  process at work: 10946 2
  exiting


  pyinstant (h for help) :> s

     *** new child spawned ***
  process at work: 10947 0
  process at work: 10947 1
  process at work: 10947 2
  exiting


  pyinstant (h for help) :> s

     *** new child spawned ***
  process at work: 10948 0
  process at work: 10948 1
  process at work: 10948 2
  exiting


(Step 3) Modify your script, but don't leave your session.
::

  import pyinstant
  if pyinstant.is_host:
      import time,os
      print('slow initialization')
      time.sleep(3)

  pyinstant.run()

  for i in range(3):
      print('my changed line')        # the changed line
      time.sleep(1)
  print('exiting')


(Step 4) Start a new child in your old session.
The changes will be dynamically reloaded.
::

  pyinstant (h for help) :> s

     *** new child spawned ***
  my changed line
  my changed line
  my changed line
  exiting




(Step 5) Quit the session::

  pyinstant (h for help) :> q
  killing old processes: [10948]
  shutting down session




Installation
------------

Quick install::

  cd /path/to/myscript
  wget https://raw.githubusercontent.com/michael1e23/pyinstant/master/pyinstant.py


Developer::

  python setup.py develop --user


Administrator::

  python setup.py install


User::

  python setup.py install --user


:Name: pyinstant
:Author: Michael Isik
:Email: isikmichael@gmx.net
:URL: https://github.com/michael1e23/pyinstant
:License: GNU General Public License v3 or later (GPLv3+)

