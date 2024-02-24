from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import argparse


def create_argparse():
    parser = argparse.ArgumentParser(description="Cut video with start and end time")
    parser.add_argument("-t", "--target", type=str, help="video you want to change")
    parser.add_argument("-o", "--output", type=str, help="Name of output video")
    parser.add_argument("-s", "--start", type=int, help="Start time of cut in seconds")
    parser.add_argument("-e", "--end", type=int, help="End time of cut in seconds")
    return parser


def main():
    parser = create_argparse()
    args = parser.parse_args()
    target = args.target
    output = args.output
    start = args.start
    end = args.end
    try:
        print(f"Cutting {target} from {start} to {end} seconds")
        ffmpeg_extract_subclip(target, start, end, targetname=output)
    except ValueError:
        print("Error. Wrong time")
    except FileNotFoundError:
        print("Error. File not found")
    except Exception:
        print("Error. Unknown error. Check extension in your filename")


if __name__ == "__main__":
    main()
