alphabet_dictionary = {'A': 0, 'B': 1, 'C':2, 'D': 3, 'E':4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9,
                       'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18,
                       'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25}

reversed_alphabet_dictionary = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J',
                       10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S',
                       19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y', 25: 'Z'}


def encode_message(message, key):
    ciphertext = []

    for message_letter, key_letter in zip(message, key):
        ciphertext.append(reversed_alphabet_dictionary[(alphabet_dictionary[message_letter] + alphabet_dictionary[key_letter]) % 26])

    return ciphertext

def decode_ciphertext(ciphertext, key):
    decoded_message = []

    for ciphertext_letter, key_letter in zip(ciphertext, key):
        decoded_message.append(reversed_alphabet_dictionary[(alphabet_dictionary[ciphertext_letter] - alphabet_dictionary[key_letter]) % 26])

    return decoded_message

def main():
    message = 'HELLO'
    key = 'XMCKL'

    ciphertext = encode_message(message, key)
    print(f'ciphertext: {ciphertext}')

    decoded_message = decode_ciphertext(ciphertext, key)
    print(f'decoded_message: {decoded_message}')


if __name__ == "__main__":
    main()
