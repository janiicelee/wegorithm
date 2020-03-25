def timeConversion(s):
    hh = s[:2]
    period = s[-2:]

    if (period == 'AM'):
        if (hh == '12'):
            output = '00' + s[2:-2]
        else:
            output = s[:-2]
    
    elif (period == 'PM'):
        if (hh == '12'):
            output = s[0:-2]
        else:
            output = str(int(hh) + 12) + s[2:-2]

    return output

