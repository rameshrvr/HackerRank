list = gets.strip.split(' ').map{|x| x.to_i}
inputs, array = [], Array.new(list[0]).map{|x| x = 0}
# (0..list[1]-1).each.map{|x| inputs[x] = gets.strip.split(' ').map{|y| y.to_i}}
# inputs.map{|y| ((y[0]-1)..(y[1]-1)).each.map{|x| array[x] += y[2]}}
(0..list[1]-1).each do
	inputs = gets.strip.split(' ').map{|y| y.to_i}
	((inputs[0]-1)..(inputs[1]-1)).each.map{|x| array[x] += inputs[2]}
end
puts array.max