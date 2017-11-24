###############

###############

limit = gets.to_i
str_array = Array.new
(0...limit).each { |index| str_array[index] = gets.split(' ').map(&:to_i) }
comparison = gets.split(' ')