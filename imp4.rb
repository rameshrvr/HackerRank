number = gets.strip.split(' ').map{|a| a.to_i}
set_a = gets.strip.split(' ').map{|b| b.to_i}.sort
set_b = gets.strip.split(' ').map{|c| c.to_i}.sort
# set_a = set_a.sort
# set_b = set_b.sort
count, try1, try2 = 0, 0, 0
(set_a.last..set_b.first).each do |x|
  set_a.each do |y|
    try1 += 1 if (x % y == 0)
  end
  set_b.each do |z|
  	try2 += 1 if (z % x == 0)
  end
  count += 1 if (try1 == set_a.length && try2 == set_b.length)
  try1, try2 = 0, 0
end
print count
