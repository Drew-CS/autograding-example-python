# NAME: LIZ BAKER
# ASSIGNMENT: WRITING LOOPS AND SEQUENCES

# Example
def hello_world():
    return "Hello!"

# 1
def squared_sum(array):
    x = 0
    sumOfNumbers = 0
    
    while x < len(array)
        sumOfNumbers += (array[x] * array[x])
        x += 1
        
    return sumOfNumbers

# 2
def mix(a, b):
    x = 0
    mixedPhrase = []

    while x < len(a) or x < len(b):
        if x < len(a):
            mixedPhrase.append(a[x])
        if x < len(b):
            mixedPhrase.append(b[x])
        x += 1

    mixedPhrase = ''.join(mixedPhrase)
    return mixedPhrase

def main():
    print("squared sum: ", squared_sum([-3, 4]))
    print("mix:         ", mix("1234", "abcd") == "1a2b3c4d")

main()
