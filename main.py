import random
randomnum = random.randint(1, 20)
while True:
  what = input()
  if what == "roll":
    print(randomnum)
