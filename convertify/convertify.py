from PIL import Image
import glob
import os

class Convertify:
    def get_images(self, path, from_type = None):
        files = []
        if from_type is not None:
            for ext in ('*.'+from_type):
                files.extend([f for f in glob.glob(path + "**/" + ext, recursive=True)])
        else:
            for ext in ('*.gif', '*.png', '*.jpg', '*.JPG', '*jpeg'):
                files.extend([f for f in glob.glob(path + "**/" + ext, recursive=True)])

        return files

    def convert(self, path = None, from_type=None, to_type="webp"):
        destination_directory = path + '/../converted-images/'
        os.makedirs(destination_directory, exist_ok=True)

        print('Indexing images...')
        all_images = self.get_images(path, from_type)
        print('Images indexed!')

        print('Convertion started...')
        count_all_images = len(all_images)
        self.progress_bar(0, count_all_images, prefix='Progress:', suffix='Complete', length=50)

        i = 0
        for image_path in all_images:
            # set destination path
            destination_path = image_path.replace(path, destination_directory).replace('//', '/')
            destination_file = os.path.splitext(destination_path)[0]+'.'+to_type

            # create destination dir
            os.makedirs(os.path.dirname(destination_file), exist_ok=True)

            # convert image
            image = Image.open(image_path).convert('RGB')
            image.save(os.path.splitext(destination_path)[0]+'.'+to_type, to_type)

            i += 1
            self.progress_bar(i, count_all_images, prefix='Progress:', suffix='Complete', length=50)

        print('All images converted!')

    # Print iterations progress
    def progress_bar(self, iteration, total, prefix='', suffix='', decimals=1, length=100, fill='█', printEnd="\r"):
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
            printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
        """
        percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
        filledLength = int(length * iteration // total)
        bar = fill * filledLength + '-' * (length - filledLength)
        print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end=printEnd)
        # Print New Line on Complete
        if iteration == total:
            print()


