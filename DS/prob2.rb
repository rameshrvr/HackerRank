array = Array.new
(0..5).each do |x|
  array[x] = gets.strip.split(' ').map{ |y| y.to_i }
end
temp, sum = [], 0
(0..(array.length-3)).each do |x|
  (0..(array.length-3)).each do |y|
    sum = array[x][y]+array[x][y+1]+array[x][y+2]+array[x+1][y+1]+array[x+2][y]+array[x+2][y+1]+array[x+2][y+2]
    temp << sum
  end
end
puts temp.max
