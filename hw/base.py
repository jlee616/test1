while True:
    base = input("Input a base: ").upper()

    if base == 'A':
        print('Adenine')
        break
    elif base == 'C':
        print('Cytosine')
        break
    elif base == 'T':
        print('Thymine')
        break
    elif base == 'G':
        print('Guanine')
        break
    elif base == 'U':
        print('Uracil')
        break
    else:
        print('Not a proper input')
        continue
