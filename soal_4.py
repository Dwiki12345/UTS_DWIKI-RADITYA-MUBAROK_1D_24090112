berat_badan = float(input("Masukkan berat badan Anda (kg): "))
tinggi_badan = float(input("Masukkan tinggi badan Anda (m): "))

bmi = berat_badan / (tinggi_badan ** 2)

if bmi < 18.5:
    kategori = "Berat badan kurang"
elif 18.5 <= bmi < 24.9:
    kategori = "Berat badan normal"
elif 25 <= bmi < 29.9:
    kategori = "Kelebihan berat badan"
else:
    kategori = "Obesitas"

print(f"\nHasil Perhitungan BMI Anda:")
print(f"BMI: {bmi:.2f}")
print(f"Kategori: {kategori}")