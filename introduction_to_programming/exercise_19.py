height_of_object_fall = float(input("Please enter the height at which the object is beieng throwed :"))
#initial speed of any object of a freely falling body is always zero
initial_velocity = 0
acceleration = 9.8
#acceleration due to gravity
final_velocity = (((initial_velocity**2)+(2*(acceleration)*height_of_object_fall)))**0.5
print("The final velocity is : ",final_velocity,"m/sec")
