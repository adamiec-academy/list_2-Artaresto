def cipher(text, shift):
    
    text_after = ""
    
    for i in range(len(text)):
        letter = (text[i])
        
        if (letter.isupper()):
            text_after += chr(ord(letter) + shift)
        else:
            text_after += chr(ord(letter) + shift)
    
    return text_after

def decipher(text, shift):
    
    text_after = ""

    for i in range(len(text)):
        letter = (text[i])
        
        if (letter.isupper()):
            text_after += chr(ord(letter) - shift)
        else:
            text_after += chr(ord(letter) - shift)

    return text_after
