####################

# Method to calc minimun no of magic beverages
#
# @param array [Array] array of heights in the race
# @jump jump [Number] Maximum height he can jump
#
# @return [Number] Number of minimum magic beverages needed to finish the race
def calc_minimum_no_of_magic(
    array:,
    jump:
  )
	# Sort the array
	array.sort!
	max_height = array.pop
	max_height <= jump ? 0 : max_height-jump
end
####################

hurdle, jump = gets.strip.split(' ').map(&:to_i)
array = gets.strip.split(' ').map(&:to_i)

puts calc_minimum_no_of_magic(array: array, jump: jump)
