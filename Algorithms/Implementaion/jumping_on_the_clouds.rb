###########################

# Method to calculate the minimum number of jumps
# needed to win the game
#
# @param clouds [Array] array of cloud details
#
# @return [Number] Minimum number fo jumps needed to
#   win the game
def calc_minimum_jumps(
    clouds:
  )
  jumps = 0
  index = 0
  # Iterate the loop untill index reaches the end
  until index == clouds.length-1
  	# If there are 2 consucetive 0 increase index = 2
    if clouds[index+2] == 0
      jumps += 1
      index += 2
    elsif clouds[index+1] == 0
      jumps += 1
      index += 1
    end
  end
  jumps
end
###########################

jumps = gets.strip.to_i
clouds = gets.strip.split(' ').map(&:to_i)

puts calc_minimum_jumps(clouds: clouds)
