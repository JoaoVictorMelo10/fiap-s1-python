#checkpoints 1 bimestre
cp1 = float(input("nota do checkpoint1 do 1 bimestre: "))
cp2 = float(input("nota do checkpoint2 do 1 bimestre: "))
cp3 = float(input("nota do checkpoint3 do 1 bimestre: "))

# verifica se as notas estão no intervalo de 0 a 10
if cp1 < 0 or cp2 < 0 or cp3 < 0 or cp1 > 10 or cp2 > 10 or cp3 > 10:
    print("Apenas notas de 0 a 10!")
else:
    # se as notas forem validas, calcular a media
    menor_nota1 = min(cp1, cp2, cp3)
    media_checkpoints1= (cp1 + cp2 + cp3 - menor_nota1) / 2

    # Exibe o resultado com duas casas decimais

# nota do global solution do 1 bimestre
gs1 = float(input("nota do Global solution, 1 bimestre: "))
challenge1 = float (input("nota do challenge, 1 bimestre: "))

if gs1 < 0 or challenge1 < 0 or gs1 > 10 or challenge1 > 10:
    print ("Apenas notas de 0 a 10!")
else:
    media1bimestre = media_checkpoints1*0.2 + gs1*0.6 + challenge1*0.2
print (f"Sua média do 1 bimestre é: {media1bimestre}")

#checkpoints 1 bimestre
cp1 = float(input("nota do checkpoint1 do 1 bimestre: "))
cp2 = float(input("nota do checkpoint2 do 1 bimestre: "))
cp3 = float(input("nota do checkpoint3 do 1 bimestre: "))

# verifica se as notas estão no intervalo de 0 a 10
if cp1 < 0 or cp2 < 0 or cp3 < 0 or cp1 > 10 or cp2 > 10 or cp3 > 10:
    print("Apenas notas de 0 a 10!")
else:
    # se as notas forem validas, calcular a media
    menor_nota1 = min(cp1, cp2, cp3)
    media_checkpoints1= (cp1 + cp2 + cp3 - menor_nota1) / 2

    # Exibe o resultado com duas casas decimais

# nota do global solution do 2 bimestre
gs1 = float(input("nota do Global solution, 1 bimestre: "))
challenge1 = float (input("nota do challenge, 1 bimestre: "))

if gs1 < 0 or challenge1 < 0 or gs1 > 10 or challenge1 > 10:
    print ("Apenas notas de 0 a 10!")
else:
    media1bimestre = media_checkpoints1*0.2 + gs1*0.6 + challenge1*0.2
print (f"Sua média do 1 bimestre é: {media1bimestre}")










