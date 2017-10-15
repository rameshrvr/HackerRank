###############

# method to calculate sum of an array
def array_sum(
    array:
  )
	sum = 0
	# Calculate sum
	array.collect { |single_num| sum += single_num }
	# Return sum
	sum
end

###############

limit = gets.strip.to_i
array_of_numbers = gets.split(' ').map(&:to_i)

puts array_sum(array: array_of_numbers)
