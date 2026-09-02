#TASK
s = input("Enter String:")
print("Length:",len(s))
print("First Char:",s[0])
print("Last Char:",s[-1])
print("Upper Case:",s.upper())
print("Contains powerful?:","powerful" in s)

#CHALLENGE
sentence = input("Enter Sentence:")
vowel_count = 0
consonants_count = 0
vowel = 'aeiouAeiou'
for x in sentence:
    if x in vowel:
        vowel_count+=1
    elif x.isalpha():
        consonants_count+=1
print("Vowel count:",vowel_count)
print("consonant count:",consonants_count)      
