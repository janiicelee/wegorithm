def birthdayCakeCandles(ar):
    tallest_candles = []
    tall = max(ar)
    for i in ar:
        if tall == i:
            tallest_candles.append(i)
    return len(tallest_candles)
    
