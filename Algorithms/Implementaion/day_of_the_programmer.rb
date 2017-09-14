# Hash containing the details of month and its corresponding no.of days
@year_hash = {
  'jan' => 31,
  'feb' => 28,
  'mar' => 31,
  'apr' => 30,
  'may' => 31,
  'jun' => 30,
  'jul' => 31,
  'aug' => 31,
  'sep' => 30,
  'oct' => 31,
  'nov' => 30,
  'dec' => 31
}

# Method to check the leap year constrain
def _check_leap_year(
    year:
  )
  if year < 1918
    return (year % 4).zero?
  else
    return (year % 400).zero? || ((year % 4).zero? && !(year % 100).zero?)
  end
end

# Method to return remainig days in the month
def _ramining_day
  @year_hash.each do |_key, value|
    break if @day + value > 256
    @day += value
    @month += 1
  end
  (256 - @day)
end

# Get input
year = gets.strip.to_i
@day, @month = 0, 0
# Update 'feb' value if the input is leap year
@year_hash['feb'] = 29 if _check_leap_year(year: year)
remaining = _ramining_day
if year == 1918
  print '26.09.1918'
else
  print "#{remaining}.09.#{year}"
end
