##############

# Method to calculate the height of the utopian tree
# after the given growth cycle
#
# @param cycle [Number] Number of growth cycle
#
# @return [Number] Height of the tree
def calc_tree_height(
    cycle:
)
  height = 1
  return height if cycle.zero?
  (1..cycle).each do |num|
    height = num.odd? ? height * 2 : height + 1
  end
  height
end

##############

test_cases = gets.strip.to_i
season_array = []

test_cases.times { season_array.push(gets.strip.to_i) }

(0...test_cases).each do |index|
  puts calc_tree_height(cycle: season_array[index])
end
