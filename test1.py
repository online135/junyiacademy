space = ' '
string1 = 'abcdefg'
string2 = 'Hello my name is kevin'

"""
Question 1

"""

def reverseStringA(string):
    return string[::-1]

def reverseStringB(string):
    string_list2 = []
    string_list1 = string.split(' ')

    for item in string_list1:
        string_list2.append(item[::-1])

    return space.join(string_list2)

if __name__ == "__main__":
    print(reverseStringA(string1))
    print(reverseStringB(string2))
    
