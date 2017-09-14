a = 'abc'
b = 'acf'

hs= Hash.new(0)

a.each_char do |ch|
    hs[ch] += 1
end
b.each_char do |ch|
    hs[ch] -= 1
end

p hs.values.map(&:abs).inject(:+)