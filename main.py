sentence = input('Enter a sentence:\n')  # Input a string sentence
c = sentence.strip().lower().split()  # Strip any spaces/characters at the beginning and
# spaces/character at the end, lowercase the stripped
# sentence Split the lowercased sentence into single words
# and returns a list
pig_latin_list = []  # Create a new list to append the new sentence
for x in c:  # Iterate over
    # If the word begins with a vowel, append 'way' at the end
    if x[0] in 'aeiou':
        y = x + 'way'  # Concatenate 'way' at the end of the word
        pig_latin_list.append(y)  # Append the words into the new list created

    # if the word begins with a sequence of consonants, the sequence must be moved to the end,
    # prefixed with 'a' and suffixed by 'ay'
    else:
        z = 0  # assigning vowel position to zero index
        for w in x:
            if w in 'aeiou':
                z = x.find(w)  # Find()
                break
            else:
                pass
        p = x[z:] + 'a' + x[:z] + 'ay'  # Slicing words using index numbers and Concatenate the words
        # with 'a' and 'ay'
        pig_latin_list.append(p)  # Append the words into the new list created

pig_latin_string = ""

# Change the pig_list into string
for elem in pig_latin_list:
    pig_latin_string += str(elem) + ' '  # this is for when the list contains an integer, it
    # will change it into a string, The empty quotes are
    # for creating spaces between words

print(pig_latin_string)  # print the new sentence
