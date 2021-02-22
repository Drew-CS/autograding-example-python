# NAME:         Tumelo Modise
# ASSIGNMENT:   Writing loops&sequences

# Example
def hello_world():
    return "Hello!"

# 1
def squared_sum(array):
    total = 0
    for x in array:
        total += (x * x)
return total
print(square_sum[])
print(square_sum[5,-3,2])
print(square_sum[-3,4])
print(square_sum[7, -1, 15, 0])

# 2
def mix(a, b):
    index = 0
    chain = ""
    if len(a) >= len(b):
      while index <len(a):
        chain = chain + a[index]
        if index < len(b):
            chain = chain + b[index]
        index += 1
    else:
      while index <len(a):
        chain = chain + a[index]
        if index < len(b):
            chain = chain + b[index]
        index += 1
    return chain

print(mix("hello", "there"))
print(mix("1234", "abcd"))
print(mix("12", "abcd"))
print(mix("1234", "ab"))

main()
