#################

# Method to calculate diagonal difference
#
# @param matrix [Array] Mostly a 2d array (array of array)
#
# @return diagonal_difference [Num] Absolute value of diagonal difference
def get_diagonal_difference(
    matrix:
  )
  primary_dia, secondary_dia = 0, 0
  array_length = matrix[0].length - 1
  # Calculate diagonal sum
  (0...matrix[0].length).each do |index|
  	primary_dia += matrix[index][index]
  	secondary_dia += matrix[index][array_length]
  	array_length -= 1
  end
  # Return absolute value of the difference between to diagonals
  (primary_dia - secondary_dia).abs
end

#################

length = gets.strip.to_i
matrix = []

(0...length).each { |index| matrix[index] = gets.strip.split(' ').map(&:to_i) }

print get_diagonal_difference(matrix: matrix)
