#!/usr/bin/env/python3

with open ("input1") as f:
	lines = f.readlines()

tmpsum = 0; sumlines = []
for i in lines:
	if len(i.strip()) != 0:
		tmpsum += int(i.strip())
	else:
		sumlines.append(tmpsum)
		tmpsum = 0

top3 = 0
for i in range(3):
	top3 += sorted(sumlines)[-(i+1)]

print("[+] Part 1: ", sorted(sumlines)[-1])
print("[+] Part 2: ", top3)
