#######################

# Method to find the product of the remaining lego
# pieces
#
# @param lego_hash [Hash] hash containing details of lego pieces
#
# @result [Number] product of remaining lego pieces
def get_product_of_lego_pieces(
    lego_hash:
  )
  lego_hash[:gave_her_friend].each do |num|
    lego_hash[:count_of_lego].delete_at(lego_hash[:count_of_lego].find_index(num))
  end
  # return result
  lego_hash[:count_of_lego][0] * lego_hash[:count_of_lego][1]
end

#######################

test_cases = gets.strip.to_i
lego_array = []

(0...test_cases).each do
  temp_hash = {}
  temp_hash[:count_of_lego] = gets.strip.split(' ').map(&:to_i)
  temp_hash[:gave_her_friend] = gets.strip.split(' ').map(&:to_i)
  lego_array.push(temp_hash)
end

lego_array.each { |hash| puts get_product_of_lego_pieces(lego_hash: hash) }
