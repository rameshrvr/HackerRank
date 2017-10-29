################################

# Method to find the totl sweetness value that a
# student can get
#
# @param portion [Array] array of portion that the student consumes
#
# @return [Number] sweetness amount
def get_sweetness_amount(
    portion:
  )
  # Calculate sum of the portion
  result = @sweet_array[@sweet_array.find_index(portion[0])..@sweet_array.find_index(portion[1])].inject(0, &:+)
  temp_index = @sweet_array.find_index(portion[0])
  return 0 if @sweet_array.empty?
  # Now remove the portion from the array
  @sweet_array -= @sweet_array[@sweet_array.find_index(portion[0])..@sweet_array.find_index(portion[1])]
  2.times { result += @sweet_array.delete_at(temp_index-1) if @sweet_array[temp_index-1] }
  result
end

################################

sweet, students = gets.strip.split(' ').map(&:to_i)
portions = []
# Generate sweet array
@sweet_array = (0...sweet).to_a

(0...students).each { |index| portions[index] = gets.strip.split(' ').map(&:to_i) }

portions.each { |portion| puts get_sweetness_amount(portion: portion) }
