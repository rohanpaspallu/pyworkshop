# Get double in the range for even numbers only
doubles = ",".join([str(x * 2) for x in range(10) if x % 2 == 0])
print(doubles)

# secondary = [x*2 for x in range(0,10,2)]
# print(secondary)