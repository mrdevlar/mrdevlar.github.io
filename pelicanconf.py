from __future__ import unicode_literals

AUTHOR = 'Richard Podkolinski'
SITENAME = "Dev-Elements"
SITEURL = ""

PATH = "content"

TIMEZONE = 'Europe/Amsterdam'

DEFAULT_LANG = 'en'

THEME = 'theme/BT3-Adapted'


# Do not publish articles set in the future
WITH_FUTURE_DATES = False
# TEMPLATE_PAGES = {'blog.html': 'blog.html'}
TEMPLATE_PAGES = {
    'blog_base.html': 'blog_base.html',
    'blog-index.html': 'blog-index.html',
    'blog.html': 'blog.html',
}

STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}}


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (
#     # ("Reddit", "https://www.reddit.com/"),
#     # ("Youtube", "https://www.youtube.com"),
#     # ("CivitAI", "https://civitai.com/"),
# )

# Social widget
SOCIAL = (
    ("LinkedIn", " https://www.linkedin.com/in/richardpodkolinski/"),
    ("Instagram", " https://www.instagram.com/mr_devlar/"),
    ("Github", "https://github.com/mrdevlar"),
    ("envelope", "mailto:devlar@gmail.com")
)

DEFAULT_PAGINATION = 10
POST_LIMIT = 3

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
DEFAULT_DATE_FORMAT = ('%Y-%m-%d')


#===theme settings===========================

FAVICON = 'theme/img/favicon.png'
ICON = 'theme/img/favicon.png'
HEADER_IMAGE = 'theme/img/header.jpg'
COPYRIGHT = '2024 &copy; CC-BY'

# About ME
PERSONAL_PHOTO = "theme/img/about.jpg"
PERSONAL_INFO = """
I'm Richard Podkolinski. I've spent the last decade working as a professional Data Scientist. I'm some weird hybrid of Software Developer, Statistician and Show Magician.

Outside of working hours, I spend a lot of time playing with projects in Software, Artificial Intelligence, Electronics, Sewing and Art. 
"""