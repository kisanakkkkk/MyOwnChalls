from Crypto.Cipher import AES
import random
from Crypto.Util.Padding import pad


# J: So for the key, I use 5 random digits and repeat it until i get 16 bytes
# M: What? Man, i was using the exact same formula!

first_key = b""
second_key = b""
FLAG = b"IFEST22{REDACTED}"

def generateKey():
	global first_key, second_key
	first_key = (str(random.randint(0, 99999)).zfill(5)*4)[:16].encode()
	second_key = (str(random.randint(0, 99999)).zfill(5)*4)[:16].encode()

def encrypt(plaintext, a, b):
	cipher = AES.new(a, mode=AES.MODE_ECB)
	ct = cipher.encrypt(pad(plaintext, 16))
	cipher = AES.new(b, mode=AES.MODE_ECB)
	ct = cipher.encrypt(ct)
	return ct.hex()

def main():
	generateKey()
	print("Here's your flag, but encrypted heheh:", encrypt(FLAG, first_key, second_key))
	while True:
		print("Text to encrypt:")
		plain = input(">> ")
		print("result:", encrypt(plain.encode(), first_key, second_key))

if __name__ == '__main__':
	main()