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

    def encryptOrDecryptROT13(self):
        for row in self.text:
            decrypted_message = ''
            for char in row:
                upper_case = s.ascii_uppercase
                index = upper_case.index(char) #- 1
                decrypted_message += upper_case[(index + 13) % 26]
            return decrypted_message
