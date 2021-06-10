# print('ok im alive')

def encrypt(text, shift):
  # return 'epp gstw evi fewxevhw'
  
  decrypted = ""
  
  for char in text:
    # turns each char into unicode
    letter_unicode = ord(char)
    # print(letter_unicode)

    # adds the shift value to each
    encrypted = letter_unicode + shift
    # print(encrypted)
    # turns those new unicode values into new char adds chars to decrypted
    decrypted += chr(encrypted)

  #replaces the $ character with a plain ol space   
  decrypted = decrypted.replace("$"," ")

  return(decrypted)


# def decrypt(text):

# print(encrypt('all cops are bastards',4))
# print(encrypt('butt sniffer',4))
# print(encrypt('klace',9))


##############################################################################

if __name__ == '__main__':

  decrypted = encrypt('all cops are bastards', 4)
  assert decrypted == 'epp gstw evi fewxevhw'

  decrypted = encrypt('klace',9)
  assert decrypted == 'tujln'

  decrypted = encrypt('abc',25)
  assert (decrypted == 'zab')


print('TESTS PASSED ')