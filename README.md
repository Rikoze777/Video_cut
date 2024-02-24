# Video_cut
This script will help you get the specified fragments from your video.

## Install

1. Install dependencies with the following command: 
```bash
pip install -r requirements.txt
```

## How to use

To begin, determine the beginning and end of the video segment in seconds.
Then use the following command:
```bash
python3 main.py -t <target> -o <output> -s <start> -e <end>
```

For example:
```bash
python3 main.py -t sample.mp4 -o sample_cut.mp4 -s 10 -e 200
```

For help with optins use the following command:
```bash
python3 main.py --help
```
