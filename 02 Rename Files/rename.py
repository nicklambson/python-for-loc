from pathlib import Path

locale_dict = {"Chinese (Simplified)": "zh_CN",
               "Chinese (Traditional)": "zh_TW",
               "English (United Kingdom)": "en_GB",
               "English (United States)": "en_US",
               "French (France)": "fr_FR",
               "German (Germany)": "de_DE",
               "Japanese (Japan)": "ja_JP",
               "Korean (Korea)": "ko_KR",
               "Russian (Russia)": "ru_RU",
               "Spanish (Latin America)": "es_419",
               "Spanish (Spain)": "es_ES",}

for language_folder in Path(r"sample").iterdir():
    language = language_folder.name
    print(f"{language=}")
    locale = locale_dict[language]
    for f in language_folder.rglob("*.*"):
        # print(f"{f}")
        new_f = f.with_name(f.stem + "_" + locale).with_suffix(f.suffix)
        # print(f"old filename: {f.name}")
        # print(f"new filename: {new_f.name}")
        f.rename(new_f)
