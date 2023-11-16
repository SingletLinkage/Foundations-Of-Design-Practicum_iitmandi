import shape_from_image
import drawfig

DELAY = 500 # in ms
SIZE = 1000 # size of canvas for real time path tracing
POS_CSV = 'positions.csv'
OP_IMG = 'path_traced.png'

if __name__  == '__main__':
    drawfig.draw_path(SIZE, POS_CSV, OP_IMG)
    shape_from_image.detect_from_img(OP_IMG)
