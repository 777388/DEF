from PIL import ImageGrab
import time
import multiprocessing as mp

# define the size of the screen capture
left = 0
top = 0
width = 1920
height = 1080

# define a function to manipulate the pixels
def manipulate_pixels(im, start_y, end_y):
    for y in range(im.height-1):
        for x in range(im.width):
            # get the pixel value for the current pixel and the one below it
            curr_pixel = im.getpixel((x, y))
            next_pixel = im.getpixel((x, y+1))

            # compute the average of the RGB values for the two pixels
            new_r = int((curr_pixel[0] + next_pixel[0]) / 2)
            new_g = int((curr_pixel[1] + next_pixel[1]) / 2)
            new_b = int((curr_pixel[2] + next_pixel[2]) / 2)

            # set the new pixel value for the current and next pixels
            im.putpixel((x, y), (new_r, new_g, new_b))
            im.putpixel((x, y+1), (new_r, new_g, new_b))


# capture the screen
while True:
    im = ImageGrab.grab(bbox=(left, top, left+width, top+height))

    # create a pool of worker processes
    pool = mp.Pool(processes=4)

    # divide the rows of pixels evenly between the worker processes
    rows_per_process = int(im.height / 4)
    start_y = 0
    for i in range(4):
        end_y = start_y + rows_per_process
        if i == 3:
            end_y = im.height
        # apply the pixel manipulation function to each row in parallel
        pool.apply_async(manipulate_pixels, args=(im, start_y, end_y))
        start_y += rows_per_process

    # close the pool and wait for all processes to finish
    pool.close()
    pool.join()

    # show the modified image on the screen
    im.show()

    # wait for a short period of time before capturing the screen again
    time.sleep(0.1)
