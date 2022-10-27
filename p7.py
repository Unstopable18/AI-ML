import os
try:
  print('try')
  os._exit(1)   # 0--> status code non-zero abnormal termination no need to worry about  0 value.
except ValueError:
  print('except')
finally:
  print('finally')