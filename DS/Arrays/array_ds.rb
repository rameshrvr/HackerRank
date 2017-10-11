# Store the input
limit = gets.strip.to_i
array = gets.strip.split(' ').map(&:to_i)

# Reverse the array
array.reverse!

# Print the result
print array.join(' ')
