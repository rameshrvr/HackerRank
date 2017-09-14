num = gets.strip.to_i
array = Array.new
(0..num-1).each do |x|
	array[x] = gets.strip
end
lim = gets.strip.to_i
query = Array.new
(0..lim-1).each do |y|
	query[y] = gets.strip
end
query.each do |a|
	count = 0
	array.each do |b|
		count += 1 if (a == b)
	end
	puts count
end