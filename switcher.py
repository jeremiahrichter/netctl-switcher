#!/usr/bin/python

import subprocess

print('Choose a profile to switch to:')

results = subprocess.run(["netctl", "list"], stdout=subprocess.PIPE)

processed_output = [x.strip() for x in results.stdout.decode('utf-8').split('\n')]

print(processed_output)
