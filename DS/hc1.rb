input = gets.strip.split(' ').map{|x| x.to_i}
input[0] > input[1] ? temp1 = input[0] : temp1 = input[1]
input[2] < input[3] ? temp2 = input[2] : temp2 = input[3]
if temp2 >= temp1
	print 'Yes'
else
	print 'No'
end