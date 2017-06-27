#  Chris Nixon | 6/27/2017
# chris@devnix.io

import os

directory = ' '   #Input whatever directory you need files changed in.

[os.rename(os.path.join(directory, f), os.path.join(directory, f).replace(' ', '_').upper()) for f in os.listdir(directory)]
