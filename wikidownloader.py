from subprocess import call

call(["curl", "--verbose", "-o", "wikipedia.xml.bz2", "http://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles.xml.bz2"])
call(["bunzip2", "-v", "wikipedia.xml.bz2"])
# * Downloaded wikipedia zip file : screen -S wikipediaDownload -d -m curl --verbose -o wikipedia.xml.bz2 http://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles.xml.bz2
#        * Used GNU Screen because I am connect via ssh, cannot wait for it to finish
#        * WARNING: This command produces a ~10GB file
# * Unzipped wikipedia zip file: screen -S wikipediaUnzip -d -m bunzip2 -v wikipedia.xml.bz2
#        * Used screen again
#        * WARNING: This command produces a ~45GB file

