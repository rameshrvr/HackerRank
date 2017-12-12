###################

# Method to find the remaining energy after completing the game
#
# @param jump_distance [Number] distance covered by single jump
# @param clouds [Boolean Array] cloud details (Array of 0/1)
#
# @return [Number] remaining energy level
def calc_remaining_energy(
    jump_distance:,
    clouds:
)
  energy = 100
  counter = 0
  max_limit = clouds.length
  until counter >= max_limit
    energy -= jump_distance unless clouds[counter].zero?
    counter += jump_distance
    energy -= 1
  end
  energy
end
###################

jump_details = gets.strip.split(' ').map(&:to_i)
clouds = gets.strip.split(' ').map(&:to_i)

puts calc_remaining_energy(
  jump_distance: jump_details[1],
  clouds: clouds
)
