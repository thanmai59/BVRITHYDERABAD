def time_conversion(s):
    # YOUR CODE HERE
def convert24(str1):
    if str1[-2:] == "AM" andstr1[:2] == "12":
        return "00" + str[2:-2]
    elif str1[-2:] == "AM":
        return str1[:-2]
    elif str1[-2:] == "PM" and str1[:2] =="12":
        return str[:-2]
    else:
        return str(int(str1[:2]) + 12) + str1[2:8]

if __name__ == "__main__":
    s = input()
    result = time_conversion(s)
    # YOUR CODE HERE