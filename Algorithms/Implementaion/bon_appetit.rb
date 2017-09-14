n,k = gets.strip.split(' ').map(&:to_i)
cost = gets.strip.split(' ').map(&:to_i)
charged_amount = gets.strip.to_i
total_cost = 0
# calculate total cost
cost.map { |x| total_cost += x }
expected_cost = total_cost - cost[k]
if expected_cost / 2 == charged_amount
  print 'Bon Appetit'
else
  print "#{charged_amount - (expected_cost / 2)}"
end
