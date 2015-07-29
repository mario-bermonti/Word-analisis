#! "C:\Python33\Python.exe"
# -*- coding: utf-8 -*-

import libraryext.iofiles as iofiles
import analyzer


class WordAnalysis():
    def __init__(self):
        print("Bienvenido Análisis de Palabras\n")
        self.fileName = self.get_file_name()
        self.words = self.get_words(self.fileName)
        self.wordanalyzer = analyzer.WordAnalyzer(self.words)

        self.interface()

    def interface(self):
        while True:
            self.print_menu()
            desiredAnalysis = self.get_desired_analysis()
            if desiredAnalysis == "6":
                break
            elif desiredAnalysis in ("1", "2", "3", "4", "5"):
                self.run_analysis(desiredAnalysis)
            else:
                print("Opción inválida. Intente nuevamente.")
                print("\n" * 2)
                print("-" * 75)

        self.export_to_csv()

    def print_menu(self):
        """Print the anaylsis options to the user."""

        print("\n")
        print("-" * 75)
        print("Presione el número que identifica el análisis deseado")
        print("Las opciones de análisis son las siguientes:")
        print("1. Identificar palabras inválidas")
        print("2. Analizar la longitud de la palabra")
        print("3. Analizar letras silenciosas")
        # Find a better description
        print("4. Analizar letras con sonidos iguales")
        print("5. Analizar anagramas")
        print("6. Fin")

    def get_desired_analysis(self):
        """Gets the desired analysis from the user."""

        desiredAnalysis = input("Escriba la opción que desee: ")

        return desiredAnalysis

    def run_analysis(self, desiredAnalysis):
        """Runs the analysis desired by the user."""

        if desiredAnalysis == "1":
            self.wordanalyzer.check_special_characters()
        elif desiredAnalysis == "2":
            self.wordanalyzer.length()
            self.wordLengthInfo = self.wordanalyzer.get_length_info()
        elif desiredAnalysis == "3":
            self.wordanalyzer.check_silent_letters()
            self.silentInfo = self.wordanalyzer.get_silent_letter_info()
        elif desiredAnalysis == "4":
            self.wordanalyzer.check_same_sound_letter()
            self.sameSoundInfo = self.wordanalyzer.get_same_sound_letter_info()
        elif desiredAnalysis == "5":
            self.wordanalyzer.check_anagrams()
            self.anagramInfo = self.wordanalyzer.get_anagrams_info()

    def get_file_name(self):
        """Aks the user for the name of the file with the words to be
        analyzed.
        """

        fileName = input("Escribe el nombre del documento con las palabras: ")
        fileName = fileName.strip()
        fileName = "{}.txt".format(fileName)

        return fileName

    def get_words(self, fileName):
        """Get the words from the file specified by get_file_name."""

        self.iodata = iofiles.IOData()

        validFile = 0
        while not validFile:
            try:
                words = self.iodata.read_file_lines(fileName)
                validFile = 1

            except FileNotFoundError:
                print("No existe ningún file con ese nombre.")
                print("Intente nuevamente.")
                fileName = self.get_file_name()

        words = self.iodata.get_data()

        return self.clean_words(words)

    def clean_words(self, words):
        """Eliminates empty strings from the word list (sometimes happens)."""

        words = [word.lower() for word in words]
        for word in words[:]:
            if word == "":
                words.remove(word)

        return words

    def prepare_data(self, wordInfo):
        """Converts each key and value pair into tuple."""

        wordInfo = [(k, ) + v for k, v in wordInfo.items()]
        print(wordInfo)
        return wordInfo

    def get_data(self):
        """Gets the results of the analysis from the analyzer class."""

        self.wordanalyzer.integrate_word_information()
        wordInfo = self.wordanalyzer.get_word_info()

        return self.prepare_data(wordInfo)

    def prepare_header(self):
        """Prepares the header that will be used in the csv file."""

        header = self.wordanalyzer.get_analysis_dimensions()

        return (("words", ) + header + ("difficulty index", ))

    def export_to_csv(self):
        """Exports the information of the analyzed words into a csv file."""

        wordInfo = self.get_data()
        header = self.prepare_header()
        self.iodata.write_csv_row(file="results", data=header)
        self.iodata.write_csv_rows(file="results", data=wordInfo, mode="a")

wordanalysis = WordAnalysis()
end = input("press enter")
