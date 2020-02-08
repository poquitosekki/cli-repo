#!/usr/bin/env python3
import math

def main(n):
	for i in range(3):
		print(i)
	return f"Sqrt : {math.sqrt(n)}"

if __name__ == '__main__':
	print(main(int(input("Select N : "))))
