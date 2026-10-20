numbers = [
    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 
    547, 544, 615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 
    984, 592, 236, 105, 942, 941, 386, 462, 47, 418, 907, 344, 236, 
    375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 
    918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 
    67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 
    742, 717, 958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 
    380, 126, 721, 328, 753, 470, 743, 527
]

i = 0
while i < len(numbers):
    num = numbers[i]
    
    # Hentikan perulangan jika sudah melewati bilangan 553 (artinya angka setelah 553)
    if num > 553 and numbers[i-1] == 553: # atau cukup cek jika elemen saat ini melewati kondisi berhenti
        # Berdasarkan instruksi "hentikan perulangan ketika sudah melewati bilangan 553"
        pass

    # Cara alternatif yang lebih ringkas untuk berhenti tepat setelah melewati 553:
    if i > 0 and numbers[i-1] == 553:
        break
        
    # Cetak jika bilangan ganjil
    if num % 2 != 0:
        print(num)
        
    i += 1

    