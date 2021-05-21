import sys
import random as rand

if __name__ == "__main__":                      #加密
    if len(sys.argv) > 2:
        seedValue = int(sys.argv[1])
        data = list(sys.argv[2])
        rand.seed(seedValue)
        rand.shuffle(data)
        print("".join(data))


if __name__ == "__main__":                      #解密
    if len(sys.argv) > 2:
        seedValue = int(sys.argv[1])
        data = list(sys.argv[2])
        lst = list(len(data))
        result = []
        for i in data:
            for j in lst:
                if data[i] == data[j]:
                    tmp = data[i]
                    data[i] = data[j]
                    data[j] = tmp
                    result.append(tmp)
    print(tmp)
print()