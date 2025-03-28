from beetsplug.bandcamp import metaguru, http_get_text
from beetsplug.bandcamp import search

from . import Source, SourceCandidate, _calc_similarities, _get_similarity

_config = {
    "comments_separator": "\n---\n",
    "include_digital_only_tracks": True,
    "genre": {
        "capitalize": False,
        "maximum": 0,
        "mode": "progressive",
        "always_include": [],
    },
    "truncate_comments": False,
}


class Bandcamp(Source):
    def __init__(self, tag):
        super().__init__(tag)
        for candidate in search.search_bandcamp(query=f"{self._artist} {self._title} {self._album}", search_type="t"):
            self._candidates.append(BandcampCandidate(candidate, tag))


class BandcampCandidate(SourceCandidate):
    def __init__(self, candidate, tag):
        super().__init__()
        self._source_type = 'Bandcamp'
        similarities = []
        self._info = {
            "artist": candidate['artist'],
            'track': candidate['name'],
            'url': candidate['url']
        }
        if candidate['type'] == 'track':
            self._info['album'] = candidate.get('album')
        else:
            self._info['album'] = candidate.get('title')
        if "album" in tag:
            similarities.append(_get_similarity(str(tag.get('album')), self._info['album']))
        if "artist" in tag:
            similarities.append(_get_similarity(str(tag.get('artist')), candidate['artist']))
        if "title" in tag:
            similarities.append(_get_similarity(str(tag.get('title')), candidate['name']))
        guru = metaguru.Metaguru.from_html(http_get_text(candidate["url"]), _config)
        if guru.image:
            self._artwork_url = guru.image
        self._confidence = _calc_similarities(similarities)
