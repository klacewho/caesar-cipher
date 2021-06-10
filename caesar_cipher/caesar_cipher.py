# print('ok im alive')

def encrypt(text, shift):
  # return 'epp gstw evi fewxevhw'
  
  decrypted = ""
  
  for char in text:
    # turns each char into unicode
    letter_unicode = ord(char)

    # adds the shift value to each
    encrypted = letter_unicode + shift

    # turns those new unicode values into new char adds chars to decrypted
    decrypted += chr(encrypted)

  #replaces the $ character with a plain ol space   
  decrypted = decrypted.replace("$"," ")
  return(decrypted)

# dude = (encrypt('all cops are bastards',4))
# print(dude)

# if (dude == 'epp gstw evi fewxevhw'):
#   print('oh yeah buddy')

if __name__ == '__main__':

  decrypted = encrypt('all cops are bastards', 4)
  assert decrypted == 'epp gstw evi fewxevhw'

  # decrypted = encrypt('klace')
  # assert decrypted == 'opegi'


  print('TEST PASSED ')