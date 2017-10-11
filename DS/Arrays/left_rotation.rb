# Method to perform left rotation for a given
# array and rotation length
def rotate_array(
    array:,
    rotation:
  )
  rotation.times do
    temp = array.shift
    array.push(temp)
  end
  array
end

# Get the input
limit, num_of_rotations = gets.strip.split(' ').map(&:to_i)
array = gets.strip.split(' ').map(&:to_i)

# fetch the result
result = rotate_array(array: array, rotation: num_of_rotations)

# Print the result
print result.join(' ')
