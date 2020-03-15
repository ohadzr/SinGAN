
import argparse
import glob
from skimage import io as img
from skimage.measure import compare_psnr
import cv2

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
    test_images = [img.imread(image_path) for image_path in all_images_path]

    test_images_psnr = [compare_psnr(cv2.resize(original_image, test_image.shape), test_image)
                        for test_image in test_images]

    for i, image_path in enumerate(all_images_path):
        print("PSNR for {} is: {}".format(image_path, test_images_psnr[i]))



