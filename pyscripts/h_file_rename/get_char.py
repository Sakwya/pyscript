output_str = " "
law_char = ['q', 'Q', 'w', 'W', 'e', 'E', 'r', 'R', 't', 'T', 'y', 'Y', 'u', 'U', 'i', 'I', 'o', 'O', 'p', 'P', 'a',
            'A', 's', 'S', 'd', 'D', 'f', 'F', 'g', 'G', 'h', 'H', 'j', 'J', 'k', 'K', 'l', 'L', 'z', 'Z', 'x', 'X',
            'c', 'C', 'v', 'V', 'b', 'B', 'n', 'N', 'm', 'M', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
while 1:
    input_str = input()
    if input_str == "~":
        break
    for i in range(0, len(input_str)):
        if input_str[i] in law_char:
            output_str += input_str[i]
        elif output_str[-1] == " ":
            continue
        else:
            output_str += " "

output = output_str.split(" ")
while "" in output:
    output.remove("")
print(output)
'''
str = "qwertyuiopasdfghjklzxcvbnm1234567890"
strr = []
for i in range(0, len(str)):
    strr += str[i]
    if str[i] in "qwertyuiopasdfghjklzxcvbnm":
        strr += str[i].upper()
print(strr)
'''
