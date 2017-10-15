###############

# Method to calculate a veru big sum
#
# @param array [Array] array of numbers
#
# @return sum [Number] sum of the elements in that array
def calculate_very_big_sum(
    array:
  )
	sum = 0
	array.collect { |single_num| sum += single_num }
	sum
end

###############


number = gets.strip.to_i
array_of_int = gets.split(' ').map(&:to_i)

print calculate_very_big_sum(array: array_of_int)
