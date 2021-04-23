from math import pi

class bangunRuang():

	def __init__(self):
		super(bangunRuang,self).__init__()
		self.nama = "Bangun Ruang"
		self.luasa = None
		self.tinggi = None

	def volume(self,luasa,tinggi):
		self.volume = self.luasa*self.tinggi
		return self.volume

class tabung(bangunRuang):
	def __init__(self,tinggi,jari):
		super().__init__()
		self.tinggi = float(input("Masukkan tinggi: "))
		self.jari = float(input("Masukkan jari: "))

	def volumeTabung(self):
		self.volumeTabung = pi*self.jari*self.jari*self.tinggi
		return self.volumeTabung

class balok(bangunRuang):
	def __init__(self,tinggi,panjang,lebar):
		super().__init__()
		self.panjang = float(input("Masukkan panjang: "))
		self.lebar = float(input("Masukkan lebar: "))
		self.tinggi = float(input("Masukkan tinggi: "))

	def volumeBalok(self):
		self.volumeBalok = self.panjang*self.lebar*self.tinggi
		return self.volumeBalok

class bola(bangunRuang):
	def __init__(self,nama,jarijari):
		super().__init__()
		self.jarijari = float(input("Masukkan jari-jari: "))

	def volumeBola(self):
		self.volumeBola = 4/3*pi*self.jarijari*self.jarijari*self.jarijari
		return self.volumeBola

print("TABUNG")
nilai = tabung("","")
print("Volume Tabung yaitu:",nilai.volumeTabung())


print()

print("BALOK")
hitung = balok("","","")
print("Volume balok yaitu:",hitung.volumeBalok())

print()

print("BOLA")
hasil = bola("","")
print("Volume bola yaitu:",hasil.volumeBola())
