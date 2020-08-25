
import sys
from lib import util

util.createDatasetFolderStructure()

util.downloadImagesFromGoogle(
    "scary images -momo",
    "scary_images_",
    200,
    downloadpath="raw/scary",
)


util.downloadImagesFromGoogle(
    "meme template",
    "meme_tmpl_",
    200,
    downloadpath="raw/meme",
)

util.downloadImagesFromGoogle(
    "person photography",
    "person_pht_",
    200,
    downloadpath="raw/person",
)

util.downloadImagesFromGoogle(
    "sports",
    "sports_",
    200,
    downloadpath="raw/sports",
)

util.downloadImagesFromGoogle(
    "news",
    "news_",
    200,
    downloadpath="raw/news",
)

util.downloadImagesFromGoogle(
    "night andscapes",
    "night_landscapes_",
    200,
    downloadpath="raw/landscapes",
)

util.downloadImagesFromGoogle(
    "trees",
    "trees_",
    200,
    downloadpath="raw/trees",
)

util.downloadImagesFromGoogle(
    "montains",
    "montains_",
    200,
    downloadpath="raw/montains",
)

