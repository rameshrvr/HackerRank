time = gets.strip.split(':')
output = time
if time[2] =~ /PM/
	time[0].eql?('12') ? output[0] = 12 : output[0] = time[0].to_i + 12
	output[2].gsub!(/[^\d]/,'')
else
	time[0].eql?('12') ? output[0] = '00' : output[0] = time[0]
	output[2].gsub!(/[^\d]/,'')
end
print "#{output[0]}:#{output[1]}:#{output[2]}"

