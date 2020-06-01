import os
import cv2


def create_dir(dir_name):
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)


def list_videos(path):
    files = os.listdir(path)
    return [file for file in files if os.path.isfile(os.path.join(path, file))
            and file.endswith(('.mp4', '.avi', '.mov', '.mkv', '.flv'))]


def extract_images(source, destination):
    # create dir if not exists
    create_dir(destination)

    # Opens the Video file
    cap = cv2.VideoCapture(source)
    start_frame_number = 180  # start from this frame
    cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame_number)
    i = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imwrite(destination + "/" + str(i) + ".jpg", frame)
        print('Frame {} writing in {} success..'.format(str(i), destination))
        i += 1

    print('''
    Finished extracting all frames,
    Total Frames extracted: {}
    '''.format(i))

    cap.release()
    cv2.destroyAllWindows()


def main():
    PATH = 'files'
    files = list_videos(path=PATH)
    for file in files:
        extract_images(source=os.path.join(PATH, file), destination='extracted/' + file)


if __name__ == '__main__':
    main()
