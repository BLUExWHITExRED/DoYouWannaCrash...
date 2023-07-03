def create_large_file(file_name, size_in_mb):
    data = b'sKjNRWAk7)%HqaFNeg&feH(ByQ7Ny4Cf#8Zf5Z)3$FTk&!Os^VxPySXIwjm6zAwwZ!Ic9M^D@$afCPbP*ExL2N9I58iJy9xHuCI)!5E6F0%rEk7gNErajlg(L)!CEh%i@Ey&v(r%#eX)&vVJU3)i%02ssZeJ&0Hk7eM8Xs#@h76(A7Z%AhdORQDDNf(p3wE3i%IO74bN^m@59fxJ(*w&vjhuYnL&JUz5FS2fm)@A&D(x&MkhvGd$H6lGhGa*9A5kJGzAAJFJYQ**4mEkT&6*gksZlODNpWiLUbOCcO$FreURxfr^*jBdF1ea*rz)0*dYKa76pvb29bLL69#jGoX#Ru0mqsUNs^Od2G^nXL7hHwyQ)3ESQ3B66unwh$AeTXZ045pfft7aI3Yh35EK#6SN^nIiGJ(L785@5o&4jvSEx8$0ck8X4EWmeq*HEYU!@kY@AsDiUG6$LWDWs3yBLTC$UhsK0!S!Hr#EbKmXWeRrY5Wk&svL07lP3N1U!13Ve@AH5bXQ91PVlzeNo^Z!PA(e1t8%K2LabYniy78N4DOQqMgRre%)UnU*Kmo0YDKZrz%*0l)L1MN9RUe1fDk0m$fvn6uo)h(xlztZtsUScCiRvu%sA#CIYl$$35Q!DDxonJ@Y)^YuNcSplf4q6gYM2l3(00QtHgEjZSt4^wBK$0M&lM1XL$J@^1Mg*oTcM*n9KfRTHynkqanFmv%kuacGsVHd5f8M#hdGkjH$U$C^aot@&VVkXoZ(K1p$A1vDmzw81C^j2O60eUvqE*f@eWmS0eYq6V6(#c78eqD&1IoXrlJqM1ZVp1pgVHw&aGIg*$6AO#8X$2STNJtJ#ZMdrhyr3a01qhCD6w$zn%$UoguX9sY)q4lr0RJ17^iv&J1hfXctO1NAaYL!TXKaMHNhJUv7!)u1V*7Vso6G7i%SLK(CR*Ss@9x@x&Sb9OxaIn4WIn0RU&3OVxY(aDd5yWnBpbnKMz(w88I$N*4hW5BMegmsy5T'
  # Sample data to write to the file
    size_in_bytes = size_in_mb * 1024 * 1024  # Convert MB to bytes

    try:
        with open(file_name, 'wb') as file:
            bytes_written = 0

            while bytes_written < size_in_bytes:
                file.write(data)
                bytes_written += len(data)

        print(f'bye.')
    except IOError:
        print(f'Retry')

create_large_file('large_file.txt', 1048576000000000)
