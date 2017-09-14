limit, count = gets.strip.to_i, 0
array = gets.strip.split(' ').map{|x| x.to_i}
i = array[0]
while i < limit
  count += 1
  break if array[i].nil?
  i += array[i]
end
puts count
