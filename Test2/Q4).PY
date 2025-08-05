height_of_wall = float(input("enter the height of wall in meters="))
width_of_wall = float(input("enter the width of wall in meters="))
cost_per_sq_meter = float(input("enter the painting cost per sq meter="))
area_of_one_wall = height_of_wall * width_of_wall
total_area = 4 * area_of_one_wall
total_cost = total_area * cost_per_sq_meter

print(f'{total_cost}rs is the total cost of painting')