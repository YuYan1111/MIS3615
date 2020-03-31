def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False
        # the funtion made jusdement base on the first letter.
        # The first letter deceide it is T or F. test only last one
        
def any_lowercase2(s):
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'
        # when c is lower case it will return true
        #the result is T in anyway
        
def any_lowercase3(s):
    for c in s:
        flag = c.islower()
    return flag
        # last lette decide T or F
        # The result should be faulse as the last letter is lowercase
def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag
        # with appearance of lowervcase letter, retuen T

def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
    return True
    # with appearance of uppercase letter, retuen F

#question 2

def rotate_word(rotate,shift):
    rotate_word= ''
    for c in rotate:
        rotate_word += chr(ord(c) + shift)
    return rotate_word    
print(rotate_word('cheer', 7))
print(rotate_word('IBM', -1))


string = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

def decipher(string):
    new_string = ''
    for char in string:
    if char == 'y':
        new_string += 'a'
    elif char == 'z':
         new_string += 'b'
    elif ord(char) >= 97 and ord(char) <= 120:
         new_string += char(ord(chard)+2)
    else:
        new_string += cHAR
return new_string

# this question is toooooooo hard