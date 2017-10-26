#####################

# Method to count the number of digits which will evenly
# devide the given number
#
# @param number [Number] Source number
#
# @return [Number] number of digits which will evenly devide
#   the given number
def count_evenly_devide_numbers(
    number:
)
  result = 0
  # Split the number into an array of its digits
  num_array = number.to_s.split('').map(&:to_i)
  # Iterate the array and inc the result if number modulo its digit in zero
  num_array.each { |num| result += 1 if !num.zero? && number.modulo(num).zero? }
  # Return the result
  result
end

#####################

test_cases = gets.strip.to_i
int_array = []
(0...test_cases).each { |index| int_array[index] = gets.strip.to_i }

int_array.each { |number| puts count_evenly_devide_numbers(number: number) }
