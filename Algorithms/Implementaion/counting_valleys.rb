#####################

# Method to calc count of valleys
#
# @param steps [String] string denotes the steps walked
#
# @return [Number] No of valleys he travelled
def calc_no_of_valleys(
    steps:
  )
  # Convert it to a char array
  char_array = steps.split('')
  result, temp, stack = 0, 0, [0]
  char_array.each do |step|
  	# If step is U increment temp else decrement
  	temp = step.eql?('U') ? temp+1 : temp-1
  	# Empty the stack
  	stack_var = stack.pop
  	# Increment result if we move from 0 to -ve
  	result += 1 if (stack_var == -1 && temp == 0)
  	# Push the last state into stack
  	stack.push(temp)
  end
  # Return result
  result
end

#####################

n = gets.strip.to_i
steps = gets.strip

# Print the result
puts calc_no_of_valleys(steps: steps)
