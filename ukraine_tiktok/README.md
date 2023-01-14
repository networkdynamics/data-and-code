# Invasion of Ukraine on TikTok Dataset

This is a dataset of videos and comments related to the invasion of Ukraine, published on TikTok by a number of users over the year of 2022. It was compiled by Benjamin Steel, Sara Parker and Derek Ruths at the Network Dynamics Lab, McGill University. We created this dataset to facilitate the study of TikTok, and the nature of social interaction on the platform relevant to a major political event.

To create the dataset, we identified hashtags and keywords explicitly related to the conflict to collect a core set of videos (or ”TikToks”). We then compiled comments associated with these videos. All of the data captured is publically available information, and contains personally identifiable information. In total we collected approximately 16 thousand videos and 12 million comments, from approximately 6 million users. There are approximately 1.9 comments on average per user captured, and 1.5 videos per user who posted a video. The author personally collected this data using the web scraping PyTok library, developed by the author: [https://github.com/networkdynamics/pytok](https://github.com/networkdynamics/pytok). 

Due to scraping duration, this is just a sample of the publically available discourse concerning the invasion of Ukraine on TikTok. Due to the fuzzy search functionality of the TikTok, the dataset contains videos with a range of relatedness to the invasion.

We release here the unique video IDs of the dataset in a CSV format. The data was collected without the specific consent of the content creators, so we have released only the data required to re-create it, to allow users to delete content from TikTok and be removed from the dataset if they wish. Contained in this repository are scripts that will automatically pull the full dataset, which will take the form of JSON files organised into a folder for each video. The JSON files are the entirety of the data returned by the TikTok API. We include a script to parse the JSON files into CSV files with the most commonly used data. We plan to further expand this dataset as collection processes progress and the war continues. We will version the dataset to ensure reproducibility.

To build this dataset from the IDs here:

1. Go to [https://github.com/networkdynamics/pytok](https://github.com/networkdynamics/pytok) and clone the repo locally
2. Run `pip install -e .` in the pytok directory
3. Run `pip install pandas tqdm` to install these libraries if not already installed
4. Run `get_videos.py` to get the video data
5. Run `video_comments.py` to get the comment data
6. Run `user_tiktoks.py` to get the video history of the users
7. Run `hashtag_tiktoks.py` or `search_tiktoks.py` to get more videos from other hashtags and search terms
8. Run `load_json_to_csv.py` to compile the JSON files into two CSV files, `comments.csv` and `videos.csv`

If you get an error about the wrong chrome version, use the command line argument `get_videos.py --chrome-version YOUR_CHROME_VERSION`
Please note pulling data from TikTok takes a while! We recommend leaving the scripts running on a server for a while for them to finish downloading everything. Feel free to play around with the delay constants to either speed up the process or avoid TikTok rate limiting.

Please do not hesitate to make an issue in this repo to get our help with this!

The `videos.csv` will contain the following columns:
`video_id`: Unique video ID
`createtime`: UTC datetime of video creation time in YYYY-MM-DD HH:MM:SS format
`author_name`: Unique author name
`author_id`: Unique author ID
`desc`: The full video description from the author
`hashtags`: A list of hashtags used in the video description
`share_video_id`: If the video is sharing another video, this is the video ID of that original video, else empty
`share_video_user_id`: If the video is sharing another video, this the user ID of the author of that video, else empty
`share_video_user_name`: If the video is sharing another video, this is the user name of the author of that video, else empty
`share_type`: If the video is sharing another video, this is the type of the share, stitch, duet etc.
`mentions`: A list of users mentioned in the video description, if any

The `comments.csv` will contain the following columns:
`comment_id`: Unique comment ID
`createtime`: UTC datetime of comment creation time in YYYY-MM-DD HH:MM:SS format
`author_name`: Unique author name
`author_id`: Unique author ID
`text`: Text of the comment
`mentions`: A list of users that are tagged in the comment
`video_id`: The ID of the video the comment is on
`comment_language`: The language of the comment, as predicted by the TikTok API
`reply_comment_id`: If the comment is replying to another comment, this is the ID of that comment

The date can be compiled into a user interaction network to facilitate study of interaction dynamics. There is code to help with that here: [https://github.com/networkdynamics/polar-seeds](https://github.com/networkdynamics/polar-seeds). Additional scripts for further preprocessing of this data can be found there too.

