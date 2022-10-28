import os

import pytok

def main():
    this_dir_path = os.path.dirname(os.path.abspath(__file__))

    videos_dir_path = os.path.join(this_dir_path, 'data', 'videos')

    video_data_paths = []
    comment_data_paths = []
    for dir_name in os.listdir(videos_dir_path):
        video_data_path = os.path.join(videos_dir_path, dir_name, 'video_data.json')
        if os.path.exists(video_data_path):
            video_data_paths.append(video_data_path)

        comment_data_path = os.path.join(videos_dir_path, dir_name, 'video_comments.json')
        if os.path.exists(comment_data_path):
            comment_data_paths.append(comment_data_path)

    cache_dir_path = os.path.join(this_dir_path, 'data', 'cache')

    if not os.path.exists(cache_dir_path):
        os.mkdir(cache_dir_path)

    comment_cache_path = os.path.join(cache_dir_path, 'comments.csv')
    video_cache_path = os.path.join(cache_dir_path, 'videos.csv')

    comment_df = pytok.utils.get_comment_df(comment_data_paths, comment_cache_path)
    video_df = pytok.utils.get_video_df(video_data_paths, video_cache_path)

    # Do some analysis!

if __name__ == '__main__':
    main()