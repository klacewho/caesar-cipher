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
    
  print(decrypted)
  decrypted = decrypted.replace("$"," ")
  return('DECRYPTED OUTPUT: ' + decrypted)

print(encrypt('all cops are bastards',4))


# if __name__ == '__main__':

#   decrypted = encrypt('all cops are bastards', 4)
#   assert decrypted == 'epp gstw evi fewxevhw'

#   # decrypted = encrypt('klace')
#   # assert decrypted == 'opegi'


#   print('TEST PASSED ')