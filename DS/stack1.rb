class ModelStack
  SIZE = 10
  @top = -1
  @stack = Array.new

  # return weather the stack is full
  def isfull
    if @top == SIZE
      return true
    else
      return false
    end
  end

  # return weather the stack is empty
  def isempty
    if @top == -1
      return true
    else
      return false
    end
  end

  # push element into the stack
  def pushstack(element:)
    unless isfull
      @stack[@top+1] = element
      @top += 1
    else
      puts "stack if full!!!"
    end
  end

  # pop element into the stack
  def popstack
    unless isempty
      @top -= 1
      return @stack[@top+1] = nil
    else
      puts "stack is empty!!!"
    end
  end

  # Print the stack
  def printstack
    unless isempty
      @stack.map{ |x| print "#{x} "}
      puts
    else
      puts "stack is empty!!!"
    end
  end
end
obj1 = ModelStack.new
obj2 = ModelStack.new
obj1.pushstack(element: 3)
obj1.pushstack(element: 5)
obj1.pushstack(element: 7)
obj1.printstack
obj2.pushstack(element: 2)
obj2.pushstack(element: 4)
obj2.pushstack(element: 6)
obj2.printstack
temp = obj1.popstack()
obj1.printstack
obj1.pushstack(element: 8)
obj1.printstack
