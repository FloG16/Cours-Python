# loi d'ohm 'U = RI' 

print('Calcul de la loi d\'ohm. Entrez une valeur, si vous ne connaissez pas la valeur indiquez simplement 0')


U = float(input('Entrez une valeur de tension U : ') or 0)
I = float(input('Entrez une valeur d intensité I : ') or 0)
R = float(input('Entrez une valeur de résistance R : ') or 0)

if not U:
    U = R * I
elif not I:
    I = U / R
elif not R:
    R = U / I
else:
    print('Il manque ue valeur pour calculer la loi d\'ohm')

print('U =', U, '[V]')
print('I =', I, '[A]')
print('R =', R, '[Ω]')
