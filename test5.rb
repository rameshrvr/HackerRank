height = gets.strip.to_i
number = height-1
(number.downto(1)).each do |x|
	(1..x).each do |y|
		print ' '
	end
	(height-x).times{print '#'}
	puts
end
height.times{print '#'}