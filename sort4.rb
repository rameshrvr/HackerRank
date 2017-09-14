limit = gets.strip.to_i
array = gets.strip.split(' ').map{|x| x.to_i}
count = 0
(0..limit-2).each do |x|
  if array[x] > array[x+1]
    ((x+1).downto(0)).each do |z|
      e = array[z]
      ((z-1).downto(0)).each do |y|
        if array[y] > e
          array[y+1] = array[y]
          count += 1
        else
          array[y+1] = e
          break
        end
        array[y] = e if y == 0
      end
    end
  end
end
print count