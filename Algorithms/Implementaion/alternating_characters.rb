################

# Method to calculate no of deletions need to be performed
# to get the array having different consecutive characters
#
# @param string [string] input string
#
# @return [Number] Number of deletions need to be performed
def calc_no_of_deletions(
    string:
)
  # Convert the string into string array
  str_arr = string.split('')
  # set deletion is 0 initially
  no_of_deletion = 0
  # traverse through the array and increment the deletion if consecutive
  # characters are equal
  (0...(str_arr.length - 1)).each do |index|
    no_of_deletion += 1 if str_arr[index].eql? str_arr[index + 1]
  end
  no_of_deletion
end

################

test_cases = gets.strip.to_i
string_array = []

test_cases.times { string_array.push(gets.strip) }

(0...test_cases).each do |index|
  puts calc_no_of_deletions(string: string_array[index])
end
