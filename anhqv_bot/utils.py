from urllib.parse import urlparse, parse_qs


def get_youtube_video_id(url):
    """
    Taken from: https://stackoverflow.com/a/7936523
    """
    query = urlparse(url)
    if query.hostname == 'youtu.be':
        return query.path[1:]
    if query.hostname in ('www.youtube.com', 'youtube.com'):
        if query.path == '/watch':
            p = parse_qs(query.query)
            return p['v'][0]
        if query.path[:7] == '/embed/':
            return query.path.split('/')[2]
        if query.path[:3] == '/v/':
            return query.path.split('/')[2]

    return None


def get_youtube_video_thumbnail(url):
    video_id = get_youtube_video_id(url)
    return f'https://img.youtube.com/vi/{video_id}/sddefault.jpg'
