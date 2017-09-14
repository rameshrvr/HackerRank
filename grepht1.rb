query = gets.strip.to_i
results, connect = [], []
(0..query-1).each do |x|
  details = gets.strip.split(' ').map{|a| a.to_i}
  lib_cost, road_cost = details[2], details[3]
  (0..details[1]-1).each do |z|
    connect[z] = gets.strip.split(' ').map{|a| a.to_i}
  end
  if lib_cost <= road_cost
    results << lib_cost*details.first
  else
    temp, count = 0, 0
    temp_arr = []
    (0..details[1]-2).each do |z|
      connect[z].each do |a|
        if z == (details[1]-2)
          connect[z+1].each do |m|
            count += 1 if connect[z+1].include?(m)
          end
          break if count != 0
        end
        (connect[z+1].include?(a)) ? temp += lib_cost+(2*road_cost) : temp_arr << a
      end
    end
    results << temp
  end
end
results.map{|x| puts x}
