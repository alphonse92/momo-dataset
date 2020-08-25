
import sys
from lib import util

util.createDatasetFolderStructure()

util.downloadImagesFromGoogle(
    "meme template",
    "meme_tmpl",
    100,
    downloadpath="raw/meme",
)

util.downloadImagesFromGoogle(
    "person photography",
    "person_pht",
    150,
    downloadpath="raw/person",
)
