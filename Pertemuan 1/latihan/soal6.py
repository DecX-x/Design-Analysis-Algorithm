def volume_kerucut(diameter, tinggi):
    radius = diameter / 2
    print(f"radius: {radius}")
    return 1/3 * 3.14 * radius ** 2 * tinggi
hasil = volume_kerucut(5,3)
print(hasil)