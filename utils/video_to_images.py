"""Convert a video to images."""

import argparse
from pathlib import Path
import cv2


def video_to_images(
    video_path: Path,
    images_path: Path,
    skip: int,
) -> None:
    assert skip > 0
    full_image_path = images_path / 'images' 
    if not full_image_path.exists():
        full_image_path.mkdir(parents=True)
    vidcap = cv2.VideoCapture(str(video_path))
    success, image = vidcap.read()
    count = 0
    image_index = 0

    while success:
        if count % skip == 0:
            cv2.imwrite(f"{full_image_path}/{image_index:04d}.jpg", image)  # Save frame as image
            image_index += 1
        success, image = vidcap.read()  # Read the next frame
        count += 1


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        "--video-path",
        type=Path,
        help="Full path to the video file.",
        required=True,
    )
    parser.add_argument(
        "--images-path",
        type=Path,
        help="Full path to the converted images.",
        required=True,
    )
    parser.add_argument(
        "--skip",
        type=int,
        help="Skipping image number to save.",
        default=5,
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    video_to_images(args.video_path, args.images_path, args.skip)
