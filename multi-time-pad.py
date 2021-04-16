import sys
import string
import collections
import sets

# XOR two strings of different lengths
def stringXOR(a, b):
    if len(a) > len(b):
       return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
    else:
       return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])

# All the given cipher texts
cipherTexts = [
    '965930e354f36fb45a60df9fdac1e4fbf4eafcdc14bf33602eeedd41bf88527cdd34599df5ddb6fbb6a4c64a09de3e3ef85865786487ffd0cac90830',
    '874330f445f36fb25a72c194d6db81f5e883f3d778b436642d87b84cbf8b497bc634499afea9d7fdbba3c9217dd84a2b995a001f6ae8f9b1d7d90134',
    '834330f65f9600a05a68df9fd4b5e9fefeeaf1d908a348052b93dd5cd78d5268c1344980e2c0d8e8deb9c7216bdb252e9339157a798be2d0ccd81951',
    '815a599a41ff08b15172df92b3d3f3f6ee9ee8c21db444763e81b149dc964e7bcc4731f2fac7d28faaa5cd216adb2b2393500b780b87fdd0d7c50851',
    '96313afc26e51bb95960b6ffb3bb81998de49fb07ab82b724d93dd5cd78b5410ab343f8bfec8de83deb9c0407db0394d9a5c116b6e9a9bdea3a36d5f',
    '955e3bfe43e40ab43f6ed986b3c5e4f8fd86f8b00fbf31692ee0af4dde81530fdd5b3d86f3ccb6fcaaa2da5807b72228f85e107a789bfeb4a3d90530',
    '8e4432fd47f10add5367d294ddb5e9f6ff98e4c378b625662f84dd40d68f290fab4055979bd9d7e6acbea85660db264d9a5c657e78e8fdbfcfc10226',
    'e25c3cf44fe51bb54d06d09ec1b5ecf6ea83feb019be20052281ab4dbf96506ac54258f2f8c1dfe3babfcd4f07b728388c3912776a9c9bbdc2c90851',
    '8b5f55ff50f31da93f72df9fcab5e5f2f98bf4dc78a72d712289b324bf845560c434499afea9deeea8a8da5268d4214d995e0476659befd0d7c50851',
    '874955fb54e40ea93f69d0f1d0daf4f9f98fefd30da2376039ecdd49d186276ea9475093f7c5b6fbbfbec3216fd8382e9d390a790b89eea2ccdf1e51',
    '973126f249e303b45172baf3b3c6e0fee9eaefdf16d025714a8fb34bdaec270dcb4149f2f3ccc58fbfaedc4867d04a219152001f6486fedea1ad6f30',
    '835f319a47e61fa25067d599d6d181e3e58f9dd41da32f0b4a99b85cbf83406ec05a31f2e8c6dbeabca2cc5809df2b29f84a007e798bf3b5c7ad0f34'
]

cipherToSolve = '835f319a47e61fa25067d599d6d181e3e58f9dd41da32f0b4a99b85cbf83406ec05a31f2e8c6dbeabca2cc5809df2b29f84a007e798bf3b5c7ad0f34'

for index1, cipher1 in enumerate(cipherTexts):
    counter = collections.Counter()
    # For each other cipher text
    for index2, cipher2 in enumerate(cipherTexts):
        # if both ciphers are not same
        if index1 != index2:
            for position, char in enumerate(stringXOR(cipher1.decode('hex'), cipher2.decode('hex'))):
                # If the char is between [a-z, A-Z]
                if char.isalpha() and char in string.printable:
                    # Update counter checking with all other ciper texts
                    counter[position] += 1 
 
    # Go through all counters
    for index, times in counter.items():
        # if number of spaces is >=7 save its index
        if times >= 7:
            spaces.append(index)

    # Get current cipher with spaces and at places we have spaces we get the key
    cipher1WithSpaces = stringXOR(cipher1.decode('hex'), ' '*150)
    for index in spaces:
        # Store key at a position
        key[index] = cipher1WithSpaces[index].encode('hex')
        # Save that we know key at this position
        knowKeyPositions.add(index)

# Get hex of the present key and adding 00 at unknown places
keyHex = ''.join([ val if val is not None else '00' for val in key ])
# XOR the cipher to solve with the key
result = stringXOR( cipherToSolve.decode('hex'), keyHex.decode('hex') )
# Print the result with * at unknown places
print(''.join([char if index in knowKeyPositions else '*' for index, char in enumerate(result)]))

#Put your cipher guess here. Below is example of cypher given.
cipherSolved= 'AND APPROACHED THE DESK. YET AGAIN, SOMEBODY HAD SEARCHED B'

print (cipherSolved)
# Getting the key 
finalKey = stringXOR(cipherToSolve.decode('hex'), cipherSolved)
print(finalKey.encode('hex'))
# Find out the orignal messages
for cipher in cipherTexts:
   print(stringXOR(cipher.decode('hex'), finalKey))
