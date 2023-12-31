# For the following list of numbers:

numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]

# 1. Print out a list of the even integers:
even_integers = []
for number in numbers:
    if number % 2 == 0:
        even_integers.append(number)

print(even_integers)

# 2. Print the difference between the largest and smallest value:
lowest_number = None
highest_number = None
# Setting as an empty value
for number in numbers:
    if highest_number == None or number > highest_number:
        highest_number = number
        # If the highest number is an empty value, or if the number is greater than the highest number,
        # Then replace it
    if lowest_number == None or number < lowest_number:
        lowest_number = number
        # If the lowest number is empty, or if the number is less than the lowest number,
        # Then replace it

print(highest_number - lowest_number)
# after Googling, found the max()  function exists, but I wanted to do it in the for loop anyway.
# i.e. could have done print(max(numbers) - min(numbers))

# 3. Print True if the list contains a 2 next to a 2 somewhere.
previous_number = None
two_next_to_two = False
for number in numbers:
    if number == previous_number and number == 2:
        two_next_to_two = True
    previous_number = number

print(two_next_to_two)

# 4. Print the sum of the numbers, 
#    BUT ignore any section of numbers starting with a 6 and extending to the next 7.
#    
#    So [11, 6, 4, 99, 7, 11] would have sum of 22

# Psuedocode:
# sum variable (total sum of sequence), starts as 0
# check_6 variable that when enabled, checks if the number is a 6, starting off True
# check_7 variable that when enabled, checks if the number is a 7, starting off False
# for number in numbers
    # if check_6 is true:
        # if number != 6
            # add to total
        # else
            # disable check_6 and enable check_7
    # if check 7 is true:
        # if number == 7
            # disable check_7 and reenable check_6

# UPDATE: Realised we didn't need two variables for checking 6 or 7.
# If we're not looking for 6, then we're looking for 7
# sum of the sequence

sum_of_sequence = 0
check_for_6 = True
# Checking for 6 when True, checking for 7 when False

for number in numbers:
    if check_for_6 == True:
        if number != 6:
            sum_of_sequence += number
        else:
            check_for_6 = False
    if check_for_6 == False:
        if number == 7:
            check_for_6 = True

print(sum_of_sequence)

# 5. HARD! Print the sum of the numbers. 
#    Except the number 13 is very unlucky, so it does not count.
#    And numbers that come immediately after a 13 also do not count.
#    HINT - You will need to track the index throughout the loop.
#
#    So [5, 13, 2] would have sum of 5. 

# Pseudocode:
# Sum of non-13 sequence variable
# found_13 variable, set to False by default (we haven't found it yet)
# for number in numbers:
    # If 13 has not been found previously and number != 13
        #add to total
    # If the number == 13
        #set found_13 to true
    # If the number != 13 and we found 13 previously
        #set to found_13 to be false

sum_of_sequence_ignoring_13_and_number_after = 0
found_13_last_number = False

for number in numbers:
    if found_13_last_number == False and number != 13:
        sum_of_sequence_ignoring_13_and_number_after += number
    if number == 13:
        found_13_last_number = True
    if number != 13 and found_13_last_number == True:
        found_13_last_number = False

print(sum_of_sequence_ignoring_13_and_number_after)