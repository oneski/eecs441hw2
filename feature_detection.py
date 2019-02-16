import os
import cv2


def read_img(path):
    return cv2.imread(path, 0)


def save_img(img, path):
    cv2.imwrite(path,img)
    print(path, "is saved!")


def harris_corner_detector(image, x_offset=5, y_offset=5, window_size=(5,5)):
    # Given an input image, x_offset, y_offset, and window_size,
    # return an heatmap image where every pixel is the harris
    # corner detector score for that pixel.
    # Input- image: H x W
    #        x_offset: a scalar
    #        y_offset: a scalar
    #        window_size: a scalar tuple M, N 
    # Output- results: a image of size H x W

    # TODO: Implement and run a harris corner detector on the image
    output = []

    return output


def main():
    # The main function
    ########################
    img = read_img('./grace_hopper.png')

    ##### Feature Detection #####  
    if not os.path.exists("./feature_detection"):
        os.makedirs("./feature_detection")

    harris_corner_image = harris_corner_detector(img)
    save_img(harris_corner_image, "./feature_detection/q1.png")


if __name__ == "__main__":
    main()
