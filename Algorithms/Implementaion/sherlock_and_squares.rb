##########################

# Method to find the no of square integers in the
# given range
#
# @param start_range [Number] starting range
# @param end_range [Number] ending range
#
# @return [Number] result (count)
def calc_count_of_square_int(
    start_range:,
    end_range:
)
  result = 0
  (start_range..end_range).each do |number|
    result += 1 if Math.sqrt(number).modulo(1).zero?
  end
  result
end

##########################

test_cases = gets.strip.to_i

range_array = []
(0...test_cases).each { |index| range_array[index] = gets.strip.split(' ').map(&:to_i) }

range_array.each do |range|
  puts calc_count_of_square_int(start_range: range[0], end_range: range[1])
end
