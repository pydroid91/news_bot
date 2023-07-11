from F1NEWS import parse_news
from panorama import parse_panorama
from tproger import parse_articles

LATEST_NEWS = {'F1NEWS': [None] * 5, 'panorama': [None] * 5, 'tproger': [None] * 5}

SEND_NEWS = {'F1NEWS': [None] * 5, 'panorama': [None] * 5, 'tproger': [None] * 5}
SEND_LINKS = {'F1NEWS': [None] * 5, 'panorama': [None] * 5, 'tproger': [None] * 5}


def update_news():
    f1titles, f1links = parse_news()
    pan_titles, pan_links = parse_panorama()
    prog_titles, prog_links = parse_articles()

    for i in range(5):
        if f1titles[i] != LATEST_NEWS['F1NEWS'][i]:
            LATEST_NEWS['F1NEWS'][i] = f1titles[i]
            SEND_NEWS['F1NEWS'][i] = f1titles[i]
            SEND_LINKS['F1NEWS'][i] = f1links[i]
        else:
            SEND_NEWS['F1NEWS'][i] = None
            SEND_LINKS['F1NEWS'][i] = None

        if pan_titles[i] != LATEST_NEWS['panorama'][i]:
            LATEST_NEWS['panorama'][i] = pan_titles[i]
            SEND_NEWS['panorama'][i] = pan_titles[i]
            SEND_LINKS['panorama'][i] = pan_links[i]
        else:
            SEND_NEWS['panorama'][i] = None
            SEND_LINKS['panorama'][i] = None

        if prog_titles[i] != LATEST_NEWS['tproger'][i]:
            LATEST_NEWS['tproger'][i] = prog_titles[i]
            SEND_NEWS['tproger'][i] = prog_titles[i]
            SEND_LINKS['tproger'][i] = prog_links[i]
        else:
            SEND_NEWS['tproger'][i] = None
            SEND_LINKS['tproger'][i] = None
