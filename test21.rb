number = gets.strip.to_i
array_of_int = gets.split(' ').map{|x| x.to_i}
result = 0
(0..number-1).each do |x|
	result += array_of_int[x]
end
print result