####################

# Method to find the matching no of pairs
#
# @param array [Array] array of numbers
#
# @retun [Number] Number of matching pairs
def calc_matching_pair(
    array:
  )
  # Sort the array
  array.sort!
  index, result = 0, 0
  (1..array.length).each do
    break if index == array.length
    if array[index] == array[index + 1]
      result += 1
      index += 2
    else
      index += 1
    end
  end
  # Return result
  result
end
###################

n = gets.strip.to_i
colors = gets.strip.split(' ').map(&:to_i)

print calc_matching_pair(array: colors)
