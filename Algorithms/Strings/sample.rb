# Get the input
number = gets.strip.to_i
# we are not gonna use this variable
_length = gets
array = gets.strip.split(' ').map(&:to_i)

puts array.index(number)