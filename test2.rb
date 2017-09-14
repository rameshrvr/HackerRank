number = gets.strip.to_i
array_of_int = gets.split(' ')
array, length= [], 0
(0..number-1).each do |x|
  array[x] = array_of_int[x].split('').map{|z| z.to_i}
  length = array[x].length if array[x].length > length
end
result = Array.new(length) {|z| z=0}
(0..length-1).each do |x|
  (0..number-1).each do |y|
    unless array[y][x].nil?
    	result[x] += array[y][x]
    end
  end
end
result.map{|x| print "#{x}"}