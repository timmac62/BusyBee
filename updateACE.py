#!/usr/bin/env python
#
# very simple script which copies my busyBee.py version controlled source
# to code.py to execute tne AdaFruit Circuit Board Express with the update code
#
import shutil

src_file = "./busyBee.py"
dst_file = "/Volumes/CIRCUITPY/code.py"

shutil.copy(src_file, dst_file)
print(f"updating ACE - src:{src_file} dst:{dst_file}")
