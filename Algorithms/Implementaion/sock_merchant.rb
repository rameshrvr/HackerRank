n = gets.strip.to_i
colors = gets.strip.split(' ').map(&:to_i)
sorted_colors = colors.sort
index, result = 0, 0
(1..n).each do
  break if index == n
  if sorted_colors[index] == sorted_colors[index + 1]
    result += 1
    index += 2
  else
    index += 1
  end
end
print result
