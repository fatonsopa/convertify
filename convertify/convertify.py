# -*- coding: utf-8 -*-
import PIL
from PIL import Image
import glob
import os

class Convertify:

    @classmethod
    def get_images(self, path, from_type=None,recursive=True):
        files = []
        if from_type is not None:
            for ext in ('*.'+from_type):
                files.extend([f for f in glob.glob(path + "**/" + ext, recursive=recursive)])
        else:
            for ext in ('*.gif', '*.png', '*.jpg', '*.JPG', '*jpeg'):
                files.extend([f for f in glob.glob(path + "**/" + ext, recursive=recursive)])

        return files

    @classmethod
    def convert(self, source_path=None, destination_path=None, from_type=None, to_type="webp", recursive=True):
        if source_path is None:
            raise Exception("No source path provided")

        if not os.path.isdir(source_path):
            raise Exception("Source path not found!")

        print('Indexing images...')
        all_images = self.get_images(source_path, from_type, recursive)
        count_all_images = len(all_images)
        if count_all_images == 0:
            raise Exception("No images found in "+str(source_path))

        # create destination path if it doesn't exist
        if destination_path is None:
            destination_path = source_path + "/../converted-images/"
        os.makedirs(destination_path, exist_ok=True)

        print('Convertion started...')
        self.progress_bar(0, count_all_images, prefix='Progress:', suffix='Complete', length=50)

        i = 0
        for image_path in all_images:
            # set destination path
            destination_dir = image_path.replace(source_path, destination_path).replace('//', '/')
            destination_file = os.path.splitext(destination_dir)[0]+'.'+to_type

            # create destination dir
            os.makedirs(os.path.dirname(destination_file), exist_ok=True)

            # convert image
            image = Image.open(image_path).convert('RGB')
            image.save(os.path.splitext(destination_dir)[0]+'.'+to_type, to_type)

            i += 1
            self.progress_bar(i, count_all_images, prefix='Progress:', suffix='Complete', length=50)

        print('All images converted!')

    # Print iterations progress
    def progress_bar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='█', print_end="\r"):
        """
        Call in a loop to create terminal progress bar
        @params:
            iteration   - Required  : current iteration (Int)
            total       - Required  : total iterations (Int)
            prefix      - Optional  : prefix string (Str)
            suffix      - Optional  : suffix string (Str)
            decimals    - Optional  : positive number of decimals in percent complete (Int)
            length      - Optional  : character length of bar (Int)
            fill        - Optional  : bar fill character (Str)
            print_end    - Optional  : end character (e.g. "\r", "\r\n") (Str)
        """
        percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
        filledLength = int(length * iteration // total)
        bar = fill * filledLength + '-' * (length - filledLength)
        print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), print_end)
        # Print New Line on Complete
        if iteration == total:
            print()


