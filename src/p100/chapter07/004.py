try:
  result = 10 / 0
except ZeroDivisionError:
  print('ZeroDivisionError')
finally:
  print('処理を終了します')