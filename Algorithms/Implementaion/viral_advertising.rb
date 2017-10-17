#################

# Method to get the number of people count who
# Liked the ad
#
# @param days [Number] Number of days that the video went viral
#
# @return [Number] people count who liked the video
def calc_liked_count(
    days:
)
  sum = 5
  liked_count = 0
  # Itreate the loop as many days
  days.times do
    liked_count += (sum / 2)
    sum = (sum / 2) * 3
  end
  liked_count
end

#################

puts calc_liked_count(days: gets.strip.to_i)
