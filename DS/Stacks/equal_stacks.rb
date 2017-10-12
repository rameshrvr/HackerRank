# Get the input
# Yeah we don't need this variable since we are using ruby
_var = gets
# Define cylinder
cylinder = []
(0..2).each { |index| cylinder[index] = gets.strip.split(' ').map(&:to_i) }
until [cylinder[0], cylinder[1]].all? { |x| x == cylinder[2] }
end
