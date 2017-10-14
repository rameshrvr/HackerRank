# Get the input
string = gets.strip.split('')

result = (string[0].eql? string[0].downcase) ? 1 : 0
# scan all characters for upper case
string.each do |char|
  result += 1 if char.eql? char.upcase
end

puts result
