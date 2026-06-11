vvvv = [0, 1]
lang = [0, 1]
prolang = [0, 1]
echo = [0, 1]
xxxx = [0, 1]
zzzz = [0, 1]
rrrr = [0, 1]
ffff = [0, 1]
adj = [0, 1]
fruits = [0, 1]
catlist = [0, 1]
spices = [0, 1]
elements = [0, 1]


aa = 0

for m in vvvv:
  for r in xxxx:
    for n in rrrr:
      for hxl in zzzz:
        for v in ffff:
          for w in catlist:
            for x in adj:
              for y in fruits:
                for yby in spices:
                   for e in lang:
                      for a in prolang:
                        for d in elements:
                          print(x, y, w, v, hxl, n, r, yby, e, y, a)
                          aa +=1
                          print(aa)

product_of_lengths = len(zzzz) * len(rrrr) * len(ffff) * len(adj) * len(fruits) * len(catlist) * len(echo) * len(xxxx) * len(vvvv) * len(spices) * len(prolang) * len(lang) * len()
print(f"Gave {product_of_lengths} codename results! Enjoy! 😺")
print("Starlace is always watching... ")
print("\U0001F63D")