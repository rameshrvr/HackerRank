#################

# Method to calculate the minimum deletion needed
# to equalize the array
#
# @param array [Array] array of numbers
#
# @return [Number] Minimum deletion possible
def calc_minimum_deletion(
    array:
)
  count = 0
  return count if array.length == 1
  # Push the max appearence of the number in the array into count
  array.each { |num| count = array.count(num) if array.count(num) > count }
  # subtract array length from count to get the result
  array.length - count
end

#################
_limit = gets.strip.to_i
array = gets.strip.split(' ').map(&:to_i)

puts calc_minimum_deletion(array: array)
