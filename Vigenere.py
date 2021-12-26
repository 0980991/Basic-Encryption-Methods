import string as s

class Vigenere:
    def __init__(self, text):
        self.text = text

    def encryptVigenere(self, key):
        upper_case = s.ascii_uppercase
        text = self.text.split()
        decrypted_message = ''
        # 1. For each letter in text:
        i = 0
        for word in text:
            for text_letter in word:
                text_index = upper_case.index(text_letter)
                key_index = upper_case.index(key[i % len(key)])
                decrypted_message += upper_case[(text_index + key_index) % 26]
                i += 1

            decrypted_message += ' '

        return decrypted_message

    def decryptVigenere(self, key):
        upper_case = s.ascii_uppercase
        text = self.text.split()
        decrypted_message = ''
        # 1. For each letter in text:
        i = 0
        for word in text:
            for text_letter in word:
                text_index = upper_case.index(text_letter)
                key_index = upper_case.index(key[i % len(key)])
                decrypted_message += upper_case[(text_index - key_index) % 26]
                i += 1

            decrypted_message += ' '

        return decrypted_message


