def count_bright_spots(pixels):
    bright_spots_count = 0
    for i in range(1,len(pixels)-1):
        if pixels[i] > pixels[i - 1]:
                if pixels[i] > pixels[i + 1]:
                    bright_spots_count += 1
    return bright_spots_count