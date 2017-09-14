limit = gets.strip.to_i
array = gets.strip.split(' ').map{|x| x.to_i}
((limit-1).downto(0)).each do |x|
	e = array[x]
	((x-1).downto(0)).each do |y|
		if array[y] > e
			array[y+1] = array[y]
			array.map{|z| print "#{z} "}
		else
			array[y+1] = e
			break
		end
		array[y] = e if y == 0
		puts
	end
end
array.map{|z| print "#{z} "}