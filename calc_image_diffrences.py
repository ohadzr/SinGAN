
import argparse
import glob
from skimage import io as img
from skimage.measure import compare_psnr
import os
from SIFID.sifid_score import calculate_sifid_given_paths
from PIL import Image

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--image_dir', help='input image dir', default='Input/Images', required=True)
    parser.add_argument('--original_image', help='input image name', required=True)
    opt = parser.parse_args()

    # get all images for test
    all_images_path = glob.glob(opt.image_dir+'/*.png')
    # all_images_path = [all_images_path[0]]
    print("Found %d images" % len(all_images_path))
    # print(all_images_path)

    # load original image and test images
    original_image = img.imread(opt.original_image)
    test_images = [img.imread(image_path) for image_path in all_images_path]

    test_images = [test_image[:,:,:3] for test_image in test_images]

    # print(original_image.shape)
    # print(test_images[0].shape)
    test_images_psnr = [compare_psnr(original_image, test_image)
                        for test_image in test_images]

    # for i, image_path in enumerate(all_images_path):
    #     print("PSNR for {} is: {}".format(os.path.basename(image_path), test_images_psnr[i]))

    print("mean PSNR is: {}".format(sum(test_images_psnr)/len(test_images_psnr)))


    for image_path in all_images_path:
        im = Image.open(image_path)
        rgb_im = im.convert('RGB')
        rgb_im.save(image_path[:-4]+'.jpg')

    test_images_sifid = [calculate_sifid_given_paths(opt.original_image, test_image_path[:-4]+'.jpg', 1, False, 64, ".jpg")
                         for test_image_path in all_images_path]

    # for i, image_path in enumerate(all_images_path):
    #     print("SIFID for {} is: {}".format(os.path.basename(image_path), test_images_sifid[i]))

    print(test_images_sifid)
    print("mean SIFID is: {}".format(sum(test_images_sifid)/len(test_images_sifid)))




