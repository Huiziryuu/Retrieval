__author__ = 'liuhui'

# Hashing a string using ordinal values
def hash(astring, tablesize):
    sum = 0
    for pos in rang(len(astring)):
        sum = sum + ord(astring(pos))

    return sum%tablesize

# Hashing a string using ordinal values with weighting
def hashWithWeight(astring, tablesize):
    sum = 0
    for pos in rang(len(astring)):
        sum = sum + ord(astring(pos)) * (pos + 1)

    return sum%tablesize