from multiprocessing.connection import answer_challenge

import string
def cap_each_word(string1):
    if len(string1)<1:
        return string1
    result = ""
    word_array = string1.split(" ",)
    for x in word_array:
        if len(result)>0:
            result = result + " " + x.strip().capitalize()
        else:
            result = x.capitalize()
    if not result:
        reurn = string1
    else:
        return result
        
result1 ="how can mirrors be real if our eyes aren't real"
result = cap_each_word(result1)
print(result)

newStr = "it's going to be sunny"
def capitalize(string):
    answer = ""
    string2 = string.split()
    for elems in string2:
        #capitalize each word and add it to a string
        if len(answer)>0:
            answer = answer + " " + elems.strip().capitalize()
        else:
            answer = elems.capitalize()
        #if still is still empty return capitalized
        if not answer:
            return string
        else:
            return answer

    print(string2)
capitalize("It's going to be sunny")

example = "winning is a choice,lets go get it"
result = " ".join(x.capitalize() for x in example.split())
result2 = string.capwords(example)
print (result2)