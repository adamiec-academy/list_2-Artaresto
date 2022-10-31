def cipher(text, shift):
    
    for i in range(len(text)):
        letter = (text[i])
        
        if (letter.isupper()):
            text += chr(ord(letter) + shift)
        else:
            text += chr(ord(letter) + shift)
    
    return text

def decipher(text, shift):

    for i in range(len(text)):
        letter = (text[i])
        
        if (letter.isupper()):
            text += chr(ord(letter) - shift)
        else:
            text += chr(ord(letter) - shift)

    return text
