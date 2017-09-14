num = gets.strip.split(' ').map{ |x| x.to_i }
array = gets.strip.split(' ').map{ |x| x.to_i }
(1..num[1]).each do
	temp = array.shift
	array.push(temp)
end
array.map{ |y| print "#{y} "}