#!/usr/bin/python

import subprocess

results = subprocess.run(["netctl", "list"], stdout=subprocess.PIPE)

processed_output = [x.strip() for x in results.stdout.decode('utf-8').split('\n') if x != '']

printable_list = [(x, False) if x[0] != '*' else (x[2:], True) for x in processed_output]

while True:
  try:
    for i, profile in enumerate(printable_list):
      print('{}: {} {}'.format(i + 1, profile[0], '[active]' if profile[1] == True else ''))
    text = input('Enter profile #, "q" to exit: ')
    if text.lower() == 'q':
      break
    else:
      number = int(text) - 1
      if number < 0 or number > len(printable_list):
        print('Number out of range')
      else:
        subprocess.run(['sudo', 'netctl', 'switch-to', printable_list[number][0]])
        break
  except ValueError:
    print('Not a number')
