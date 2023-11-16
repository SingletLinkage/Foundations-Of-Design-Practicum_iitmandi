import cv2
import shape_from_vertices

def detect_from_img(path='path_traced.png'):
    image = cv2.imread(path)
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresh_image = cv2.threshold(image_gray, 220, 255, cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(thresh_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for i, contour in enumerate(contours):
        if i == 0:            continue

        shape, approx = shape_from_vertices.detect(contour)
        cv2.drawContours(image, contour, 0, (0, 0, 0), 4)
        x, y, w, h= cv2.boundingRect(approx)

        text_size = cv2.getTextSize(shape, cv2.FONT_HERSHEY_PLAIN, 2, 1)[0]
        text_x = x + (w - text_size[0]) // 2
        text_y = y + (h + text_size[1]) // 2

        coords = (text_x, text_y)
        colour = (0, 0, 0)
        font = cv2.FONT_HERSHEY_PLAIN

        cv2.putText(image, shape, coords, font, 2, colour, 1)
        for i in approx:
            cv2.putText(image, str(i[0]), i[0], font, 1, colour, 1)
    cv2.imshow("shapes_detected", image)
    cv2.waitKey(0)

if __name__ == '__main__':
    detect_from_img('path_traced.png')
