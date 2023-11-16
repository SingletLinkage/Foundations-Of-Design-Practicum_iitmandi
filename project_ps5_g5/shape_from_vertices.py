import cv2
import is_convex

def detect(contours):
    shape_dict = {
        3 : 'triangle',
        4 : 'quadrilateral',
        5 : 'pentagon',
        6 : 'hexagon',
        7 : 'heptagon',
        8 : 'octagon',
        9 : 'nonagon',
        10: 'decagon'
    }
    # The epsilon value will specify the precision in which we approximate our shape. 0.01 to 0.02 is good enough probably
    # both 'True' means figure is closed
    epsilon = 0.02*cv2.arcLength(contours, True)
    approx = cv2.approxPolyDP(contours, epsilon, True) # approx: array containing detected vertices
    
    polytype = 'convex' if is_convex.is_convex_polygon([i[0] for i in approx]) else 'concave'

    return polytype+' '+shape_dict.get(len(approx), 'Elliptical'), approx

