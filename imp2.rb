house = gets.strip.split(' ').map{|x| x.to_i}
tree_loc = gets.strip.split(' ').map{|x| x.to_i}
fruit_count = gets.strip.split(' ').map{|x| x.to_i}
apple = gets.strip.split(' ').map{|x| x.to_i}
orange = gets.strip.split(' ').map{|x| x.to_i}
apple_count, orange_count = 0, 0
apple.each do |s|
	(s+tree_loc[0] >= house[0] && s+tree_loc[0] <= house[1]) ? apple_count += 1 : apple_count += 0
end
orange.each do |s|
	(s+tree_loc[1] <= house[1] && s+tree_loc[1] >= house[0]) ? orange_count += 1 : orange_count += 0
end
puts apple_count
puts orange_count