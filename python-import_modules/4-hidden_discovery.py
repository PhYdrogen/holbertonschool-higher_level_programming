#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    res = dir(hidden_4)
    for i in range(len(res)):
        if res[i][0] == "_":
            continue
        print("{}".format(res[i]))
