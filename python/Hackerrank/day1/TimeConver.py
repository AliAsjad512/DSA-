def timeConversion(s):
    period = s[-2:]
    hh = int(s[:2])
    rest = s[2:-2]
    
    if period == "AM":
        if hh == 12:
            return "00" + rest
        return f"{hh:02}{rest}"
    else:  # PM
        if hh != 12:
            hh += 12
        return f"{hh:02}{rest}"

print(timeConversion("07:05:45PM"))
