from subprocess import call
import os.path

# Downloads and unzips wikipedia dump TODO: Change this to a torrent, for the sake of wikiservers
if not os.path.isfile("wikipedia.xml"):
    if not os.path.isfile("wikipedia.xml.bz2"):
        call(["curl", "--verbose", "-o", "wikipedia.xml.bz2", "http://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles.xml.bz2"])
    call(["bunzip2", "-v", "wikipedia.xml.bz2"])

