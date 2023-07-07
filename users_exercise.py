users = {
  "Jonathan": {
    "twitter": "jonnyt",
    "lottery_numbers": [6, 12, 49, 33, 45, 20],
    "home_town": "Stirling",
    "pets": [
    {
      "name": "fluffy",
      "species": "cat"
    },
    {
      "name": "fido",
      "species": "dog"
    },
    {
      "name": "spike",
      "species": "dog"
    }
  ]
  },
  "Erik": {
    "twitter": "eriksf",
    "lottery_numbers": [18, 34, 8, 11, 24],
    "home_town": "Linlithgow",
    "pets": [
    {
      "name": "nemo",
      "species": "fish"
    },
    {
      "name": "kevin",
      "species": "fish"
    },
    {
      "name": "spike",
      "species": "dog"
    },
    {
      "name": "rupert",
      "species": "parrot"
    }
  ]
  },
  "Avril": {
    "twitter": "bridgpally",
    "lottery_numbers": [12, 14, 33, 38, 9, 25],
    "home_town": "Dunbar",
    "pets": [
      {
        "name": "monty",
        "species": "snake"
      }
    ]
  }
}

# 1. Get Jonathan's Twitter handle (i.e. the string `"jonnyt"`)
print(users["Jonathan"]["twitter"])
# 2. Get Erik's hometown
print(users["Erik"]["home_town"])
# 3. Get the list of Erik's lottery numbers
print(users["Erik"]["lottery_numbers"])
# 4. Get the species of Avril's pet Monty
print(users["Avril"]["pets"][0]["species"])
# 5. Get the smallest of Erik's lottery numbers
erik_sorted_lotto_numbers = sorted(users["Erik"]["lottery_numbers"])
# above creates a new variable, creates a sorted list of Erik's lottery numbers
print(erik_sorted_lotto_numbers[0]) #index 0 will be the smallest number

# 6. Return an list of Avril's lottery numbers that are even
avril_lottery_numbers = users["Avril"]["lottery_numbers"]
avril_even_numbers =[] #creating an empty list to store Avril's even numbers
for number in avril_lottery_numbers:
    if number % 2 == 0:
    # runs throughs avril's lottery numbers, checks if the numbers are divisable by 2 with no remainder
    # (this will return even numbers)
        avril_even_numbers.append(number) #store that number in Avril's even number list

print(avril_even_numbers)
# 7. Erik is one lottery number short! Add the number `7` to be included in his lottery numbers
users["Erik"]["lottery_numbers"].append(7)
print(users["Erik"]["lottery_numbers"])

# 8. Change Erik's hometown to Edinburgh
users["Erik"]["home_town"] = "Edinburgh"
# Sets a new assignment ("Edinburgh") to Erik's hometown
print(users["Erik"]["home_town"])

# 9. Add a pet dog to Erik called "fluffy"
users["Erik"]["pets"].append(
    {
    "name":"fluffy",
    "species":"dog"
    }
)
print(users["Erik"]["pets"])
# 10. Add another person to the users dictionary
users["Mark"] = {
    "twitter": "MarkR",
    "lottery_numbers": [1, 3, 37, 32, 12, 20],
    "home_town": "Penicuik",
    "pets": [
        {
            "name": "mr. snuffles",
            "species": "dog"
        },
        {
            "name": "snowbell",
            "species": "cat"
        }
    ]
}
# Note to self, remember the comma (,) and the end of a key-value pair (unless it's the last item)
print(users["Mark"])