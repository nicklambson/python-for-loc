from pathlib import Path

TO_CHECK = Path("from translation")
PARENT = TO_CHECK.parent

# create a result folder in the parent folder
RESULT = PARENT / 'Result'
print(f"creating folder {RESULT.name}")
RESULT.mkdir(exist_ok=True)

# iterate through subfolders, creating them in the result folder
for language_folder in TO_CHECK.iterdir():
    language_folder_r = RESULT / language_folder.name
    print(f"creating folder: {language_folder}")
    language_folder_r.mkdir(exist_ok=True)

    
    # iterate through all folders and files
    # get the relative path and infer the result path
    for f in language_folder.rglob("*"):
        relative = f.relative_to(TO_CHECK)
        print(f"{relative}")
        result_path = RESULT / relative
        print(f"{result_path}")

        
        # if directory, make the directory in the result path
        if f.is_dir():
            print(f"creating folder: {result_path.name}")
            result_path.mkdir(exist_ok=True)
        
        # if file, read contents as text,
        # rename the file, and infer the result filepath
        # r.touch creates an empty file at location
        elif f.is_file():
            f_contents = f.read_text()
            f_contents = f_contents.replace("a", "888")
            # modify contents as necessary
            new_filename = f.stem + f.suffix
            r = result_path.with_name(new_filename)
            print(f"writing to file: {f.name}")
            r.touch(exist_ok=True)
            r.write_text(f_contents)


