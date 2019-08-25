

def find_triangle_height(area, base):
    # Formula for finding area of triangle is (Base * height) / 2
    # In this problem we know base and area and we need to find height
    # so the formula is height = (2 * area) / base
    height = (2 * area) / base
    if height == int(height):
        return int(height)
    else:
        return int(height) + 1


###################
data = list(map(int, input().split()))
print(find_triangle_height(data[1], data[0]))
###################
