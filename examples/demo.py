from pythonid.interpreter import PythonID

if __name__ == "__main__":
    kode = '''
cetak("Selamat datang di Python ID")

nama = lihat("Siapa nama kamu? ")

cetak("Halo", nama)
'''
    
    interp = PythonID(kode)
    
    print(interp)
