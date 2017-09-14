limit = gets.strip.to_i
array = gets.strip.split(' ').map{|x| x.to_i}.sort
array.map{|y| print "#{y} "}