
# Python code
# define hex values as a dictionary
hexNumbers = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
}
input_data=input("Please enter a hexadecimal value:")
hex_val=input_data.upper() #convert to upper case
print(hex_val)
#split the string into single char


# Converts a string hexadecimal number into an integer decimal
# If hexNum is not a valid hexadecimal number, returns None
#define the function to convert Hex to Int
def hexToDec(y):
    split_val=list(hex_val) #convert the input to List
    print(split_val) #print the list value
    # decimal convertion of input ..ABC is ..+(A*(16 power 2))+(B *(16 power 2))+(C*(16 power 0))
    power=0 #initialize to 0
    output=0
    index=len(split_val)-1 # set to the last value of index in the list
    for i in range(len(split_val)):
        val=hexNumbers[split_val[index]] #refer the hexNumbers to assign the integer value for the equivalent Hex input 
        output+=(16**power)*val; # calculate the integer/decimal value through the formula in iterations 
        index-=1 # iterate to the next value in reverse
        power+=1 # increase the power of 16 
    return output

print(hexToDec(hex_val))
