def sort(length: float, width: float, height: float, mass: float):
    # edge case weight is non-existant
    if mass <= 0:
        return 'REJECTED'
    
    isBulky = False
    # single loop instead of multiple any()
    for num in (length, width, height):
        # edge case dimension is non-existant
        if num <= 0:
            return 'REJECTED'
        if num >= 150:
            isBulky = True

    # if not isBulky check volume
    isBulky = isBulky or length * width * height >= 1_000_000
    isHeavy = mass >= 20

    if isBulky and isHeavy:
        return 'REJECTED'
    
    elif isBulky or isHeavy:
        return 'SPECIAL'
    
    return 'STANDARD'

print(sort(50, 10, 10, 10))