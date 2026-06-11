import time

def binary_count(n):
  bits = []
  while n > 0:
    bits.append(n % 2)
    n //= 2
  return bits[::-1]



while True:
  v = input("How many times do you want to repeat binary count?")
  try:
    v = int(v)
    break
  except ValueError:
    print("Not a valid integer!")

start_time = time.perf_counter()

for i in range(v):
  print(binary_count(i))

end_time = time.perf_counter()

elapsed_time = end_time - start_time

if elapsed_time < 60:
  print(f"Elapsed Time: {elapsed_time} seconds")
elif elapsed_time < 3600:
  print(f"Elapsed Time: {elapsed_time} minutes")
elif elapsed_time < 3600 * 24:
  print(f"Elapsed Time: {elapsed_time} hours")
elif elapsed_time < 3600 * 24 * 7:
  print(f"Elapsed Time: {elapsed_time} days")
elif elapsed_time < 3600 * 24 * 7 * 30:
  print(f"Elapsed Time: {elapsed_time} weeks")
elif elapsed_time < 3600 * 24 * 7 * 30 * 12:
  print(f"Elapsed Time: {elapsed_time} months")
else:
  print(f"Elapsed Time: {elapsed_time} years")