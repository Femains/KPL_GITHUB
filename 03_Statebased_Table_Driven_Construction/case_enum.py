from enum import Enum

class JenisKelamin(Enum):
    LAKI_LAKI = 1
    PEREMPUAN = 2

print(JenisKelamin.LAKI_LAKI) ## value of Enum => JenisKelamin.LAKI_LAKI
print(JenisKelamin.LAKI_LAKI.value) ## value dari LAKI_LAKI => 1
print(JenisKelamin.LAKI_LAKI.name) ## Nama Enum => LAKI_LAKI

