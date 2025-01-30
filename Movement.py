import math

# Movement may be a class but it is static and 
# follows a functional paradigm (no state, no side-effects, pure functions only)
#
# This allows for code re-use without falling into the OOP inheritance trap
class Movement():
    def calc_move_x(speed, angle, x):
        dx = speed * math.cos(math.radians(angle))
        return x + dx
    
    def calc_move_y(speed, angle, y):
        dy = speed * math.sin(math.radians(angle))
        return y - dy
    
    def calc_projectile_starting_point(centerx, centery, width, height, angle):
        projectile_x = centerx + (width / 2 + 20) * math.cos(math.radians(angle))
        projectile_y = centery - (height / 2 + 20) * math.sin(math.radians(angle))
        return (projectile_x, projectile_y)
