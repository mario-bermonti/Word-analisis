#! "C:\Python33\python.exe"
# -*- coding: utf-8 -*-

import iofiles
import analysis

iodata = iofiles.IOData()
words = iodata.read_sequence("silabas2.txt", duplicates="n")

wordanalysis = analysis.WordAnalysis(words)
# wordanalysis.check_special_characters()

# wordanalysis.length()
# wordInfo = wordanalysis.get_word_info()

wordanalysis.check_mute_letters()
muteInfo = str(wordanalysis.get_mute_info())

end = input("press enter")
