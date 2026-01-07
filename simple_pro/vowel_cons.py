print("WELCOMRE HERE..!")
def vowconst(user_input):
    #define vowel
    vowel = "aeiouAEIOU"
    vowelcount = 0
    conscount = 0
    for eachchar in user_input:
        if eachchar.isalpha():
            if eachchar in vowel:
                vowelcount += 1
            else:
                conscount += 1
    return vowelcount, conscount
user_input = input("Enter a string: ")
vowel, conscount = vowconst(user_input)
print(f" vowel is :{vowel}\n conscount is :{conscount}")
            
