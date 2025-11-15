import os

source_folder = r'C:\Users\Vince Shu\OneDrive\Desktop\AppSheet'

for item in os.listdir(source_folder):
    # check if item is a file
    if os.path.isfile(os.path.join(source_folder, item)):
        # check if file ends with .jpg (no space before .jpg)
        if item.endswith('.png'):
            try:
                # renaming the file
                os.rename(
                    os.path.join(source_folder, item),
                    os.path.join(source_folder, 'Vince_' + item)
                )
                print(f"Renamed: {item} → Strong_{item}")
            except PermissionError:
                print(f"❌ Permission denied for: {item}")
