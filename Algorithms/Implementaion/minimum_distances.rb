##################

# Method to find the minimum distance between two identical elements
#
# @param array [Array] array of numbers
# @param range [Number] length of the array
#
# @return [Number] Minimum distance if one else -1
def find_minimum_distance(
    array:,
    range:
)
  # Define minimum distance as the length of the array
  min_distance = range
  # Process the array until its empty
  until array.empty?
    # shift the first value
    var = array.shift
    # Find index if the same element found in that array
    index = array.index(var)
    # continue from top if we couldn't find the same element in the array
    next if index.nil?
    # minimum distance will be index difference + 1
    min_distance = index + 1 if min_distance > index + 1
  end
  # Return minimum distance else -1
  min_distance.eql?(range) ? -1 : min_distance
end

##################

# get range and array
range = gets.strip.to_i
array = gets.strip.split(' ').map(&:to_i)

puts find_minimum_distance(array: array, range: range)
