length = gets.strip.to_i
matrix = []
last_elm = length-1
(0..length-1).each do |x|
  matrix[x] = gets.split(' ').map{|z| z.to_i}
end
primary_dia, secondary_dia = 0, 0
(0..length-1).each do |x|
	primary_dia += matrix[x][x]
	secondary_dia += matrix[x][last_elm]
	last_elm -= 1
end
result = primary_dia-secondary_dia
result < 0 ? result *= -1 : result *= 1
print "#{result}"

