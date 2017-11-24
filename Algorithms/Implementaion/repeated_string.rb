#########################

# Method to calculate the number of occurance
# of 'a' in the infinite string
#
# @param string [String] the input string
# @param integer [Number] interval
#
# @return [Number] Number of occurance of 'a'
def calc_num_of_occurance(
    string:,
    integer:
  )
  str_len = string.split('').length
  result = (integer / str_len) * string.split('').count('a')
  temp = integer.modulo(str_len)
  unless temp == 0
    string = string.split('')
    result += string[0..temp-1].count('a')
  end
  result
end

#########################

string = gets.strip
number = gets.strip.to_i

puts calc_num_of_occurance(string: string, integer: number)
