#!/usr/bin/env python
# coding: utf-8

# In[86]:


def enc(k, m):
    a=list(m.encode("ascii"))
    for i in range(len(a)):
        if a[i]>96 and a[i]<123:
            a[i]=(a[i]+k-19)%26+3*26+19
    m=bytes(a).decode("ascii")
    return m

def dec(k, c):
    a=list(c.encode("ascii"))
    for i in range(len(a)):
        if a[i]>96 and a[i]<123:
            a[i]=(a[i]-k-19)%26+3*26+19
    c=bytes(a).decode("ascii")
    return c
def caesarCryptanalysis(ciphertext):
    print("Caesar Cipher Cryptanalysis")
    print("Write the ciphertext and I will try to decode it for you!")
    a=list(ciphertext.encode("ascii"))
    freq=[]
    for i in range(97,123):
        f=a.count(i)
        freq.append(f)
    k=freq.index(max(freq))-4
    return k
####################
### MAIN PROGRAM ###
####################
def caesarCipher():
    print("Caesar Cipher Application")
    print("What do you want to do?")
    cyphertext = input("Write the cyphertext: ")
    print("\n")
    #Cryptanalysis
    k=caesarCryptanalysis(cyphertext)
    print("Encryption key = ",k)
    print("\n")
    #Decryption
    plaintext = dec(k, cyphertext)
    print("The corresponding plaintext is:")
    print(plaintext)

# Execute the main program
caesarCipher()

