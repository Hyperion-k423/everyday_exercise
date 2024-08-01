qian = 10000
for i in range(1, 21):
    import random

    fen = random.randint(1, 10)
    if fen < 5:
        print(f"{i}jixiaofen{fen},bufa")
        continue

    if qian >= 1000:
        qian -= 1000
        print(f"yuangong{i},fagongzi1000,gongzishnegyu{qian}")
    else:
        print(f"qianbugou,yue{qian}")

        break
