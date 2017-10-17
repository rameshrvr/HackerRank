################

# Method to find out number of beautiful days
# in a date range
#
# @param date_range: [Array] array[0] starting date,
#   array[1] ending date
# @param k [Number] K value
#
# @return [Number] Number of beautiful days
def calc_no_of_beautiful_days(
    date_range:,
    k:
)
  beautiful_days = 0
  (date_range[0]..date_range[1]).each do |date|
    reverse_date = date.to_s.split('').reverse.join('').to_i
    beautiful_days += 1 if (date - reverse_date).modulo(k).zero?
  end
  beautiful_days
end
################

input = gets.strip.split(' ').map(&:to_i)

puts calc_no_of_beautiful_days(date_range: [input[0], input[1]], k: input[2])
