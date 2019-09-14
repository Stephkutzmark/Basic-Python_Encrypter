import random as r

def menu():
  option = input('Would you like to Encrypt or Decrypt? ')
  option = option.lower()
  while option:
    if option == 'encrypt':
      return 1
    elif option == 'decrypt':
      return 2
    else:
      print('Sorry, I didn\'t understand that')
      option = input('Would you like to Encrypt or Decrypt? ')

choice = menu()
while choice:
  if choice == 1:
    decryptkey = ''
    word = input('What would you like to encrypt? ')
    if word:
      dekey = {}
      used = []
      neword = ''
      i = 33
      while i < 126:
        y = r.randint(33, 126)
        if y not in used:
          dekey[chr(i)] = (chr(y))
          i += 1
          used.append(y)
      for letter in word:
        if letter == chr(32):
         neword += chr(32)
        else:
          neword += (dekey[letter])
      for piece in dekey:
        decryptkey += f'{dekey[piece]}'
    print(f'Here is your encrypted word(s): {neword}')
    print(f'Here is your decryption key: ({decryptkey}). Don\'t lose it!')
    choice = menu()
  elif choice == 2:
    decryptword = input('Please enter the string you want decrypted: ')
    decryptingkey = input('Please enter the decryption key:')
    let = 33
    decryptingkeylist = {}
    if decryptword and decryptingkey:
      newword = ''
      for char in decryptingkey:
        decryptingkeylist[char] = chr(let)
        let += 1
      for char in decryptword:
        if char == chr(32):
          newword += chr(32)
        else:
          newword += decryptingkeylist[char]
      print(f'Here is the decrypted string: {newword}')
    choice = menu()