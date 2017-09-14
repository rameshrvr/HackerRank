number = gets.strip.to_i
candles = gets.split(' ').map{|x| x.to_i}
high, count = 0, 0
candles.each do |single|
	if single > high
		high = single
		count = 0 if count > 0
	end
	if single == high
		count += 1
	end
end
print count