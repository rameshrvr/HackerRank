# Get the inputs
query = gets.to_i
# Define an empty array
array = Array.new
result = []

# Initialize a proc object
virtual_stack = proc do |*param|
  print param
  if param[1]
    array.push(param[1])
  elsif param[0] == 2
    array.pop unless array.empty?
  elsif param[0] == 3
    return array.max
  end
end

query.times do
  # run time input
  input = gets.strip.split(' ').map(&:to_i)
  temp = virtual_stack.call(input[0], input[1])
  result.push(temp) unless temp.nil?
end

# print the result
result.map{ |x| puts x }
