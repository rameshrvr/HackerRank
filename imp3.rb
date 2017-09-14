def return_value(start1:, start2:, jump1:, jump2:)
	(0..10000).each do |x|
		return 'YES' if (start1 + x*jump1) == (start2 + x*jump2)
	end
	return 'NO'
end
int = gets.strip.split(' ').map{ |y| y.to_i}
puts "#{return_value(start1: int[0], start2: int[2], jump1: int[1], jump2: int[3])}"