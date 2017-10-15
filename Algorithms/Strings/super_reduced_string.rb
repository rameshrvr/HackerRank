#################

# Method to calculate super reduced string
#
# @param string [String] input string
#
# @return processed string or 'Empty String'
def get_super_reduced_string(
    string:
  )
  string_array = string.split('')
  # Set index to zero
  index = 0

  until (index == string_array.length) do
    # If a pair found delete them and start the search from begining
    if string_array[index].eql? string_array[index+1]
      2.times { string_array.delete_at(index) }
      index = 0
      next
    end
    index += 1
  end
  index.zero? ? 'Empty String' : string_array.join('')
end
##################

# Get the input
string_array = gets.strip

# Print the output
puts get_super_reduced_string(string: string_array)
