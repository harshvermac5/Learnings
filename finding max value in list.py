words = [
    "gem",
    "sword",
    "shield",
    "potion",
    "coins",
    "gem",
    "sword",
    "gem"
]

nums = [
    1,
    2,
    3,
    4,
    3,
    5,
    5,
    3,
    6
]

most_words = max(words) #returns the highest value in list alphabetically
print(most_words)

most_words_1 = max(words, key=words.count) #returns the most occurred value in list
print(most_words_1)

most_nums = max(nums) #returns the highest integer value in list
print(most_nums)

most_nums_1 = max(nums, key=nums.count) #returns the maximum occurances of integer value in list
print(most_nums_1)