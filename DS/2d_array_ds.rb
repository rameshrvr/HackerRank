# Define an array
array = Array.new
# Get values from command line
(0..5).each do |x|
  array[x] = gets.strip.split(' ').map(&:to_i)
end
result, sum = [], 0
(0..(array.length-3)).each do |x|
  (0..(array.length-3)).each do |y|
    # calculate the sum of each hour glass
    sum = array[x][y]+array[x][y+1]+array[x][y+2]+array[x+1][y+1]+array[x+2][y]+array[x+2][y+1]+array[x+2][y+2]
    # push that into an array
    result << sum
  end
end
# Print the max value from the array which is the expected result
puts result.max
