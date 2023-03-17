def millify(num):
    '''
    Converting number to "prettified" string version as per requirement.
    '''
    num = float('{:.3g}'.format(num))
    magnitude = 0
    round_number = [1, 0.5, 0.1, 0.1, 0.1, 0.1]
    while abs(num) >= 1000:
        magnitude += 1
        num /= 1000.0
    if magnitude >=6:
        return 'Number above quadrillion'
    final = round_number[magnitude]*round((num)/round_number[magnitude])
    if final % 1==0:
        return '{}{}'.format(int(final), ['', 'K', 'M', 'B', 'T', 'Q'][magnitude])
    else:
        return '{}{}'.format(round(final, 1), ['', 'K', 'M', 'B', 'T', 'Q'][magnitude])