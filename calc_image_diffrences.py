
import argparse
import glob
from skimage import io as img


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--image_dir', help='input image dir', default='Input/Images', required=True)
    parser.add_argument('--original_image', help='input image name', required=True)
    opt = parser.parse_args()

    # get all images for test
    all_images_path = glob.glob(opt.image_dir)
    print("Found %d images" % len(all_images_path))

    # load original image and test images
    original_image = img.imread('%s%s' % (opt.input_img, opt.ref_image))
    test_images = []


