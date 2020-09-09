

def count_total():

    number = int(input("請輸入大於0的正整數"))
    list_number = [i for i in range(1, number+1)]
    list_del = []

    for i, item in enumerate(list_number):
        if (item%15 != 0) and (item%3 == 0 or item%5 == 0):
            list_del.append(list_number[i])
        else:
            continue

    return len(list_number) - len(list_del)
        


if __name__ == '__main__':
    print(count_total())
