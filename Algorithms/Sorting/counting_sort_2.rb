_n = gets
# get the array of numbers
array = gets.strip.split(' ').map(&:to_i)
# sort the array
array.sort!

# print the result
print array.join(' ')
