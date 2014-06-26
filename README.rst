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
      print('child process at work: ' + os.getpid() + ' ' + str(i))
      time.sleep(1)



Workflow
------------

First you have a bare script.

dostuff.py::

  import time,os
  print('slow initialization')
  time.sleep(3)

  for i in range(3):
      print('process at work: ' + os.getpid() + ' ' + str(i))
      time.sleep(1)




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

