################

# Method to calculate who wins
#
# @param locations [Array] Array of numbers describing the positions
#   of cat and mouse
#
# @return [String] return who wins cat or mouse
def calc_who_wins(
    locations:
  )
  if (locations[2]-locations[0]).abs == (locations[2]-locations[1]).abs
    return 'Mouse C'
  else
  	return ((locations[2]-locations[0]).abs > (locations[2]-locations[1]).abs) ? 'Cat B' : 'Cat A'
  end
end
################

query = gets.strip.to_i

array = []
(0...query).each { |index| array[index] = gets.strip.split(' ').map(&:to_i) }

# Print result
array.each { |location| puts calc_who_wins(locations: location) }
