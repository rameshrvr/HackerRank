################

# Method to predict weather the class will be conducted or not
#
# @param threshold [Number] cancelation threshold
# @param arrival_time [Array] arrival time of students
#
# @return [Boolean] YES or NO
def predict_class(
    threshold:,
    arrival_time:
)
  # Define counter = 0
  counter = 0
  arrival_time.each do |value|
    # increment counter if it is <= 0
    counter += 1 if value <= 0
    # return the value if we got the minimum value to conduct the class
    return 'NO' if threshold.eql? counter
  end
  'YES'
end

################

# Get test cases count
test_cases = gets.strip.to_i
# Define threshold_details and arrival_time
threshold_details = []
arrival_time = []
# get the input
(0...test_cases).each do |index|
  threshold_details[index] = gets.strip.split(' ').map(&:to_i)
  arrival_time[index] = gets.strip.split(' ').map(&:to_i)
end

(0...test_cases).each do |index|
  # For each test cases call the sub
  puts predict_class(
    threshold: threshold_details[index][1],
    arrival_time: arrival_time[index]
  )
end
