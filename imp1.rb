def solve(grades:)
  if grades%5 >= 3 && grades >= 38
    grades%5 == 3 ? (return grades+2) : (return grades+1)
  else
    return grades
  end
end

n = gets.strip.to_i
grades = []
for grades_i in (0..n-1)
  grades[grades_i] = gets.strip.to_i
end
grades.each do |x|
  result = solve(grades: x)
  puts result
end
