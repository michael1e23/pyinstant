pyinstant
======

***Instantly start python script by skipping initialization procedures***

::

  import pyinstant

  if pyinstant.is_host:
      # my slow initialization

  pyinstant.run()

  # main code


example::

  import pyinstant

  if pyinstant.is_host:
      import time,os
      print('my slow initialization')
      time.sleep(3)

  pyinstant.run()

  while True:
      print('working proc' + os.getpid())
      time.sleep(1)



Installation
------------

Quick install::

   pip install pyinstant


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

