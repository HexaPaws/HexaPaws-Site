import time

def binary_count(n):
  if n == 0:
    return [0]
  bits = []
  while n > 0:
    bits.append(n % 2)
    n //= 2
  return bits[::-1]

def ternary_count(n):
  if n == 0:
    return [0]
  bits = []
  while n > 0:
    bits.append(n % 3)
    n //= 3
  return bits[::-1]

def custom_count(n, base):
  if n == 0:
    return [0]
  bits = []
  while n > 0:
    bits.append(n % base)
    n //= base
  return bits[::-1]

while True:
  mode = input("Binary, Ternary Count, Custom or Quit? B / T / C / Q")


  if mode == "Q":
    break
  if mode == "B":
    while True:
      v = input("How many times do you want to repeat binary count?")
      try:
        v = int(v)
        break
      except ValueError:
        print("Not a valid integer!")
    for i in range(v):
      start_time = time.perf_counter()
      print(custom_count(i, basey))
      end_time = time.perf_counter()
      elapsed_time = end_time - start_time

  if mode == "T":
    while True:
      v = input("How many times do you want to repeat ternary count?")
      try:
        v = int(v)
        break
      except ValueError:
        print("Not a valid integer!")
    for i in range(v):
      start_time = time.perf_counter()
      print(ternary_count(i, basey))
      end_time = time.perf_counter()
      elapsed_time = end_time - start_time

  if mode == "C": # C means Custom
    while True:
      try:
        basey = int(input("What base number do you want?"))
        basey = int(basey)
        break
      except ValueError:
        print("Not a valid integer!")
    
    for i in range(basey):
      start_time = time.perf_counter()
      print(custom_count(i, basey))
      end_time = time.perf_counter()
      elapsed_time = end_time - start_time
      print(f"It took {elapsed_time} seconds to count.")






if elapsed_time < 60:
  print(f"Elapsed Time: {elapsed_time} seconds")
elif elapsed_time < 3600:
  print(f"Elapsed Time: {elapsed_time/60} minutes")
elif elapsed_time < 3600 * 24:
  print(f"Elapsed Time: {elapsed_time/3600} hours")
elif elapsed_time < 3600 * 24 * 7:
  print(f"Elapsed Time: {elapsed_time/3600/24} days")
elif elapsed_time < 3600 * 24 * 7 * 30:
  print(f"Elapsed Time: {elapsed_time/3600/24/7} weeks")
elif elapsed_time < 3600 * 24 * 7 * 30 * 12:
  print(f"Elapsed Time: {elapsed_time/3600/24/7/30} months")
else:
  print(f"Elapsed Time: {elapsed_time/3600/24/7/30/12} years")