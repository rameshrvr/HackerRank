first_line = gets.strip
number = first_line.split(' ').first.to_i
value = first_line.split(' ').last.to_i
second_line = gets.strip
array = second_line.split(' ')
(1..value).each do
	temp1 = array.shift
	array << temp1
end
array.each do |var|
    print "#{var} "
end