def encrypt():
    plain = input('Enter your Secret Message: ')
    string1 = ''
    string2 =  '' 
    for i in range(len(plain)):
        if i % 2 == 0:
            string1 += plain[i]
        else:
            string2 += plain[i]
    cipher = (string1 + string2)
    cipher = ''.join(cipher) 
    with open ('encrypted_file.txt' , 'w') as file:
        file.write(cipher)
    print('\nYour Encrypted Message is: {}'.format(cipher))
    print('\nYour Encrypted Message is Stored in "encrypted_file.txt"')

    
def decrypt():
    cipher = (input('Enter Cipher message: '))
    from math import ceil
    a = ceil(len(cipher)/2)
    cipher1 = cipher[:a] 
    cipher2 = cipher[a:] 
    x = len(cipher1)
    y = len(cipher2) 
    if y < x: 
        cipher2 = cipher2.ljust(y+1) 
    plain = ''.join([(i+p) for i,p in zip(cipher1,cipher2)])
    with open ('decrypted_file.txt', 'w') as file:
        file.write(plain)
    print('\nYour Decrypted Message is: {}'.format(plain))
    print('\nYour Decrypted Message is Stored in "decrypted_file.txt"')   
 
while True:
        user = input('(E)ncryption / (D)ecryption / (Q)uit: ').lower()
        if user == 'e':
            encrypt()
        elif user == 'd':
            decrypt()
        elif user == 'q':
            print('Exiting...\nDone')
            break
        else:
            print('Sorry, I Don\'t Understand That...')