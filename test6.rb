input = gets.split(' ').map{ |x| x.to_i}
sum, min_sum, max_sum = 0, 0, 0
(1..input.length-1).each do |x|
  min_sum += input[x]
  max_sum += input[x]
end
(0..input.length-1).each do |x|
  (0..input.length-1).each do |y|
    unless x == y
      sum += input[y]
    end
  end
  min_sum > sum ? min_sum = sum : min_sum = min_sum
  max_sum < sum ? max_sum = sum : max_sum = max_sum
  sum = 0
end
print "#{min_sum} #{max_sum}"
