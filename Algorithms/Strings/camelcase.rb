##################

# Method to calculate no of camelcase words
#
# @param [String] input string
#
# @return [Number] result
def calc_camel_case(
    string:
  )
  string_array = string.split('')
  result = (string_array[0].eql? string_array[0].downcase) ? 1 : 0
  # scan all characters for upper case
  string_array.each { |char| result += 1 if char.eql? char.upcase }
  # Return result
  result
end
###################

# Get the input
string = gets.strip

puts calc_camel_case(string: string)
