number = gets.strip.to_i
array = gets.strip.split(' ').map{|x| x.to_i}
max, min, max_count, min_count = array.first, array.first, 0, 0
array.each do |x|
	if x > max
		max = x
		max_count += 1
	end
	if x < min
		min = x
		min_count += 1
	end
end
print "#{max_count} #{min_count}"