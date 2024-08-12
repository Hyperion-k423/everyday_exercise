f = open("word.txt.txt", "r", encoding="UTF-8")
x = f.read()
y = x.count("itheima")
print(f"itheima出现了{y}次")
f.close()


fr = open("bill.txt", "r", encoding="UTF-8")
fw = open("billback.txt", "r", encoding="UTF-8")
for line in fr:
    line = line.strip()
    if line.split(",") == "测试":
        continue
    fw.write(line)
    fw.write("\n")
fr.close()
fw.close()
