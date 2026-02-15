

# Rotor wirings
rotor_1 = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
rotor_2 = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
rotor_3 = "BDFHJLCPRTXVZNYEIWGAKMUSQO"
reflector = "YRUHQSLDPXNGOKMIEBFZCWVJAT"

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

rotor_1_pos = 0
rotor_2_pos = 0
rotor_3_pos = 0

plugboard_dict = {'A': 'B', 'B': 'A', 'C': 'D', 'D': 'C'}

def plugboard(letter):
    if letter in plugboard_dict:
        return plugboard_dict[letter]
    else:
        return letter

def rotor_forward(letter, rotor, position):

    index = alphabet.index(letter)
    
    index = (index + position) % 26
    
    new_letter = rotor[index]
    
    new_index = alphabet.index(new_letter)
    new_index = (new_index - position) % 26
    
    return alphabet[new_index]

def rotor_backward(letter, rotor, position):
    index = alphabet.index(letter)

    index = (index + position) % 26
    
    letter_to_find = alphabet[index]
    new_index = rotor.index(letter_to_find)
    
    new_index = (new_index - position) % 26
    
    return alphabet[new_index]

def reflector_func(letter):
    index = alphabet.index(letter)
    return reflector[index]

def rotate_rotors():
    global rotor_1_pos, rotor_2_pos, rotor_3_pos
    
    rotor_1_pos = rotor_1_pos + 1
    
    if rotor_1_pos >= 26:
        rotor_1_pos = 0
        rotor_2_pos = rotor_2_pos + 1
    
    if rotor_2_pos >= 26:
        rotor_2_pos = 0
        rotor_3_pos = rotor_3_pos + 1
    
    if rotor_3_pos >= 26:
        rotor_3_pos = 0

def encrypt_letter(letter):
    if letter not in alphabet:
        return letter
    rotate_rotors()
    
    letter = plugboard(letter)
    
    letter = rotor_forward(letter, rotor_1, rotor_1_pos)
    letter = rotor_forward(letter, rotor_2, rotor_2_pos)
    letter = rotor_forward(letter, rotor_3, rotor_3_pos)
    
    letter = reflector_func(letter)
    
    letter = rotor_backward(letter, rotor_3, rotor_3_pos)
    letter = rotor_backward(letter, rotor_2, rotor_2_pos)
    letter = rotor_backward(letter, rotor_1, rotor_1_pos)
    
    letter = plugboard(letter)
    
    return letter


message = "HELLO"
output = ""

for letter in message:
    encrypted = encrypt_letter(letter)
    output = output + encrypted

print("Input: " + message)
print("Output: " + output)

rotor_1_pos = 0
rotor_2_pos = 0
rotor_3_pos = 0

decrypted = ""
for letter in output:
    decrypted_letter = encrypt_letter(letter)
    decrypted = decrypted + decrypted_letter

print("Decrypted: " + decrypted)
