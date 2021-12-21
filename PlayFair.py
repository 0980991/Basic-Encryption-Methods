import string as s

class PlayFair:
    def __init__(self):
        # 1st row missing chars [A, J, W, I]
        # 2nd row missing chars [E, F, J, T, V, Y]
        # 3rd row missing chars [P, T, X]
        # 4th row missing chars [D, J, M, N, T, W, Y, Z]
        # 5th row missing chars [O, R, S, W, X]
        # 5th row missing chars [C, F, J, T]
        self.text = ['VUDGHVBBONOVZRKHNIBDLNCVGRPDEXZEVMGKSVBTLIFGITQQO',
                     'BZBLARLZDLHBURHARLCPIBIZMKQBGXAIMRPNOLWHMCSQ',
                     'RLZMKUGADGHIQONJDHFMKERLWYDGWVGLBSKQBHCUNUQE',
                     'ICSOQRRSPBIKRSIEQOGHHAAPLBVGKXAFGFUSVIILKREG',
                     'TDHABADKVPUZNAGQHVCFHJHDBFYEULITMYHQEIMNGKGU',
                     'SQKBDYKLMKANURGKGNWYYOOENRIINVXUHPARKKZEHBAE'
                    ]

        self.grids = None

    def fillGrid(self, key, removed_letter='X'):
        grids = [[],[]]

        # Fills the list of values
        for i in range(25):
            grids[0].append(i+1)

        # Fills the first squares of the grid with the key
        for letter in key:
            if letter not in grids[1]:
                grids[1].append(letter)

        # Fills the rest of the grid with alphabetical characters that aren't in the key
        for i, letter in enumerate(s.ascii_uppercase):
            if len(grids[1]) > 24:
                self.grids.append(grids[1])
                break

            if letter not in grids[1] and letter != removed_letter:
                grids[1].append(s.ascii_uppercase[i])

    def encryptPlayfair(self):
        pass

    def letterToValue(self, encrypted_pair):
        index_X = self.grids[1].index(encrypted_pair[0])
        index_Y = self.grids[1].index(encrypted_pair[1])

        return [self.grids[index_X], self.grids[index_Y]]

    def decrypt(self, encrypted_values):
        X = encrypted_values[0]
        Y = encrypted_values[1]

        X_Y_swap = False

        if X > Y:
            temp = X
            X = Y
            Y = temp
            X_Y_swap = True

        left_edge = [1, 6, 11, 16, 21]
        top_edge  = [1, 2, 3,  4,  5]
        
        # Check if letters are in the same row
        if (X-1) // 5 == (Y-1) // 5:
            if X in left_edge:
                X = X + 4
            else:
                X = X - 1

            if Y in left_edge:
                Y = Y + 4
            else:
                Y = Y - 1

        # Check if letters are in the same column
        elif Y % 5 == X % 5:
            if X in top_edge:
                X = X + 20
            else:
                X = X - 5

            if Y in top_edge:
                Y = Y + 20
            else:
                Y = Y - 5

        # Check if letters are the opposite corners of a box
        else:
            for j in range(1, 5):
                for i in range(1, 5):
                    if (X % 5 == 0) or (X % 5 > Y % 5 and Y % 5 != 0):
                        if Y == (X - j) + (i * 5):
                            X -= j
                            Y += j
                    else:
                        if Y == (X + j) + i * 5:
                            X += j
                            Y -= j

        if X_Y_swap:
            print(f'{Y}, {X}')
            return [Y, X]

        print(f'{X}, {Y}')
        return [X, Y]

    #TODO COunt which Letter is missing to find how to fill the grid
    def decryptPlayfair(self):

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

        encrypted_text = self.text[0]


        grid = [{1  : 'P'}, {2.  : 'L'}, {3.  : 'A'}, {4.  : 'Y'}, {5.  : 'F'},
                {6  : 'I'}, {7.  : 'R'}, {8.  : 'B'}, {9.  : 'C'}, {10. : 'D'},
                {11 : 'E'}, {12. : 'G'}, {13. : 'H'}, {14. : 'J'}, {15. : 'K'},
                {16 : 'M'}, {17. : 'N'}, {18. : 'O'}, {19. : 'Q'}, {20. : 'S'},
                {21 : 'T'}, {22. : 'U'}, {23. : 'V'}, {24. : 'W'}, {25. : 'X'}]


        if len(encrypted_text) % 2 != 0:
            encrypted_text += f'{encrypted_text[len(encrypted_text)-1]}'

        decrypted_text = ''

        pair_index = 0
        while pair_index < range(len(encrypted_text)):
            encrypted_pair = '' + encrypted_text[pair_index] + encrypted_text[pair_index + 1]
            encrypted_values = self.letterToValue(encrypted_pair)
            decrypted_pair = self.decrypt(encrypted_values)
            decrypted_text.append(decrypted_pair)
            pair_index += 2

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