first_string = 'abc'
second_string = 'acf'
@temp1_arr, @temp2_arr, @count = [], [], 0
def check_deletion(first_string:, second_string:)
  first_string.each_char do |ch|
    (second_string.include? ch) ? @temp1_arr << ch : @count += 1
  end
  second_string.each_char do |ch|
    (@temp1_arr.include? ch) ? @temp2_arr << ch : @count += 1
  end
  print @count
end
def check_anagram(string1:, string2:)
	string1.each_char do |ch|
		if string1 == string2
			return
		else
			
		end
end
check_deletion(first_string: first_string, second_string: second_string)
