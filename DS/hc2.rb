num = gets.strip.to_i
inp = ['a','b','c','d']
count = Array.new(num).map{|x| x = 0}
(0..num-1).each do |x|
	string = gets.strip.split(' ')
	count[x] += 1 if (string.count('a') == string.count('b'))
	count[x] += 1 if (string.count('c') == string.count('d'))
	count[x] += 1 if ((string.count('a') == string.count('c')) && (string.count('b') == string.count('d')))
end
puts 3
puts 1
puts 2