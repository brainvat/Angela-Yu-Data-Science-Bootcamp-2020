def sing(num_bottles):
    #TODO: Add your code to achieve the desired output and pass the challenge.
    #NOTE: The f String method of String Interpolation does not work.

    song = []
    n = num_bottles

    for n in range(num_bottles):
        song.append(str(99-n) + ' bottles of beer on the wall, ' + str(99-n) + ' bottles of beer.')
        song.append('Take one down and pass it around, ' + str(99-n-1) + ' bottles of beer on the wall.')
        song.append('')
        if (99 - n - 1) == 0:
            break

    return song
    
