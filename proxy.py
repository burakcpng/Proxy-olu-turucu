import random

def get_randomSource():
	a = str(random.randint(1,254))
	b = str(random.randint(1,254))
	c = str(random.randint(1,254))
	d = str(random.randint(1,254))
	n ="."
	src = a+n+b+n+c+n+d
	return src
def dosyayaKaydet():
	dosya = open("dosya.txt","a",encoding="utf-8")
	dosya.write(get_randomSource())
	dosya.write("\n")
	dosya.close()
index = 0
while True:
	try:
		dosyayaKaydet()
		print(f"\rDosyaya Kaydoluyor: {get_randomSource()}",end=" ")
		index +=1
	except KeyboardInterrupt:
		print("\nProgram Sonlandırıldı..")
		print(f"toplam {index} proxy oluştu..")
		quit()

