import math

class Point:
    def __init__(self,x,y,z,direction):
        self.x = x
        self.y = y
        self.z = z
        self.direction = direction


def cal_distance(p1,p2):
    return math.sqrt((p1.x - p2.x)**2 + (p1.y-p2.y)**2 + (p1.z-p2.z)**2)

def inside_cone(centre, target, cone_angle):
    angle = math.degrees(math.atan2(target.y-centre.y, target.x- centre.x))
    angle_diff = abs(angle- centre.direction)
    return angle_diff <= cone_angle /2

def VisiblePoints(centre,cone_angle, max_distance,pointslist):
    visible_points= []

    for point in pointslist:
        distance = cal_distance(centre, point)
        if distance <= max_distance and inside_cone(centre,point, cone_angle):
            visible_points.append((point.x,point.y, point.z, point.direction))

    return visible_points

centre_points = Point(27,46,2,90)
points_list = [Point(25,45,2,0), Point(30,48,2,135), Point(28,50,2,45)]
visible_points = VisiblePoints(centre_points, 45,20,points_list)
print(visible_points)
