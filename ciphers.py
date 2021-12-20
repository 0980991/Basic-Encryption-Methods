class Ciphers:

    def __init__(self):
        self.text = ['VUDGHVBBONOVZRKHNIBDLNCVGRPDEXZEVMGKSVBTLIFGITQQO',
                     'BZBLARLZDLHBURHARLCPIBIZMKQBGXAIMRPNOLWHMCSQ',
                     'RLZMKUGADGHIQONJDHFMKERLWYDGWVGLBSKQBHCUNUQE',
                     'ICSOQRRSPBIKRSIEQOGHHAAPLBVGKXAFGFUSVIILKREG',
                     'TDHABADKVPUZNAGQHVCFHJHDBFYEULITMYHQEIMNGKGU',
                     'SQKBDYKLMKANURGKGNWYYOOENRIINVXUHPARKKZEHBAE'
                    ]

    #TODO COunt which Letter is missing to find how to fill the grid

    def decryptSubstitution(text, key='SUBSTITUTIE'):
        pass

    def decryptROT13(text):
        pass

    def decryptPlayfair(self, encrypted_text=''):

        #----#----#----#----#----#
        # 1  # 2  # 3  # 4  # 5  #
        #----#----#----#----#----#
        # 6  # 7  # 8  # 9  # 10 #
        #----#----#----#----#----#
        # 11 # 12 # 13 # 14 # 15 #
        #----#----#----#----#----#
        # 16 # 17 # 18 # 19 # 20 #
        #----#----#----#----#----#
        # 21 # 22 # 23 # 24 # 25 #
        #----#----#----#----#----#

        encrypted_text = self.text
        grid = [{1  : 'P'}, {2.  : 'L'}, {3.  : 'A'}, {4.  : 'Y'}, {5.  : 'F'},
                {6  : 'I'}, {7.  : 'R'}, {8.  : 'B'}, {9.  : 'C'}, {10. : 'D'},
                {11 : 'E'}, {12. : 'G'}, {13. : 'H'}, {14. : 'J'}, {15. : 'K'},
                {16 : 'M'}, {17. : 'N'}, {18. : 'O'}, {19. : 'Q'}, {20. : 'S'},
                {21 : 'T'}, {22. : 'U'}, {23. : 'V'}, {24. : 'W'}, {25. : 'X'}]

        if len(encrypted_text) % 2 != 0:
            encrypted_text += f'{encrypted_text[len(encrypted_text)-1]}'

        decrypted_text = ''
        for row in encrypted_text:
            for char_pair in range(len(row)):
                encrypted_pair = '' + row[0] + row[1]
                row.pop
                encrypted_dic_items = []

                for character in encrypted_pair:
                    for i, letter in enumerate(grid):
                        if letter[i + 1] == character:
                            encrypted_dic_items.append(letter)

                print(encrypted_dic_items)

                for horizontal_step in range(1, 5):
                    x_and_y = []
                    for i, dict_key in enumerate(encrypted_dic_items):
                        p = int([key for key in dict_key][0])
                        x_and_y.append(p)
                
                    #if encrypted_dic_items[0][1] + horizontal_step * 5 == row[1]:
                        pass
        # 1. Divide alphabet letters into 5x5 grid
        # 2. Skip one letter that is not often used. The receiver MUST know which letter to skip

        # When picking any 2 letters in the grid they will either:
            # Be in the same row
                # Decode by finding the letter left to the encrypted letter (X - 1, Y - 1)
            # Be in the same column
                # Decode by finding the letter above the encrypted letter (X - 5, Y - 5)
            # Be the 2 opposite corners of a box
                # Decode by finding the letter of the other corner on the horizontal (X + (Y % 10 - X % 10), Y - a(Y % 10 - X % 10))

        # IF a msg is uneven fill the last place with an X or Q
        pass

    def decryptVigenere(text, key='VIGENERE'):
        decryption = ''
        for character in text:
            if character == ' ':
                decryption += character
