#deteksi nomor hp: 0818-0980-9636

def isphonenumber(text):
	if len(text)!=14:
		return False
	for i in range(0,3):
		if not text[i].isdigit():
			return False
	if text[4]!="-":
		return False
	for i in range(5,8):
		if not text[i].isdigit():
			return False
	if text[9]!="-":
		return False
	for i in range(10,13):
		if not text[i].isdigit():
			return False
	return True

print (isphonenumber("0818-0980-9636"))

message="telpon saya di nomor 0818-0980-9636. Atau telpon di nomor 1234-5678-9000"
for i in range (len(message)):
	hasil=message[i:i+14]
	if isphonenumber(hasil):
		print("nomor ditemukan adalah "+hasil)