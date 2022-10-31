def cipher(text, shift):
    
    text_after = ""

    for i in range(len(text)):
        letter = (text[i])
        
        if letter == " ":
            text_after += " "
        elif (letter.isupper()):
            text_after += chr((ord(letter) + shift - 65) % 26 + 65)
        else:
            text_after += chr((ord(letter) + shift - 97) % 26 + 97)
    
    return text_after

def decipher(text, shift):
    
    text_after = ""

    for i in range(len(text)):
        letter = (text[i])
        
        if letter == " ":
            text_after += " "
        elif (letter.isupper()):
            text_after += chr((ord(letter) - shift - 65) % 26 + 65)
        else:
            text_after += chr((ord(letter) - shift - 97) % 26 + 97)

    return text_after
