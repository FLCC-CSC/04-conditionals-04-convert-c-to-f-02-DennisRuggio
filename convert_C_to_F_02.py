# FILE NAME - convert_C_to_F_02.py

# NAME: Dennis Ruggio
# DATE: 10/1/25
# BRIEF DESCRIPTION: convert_C_to_F_02.py lab



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience



########## ENTER YER CODE BELOW THIS LINE ##########

def main():
    C_and_F_convert()

def C_and_F_convert():
    print('===== Temperature Converter =====')
    print()
    print('  1. Convert from Celsius to Fahrenheit')
    print('  2. Convert from Fahrenheit to Celsius')
    print()
    choice = float(input('Please choose from the above menu: '))

    if choice == 1:

        Celsius = float(input('Enter a temperature to convert: '))
        converted = Celsius * 9/5 + 32
        print()
        print(f'{Celsius} degrees Celsius is {converted} degrees Fahrenheit.')

    else:
        Fahrenheit = int(input('Enter a temperature to convert: '))
        converted = (Fahrenheit - 32) * 5/9
        print()
        print(f'{Fahrenheit} degrees Fahrenheit is {converted} degrees Celsius.')

main()








########### END YER CODE ABOVE THIS LINE ###########

    



########################################
#          SAMPLE OUTPUT
########################################

'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 1
Enter a temperature to convert: 100

100.0 degrees Celsius is 212.0 degrees Fahrenheit.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 2
Enter a temperature to convert: 32

32.0 degrees Fahrenheit is 0.0 degrees Celsius.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 1
Enter a temperature to convert: -40

-40.0 degrees Celsius is -40.0 degrees Fahrenheit.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 2
Enter a temperature to convert: -40

-40.0 degrees Fahrenheit is -40.0 degrees Celsius.
'''

########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What is one lesson you learned in this lab?

Utilizing the ability to convert and creating different formulas for different choices.
Also definitely making sure you have everything accurate because the first time I did the code I had 6 = instead of 5 starting the Temperature Converter line.
And definitely paying attention to the amount of spaces before choices 1 and 2. Oops!




'''
