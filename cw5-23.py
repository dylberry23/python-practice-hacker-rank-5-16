# Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.
# Examples

# "This is an example!" ==> "sihT si na !elpmaxe"
# "double  spaces"      ==> "elbuod  secaps"



def reverse_words(text):
  #go for it
    new = []
    for i in text.split(' '):
        new.append(i[::-1])
    return ' '.join(new)



print(reverse_words('I like to ride my  bicycle'))