#!/usr/bin/python

import subprocess

results = subprocess.run(["netctl", "list"], stdout=subprocess.PIPE)

processed_output = [x.strip() for x in results.stdout.decode('utf-8').split('\n') if x != '']

printable_list = [(x, False) if x[0] != '*' else (x[2:], True) for x in processed_output]

for i, profile in enumerate(printable_list):
  print('{}: {} {}'.format(i, profile[0], '[active]' if profile[1] == True else ''))

while True:
  try:
    text = input('Enter profile #, "q" to exit: ')
    if text.lower() == 'q':
      break
  except ValueError:
    print('Not a number')
