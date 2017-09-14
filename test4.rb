number = gets.strip.to_i
array = gets.split(' ').map{|x| x.to_i}
pos_num, neg_num, zero = 0, 0, 0
array.each do |single|
	if single >= 0
		single > 0 ? pos_num += 1 : zero += 1
	else
		neg_num += 1
	end
end
puts pos_num.to_f/number.to_f
puts neg_num.to_f/number.to_f
puts zero.to_f/number.to_f