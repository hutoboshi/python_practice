for i in range(3):
  try:
    print("aiu", end="")
    1 / 0
  except ZeroDivisionError:
    break
  finally:
    print("eo")