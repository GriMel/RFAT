# !/usr/bin/env
# -*- coding: utf-8 -*-

import os
import logging
from taglib import File
AUDIO_TYPES = ['.mp3', '.ac3', '.wma', '.flac']


def setLogger():
    """
    Logger configuration
    """
    logger = logging.getLogger(__name__)
    logger.setlevel(logging.INFO)
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    formatter = logging.Formatter('%(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger


def transliterate(string):
    # improved version of https://gist.github.com/aruseni/1685068
    capital_letters = {
        'А': 'A',
        'Б': 'B',
        'В': 'V',
        'Г': 'G',
        'Д': 'D',
        'Е': 'E',
        'Ё': 'E',
        'З': 'Z',
        'И': 'I',
        'Й': 'Y',
        'К': 'K',
        'Л': 'L',
        'М': 'M',
        'Н': 'N',
        'О': 'O',
        'П': 'P',
        'Р': 'R',
        'С': 'S',
        'Т': 'T',
        'У': 'U',
        'Ф': 'F',
        'Х': 'H',
        'Ъ': '',
        'Ы': 'Y',
        'Ь': '',
        'Э': 'E',
        'І': 'I'
    }

    capital_letters_transliterated_to_multiple_letters = {
        'Ж': 'Zh',
        'Ц': 'Ts',
        'Ч': 'Ch',
        'Ш': 'Sh',
        'Щ': 'Sch',
        'Ю': 'Yu',
        'Я': 'Ya',
        'Є': 'Ye',
        'Ї': 'Yi'
    }

    lower_case_letters = {
        'а': 'a',
        'б': 'b',
        'в': 'v',
        'г': 'g',
        'д': 'd',
        'е': 'e',
        'ё': 'e',
        'ж': 'zh',
        'з': 'z',
        'и': 'i',
        'й': 'y',
        'к': 'k',
        'л': 'l',
        'м': 'm',
        'н': 'n',
        'о': 'o',
        'п': 'p',
        'р': 'r',
        'с': 's',
        'т': 't',
        'у': 'u',
        'ф': 'f',
        'х': 'h',
        'ц': 'ts',
        'ч': 'ch',
        'ш': 'sh',
        'щ': 'sch',
        'ъ': '',
        'ы': 'y',
        'ь': '\'',
        'э': 'e',
        'ю': 'yu',
        'я': 'ya',
        'є': 'ye',
        'і': 'i',
        'ї': 'yi'
    }

    capital_and_lower_case_letter_pairs = {}

    for capital_letter,\
        capital_letter_translit\
            in capital_letters_transliterated_to_multiple_letters.items():
        for lowercase_letter,\
            lowercase_letter_translit\
                in lower_case_letters.items():
            capital_and_lower_case_letter_pairs[
                "%s%s" % (capital_letter,
                          lowercase_letter)] =\
                "%s%s" % (capital_letter_translit,
                          lowercase_letter_translit)

    for dictionary\
        in (capital_and_lower_case_letter_pairs,
            capital_letters, lower_case_letters):

        for cyrillic_string, latin_string in dictionary.items():
            string = string.replace(cyrillic_string, latin_string)

    for cyrillic_string,\
        latin_string\
            in capital_letters_transliterated_to_multiple_letters.items():
        string = string.replace(cyrillic_string, latin_string.upper())

    return string


def rename_audio(filename):
    """
    Function to transliterate and rename given file
    """
    new_filename = transliterate(filename)
    os.rename(filename, new_filename)
    return new_filename


def fill_tags(filename, tracknumber):
    """
    Deletes all tags and sets only title and tracknumber
    """
    audio = File(filename)
    audio.tags.clear()
    audio.tags['TRACKNUMBER'] = [str(tracknumber)]
    audio.tags['TITLE'] = [os.path.splitext(filename)[-1]]
    audio.save()


def main():
    logger = setLogger()
    audio_files = []
    for file in os.listdir():
        if os.path.splitext(file)[-1] in AUDIO_TYPES:
            audio_files.append(file)
    for index, audio in enumerate(audio_files):
        new_name = rename_audio(audio)
        fill_tags(new_name, index + 1)
        logger.info("%s/%s %s -> %s proceeded" % (index + 1,
                                                  len(audio_files),
                                                  audio,
                                                  new_name))
    logger.info("Converting done.")

if __name__ == "__main__":
    main()
