from seleniumbase import BaseCase


class Card(object):
    def __init__(self, tweet=''):
        card = f'{tweet}.card '
        self.link = f'{card}a'
        self.title = f'{card}.card-title'
        self.description = f'{card}.card-description'
        self.destination = f'{card}.card-destination'
        self.image = f'{card}.card-image'


class Quote(object):
    def __init__(self, tweet=''):
        quote = f'{tweet}.quote '
        namerow = f'{quote}.fullname-and-username '
        self.link = f'{quote}.quote-link'
        self.fullname = f'{namerow}.fullname'
        self.username = f'{namerow}.username'
        self.text = f'{quote}.quote-text'
        self.media = f'{quote}.quote-media-container'
        self.unavailable = f'{quote}.quote.unavailable'


class Tweet(object):
    def __init__(self, tweet=''):
        namerow = f'{tweet}.tweet-header '
        self.fullname = f'{namerow}.fullname'
        self.username = f'{namerow}.username'
        self.date = f'{namerow}.tweet-date'
        self.text = f'{tweet}.tweet-content.media-body'
        self.retweet = f'{tweet}.retweet-header'
        self.reply = f'{tweet}.replying-to'


class Profile(object):
    fullname = '.profile-card-fullname'
    username = '.profile-card-username'
    protected = '.icon-lock'
    verified = '.verified-icon'
    banner = '.profile-banner'
    bio = '.profile-bio'
    location = '.profile-location'
    website = '.profile-website'
    joinDate = '.profile-joindate'
    mediaCount = '.photo-rail-header'


class Timeline(object):
    newest = 'div[class="timeline-item show-more"]'
    older = 'div[class="show-more"]'
    end = '.timeline-end'
    none = '.timeline-none'
    protected = '.timeline-protected'
    photo_rail = '.photo-rail-grid'


class Conversation(object):
    main = '.main-tweet'
    before = '.before-tweet'
    after = '.after-tweet'
    replies = '.replies'
    thread = '.reply'
    tweet = '.timeline-item'
    tweet_text = '.tweet-content'


class Poll(object):
    votes = '.poll-info'
    choice = '.poll-meter'
    value = 'poll-choice-value'
    option = 'poll-choice-option'
    leader = 'leader'


class Media(object):
    container = '.attachments'
    row = '.gallery-row'
    image = '.still-image'
    video = '.gallery-video'
    gif = '.gallery-gif'


class BaseTestCase(BaseCase):
    def setUp(self):
        super(BaseTestCase, self).setUp()

    def tearDown(self):
        super(BaseTestCase, self).tearDown()

    def open_nitter(self, page=''):
        self.open(f'http://localhost:8080/{page}')

    def search_username(self, username):
        self.open_nitter()
        self.update_text('.search-bar input[type=text]', username)
        self.submit('.search-bar form')


def get_timeline_tweet(num=1):
    return Tweet(f'.timeline > div:nth-child({num}) ')
