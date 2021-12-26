import string as s

class ROT13:
    def __init__(self):
        self.text = ['VUDGHVBBONOVZRKHNIBDLNCVGRPDEXZEVMGKSVBTLIFGITQQO',
                     'BZBLARLZDLHBURHARLCPIBIZMKQBGXAIMRPNOLWHMCSQ',
                     'RLZMKUGADGHIQONJDHFMKERLWYDGWVGLBSKQBHCUNUQE',
                     'ICSOQRRSPBIKRSIEQOGHHAAPLBVGKXAFGFUSVIILKREG',
                     'TDHABADKVPUZNAGQHVCFHJHDBFYEULITMYHQEIMNGKGU',
                     'SQKBDYKLMKANURGKGNWYYOOENRIINVXUHPARKKZEHBAE'
                    ]
        #self.text = [s.ascii_uppercase]

    def encryptROT13(self, key=13):
        decrypted_list = []
        for row in self.text:
            decrypted_message = ''
            for char in row:
                upper_case = s.ascii_uppercase
                index = upper_case.index(char) #- 1
                decrypted_message += upper_case[(index + key) % 26]
            decrypted_list.append(decrypted_message)
        return decrypted_list

    def decryptROT13(self, key=13):
        decrypted_list = []
        for row in self.text:
            decrypted_message = ''
            for char in row:
                upper_case = s.ascii_uppercase
                index = upper_case.index(char) #- 1
                decrypted_message += upper_case[(index - key) % 26]
            decrypted_list.append(decrypted_message)
        return decrypted_list