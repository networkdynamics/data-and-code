# Ukraine Discourse on TikTok Dataset

To build this dataset from the IDs here:

1) Go to github.com/networkdynamics/pytok and clone the repo locally
2) Run `pip install -e .` in the pytok directory
3) Run `pip install pandas tqdm` to install these libraries if not already installed
4) Run `get_videos.py` to get the video data
5) Run `video_comments.py` to get the comment data
6) Run `user_tiktoks.py` to get the video history of the users
7) Run `hashtag_tiktoks.py` or `search_tiktoks.py` to get more videos from other hashtags and search terms

If you get an error about the wrong chrome version, use the command line argument `get_videos.py --chrome-version YOUR_CHROME_VERSION`
Please note pulling data from TikTok takes a while! We recommend leaving the scripts running on a server for a while for them to finish downloading everything. Feel free to play around with the delay constants to either speed up the process or avoid TikTok getting mad at you.

Please do not hesitate to make an issue in this repo to get our help with this!