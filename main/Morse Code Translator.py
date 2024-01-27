def morse_translator(text):
    # Morse code mapping
    morse_code_dict = {
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
    }

    # Your code goes here
    # Remember to consider both upper and lower case letters, and spaces
    # The function should return the translated Morse code string

    
    x=text.upper()
    #print(x)
    re1=""
    for i in range(0,(len(text))):
      
      u=x[i]
      
      if u>="A" and u<="Z":
       re1+=morse_code_dict[u]
       re1+=" "
      
      else:
          re1+="/"
    print(re1)
      
# Test cases
print(morse_translator("HELLO WORLD"))  # Expected output: ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."
print(morse_translator("Python"))  # Expected output: ".--. -.-- - .... --- -."
print( morse_translator("Morse Code"))  # Expected output: "-- --- .-. ... . / -.-. --- -.. ."
