import argparse
import os
import shutil

def handle_directory(source_path, destination_path):
    if not os.path.exists(source_path):
        return print(f'Such directory {source_path} doesn\'t exist')

    if not os.path.exists(destination_path):
        os.makedirs(destination_path, exist_ok=True)
    
    for entry in os.listdir(source_path):
        if entry.startswith('.') or entry.startswith('__'):
            continue

        process_entry(entry, source_path, destination_path)

def process_entry(entry, source_path, destination_path):
    entry_src_path = os.path.join(source_path, entry)
    print('Processing:', entry_src_path)
        
    if os.path.isdir(entry_src_path):
        new_destination_path = os.path.join(destination_path, entry)
        os.makedirs(new_destination_path, exist_ok=True)
        handle_directory(entry_src_path, new_destination_path)
    else:
        copy_file_to_extension_folder(entry_src_path, destination_path)

def copy_file_to_extension_folder(file_path, destination_path):
    filename = os.path.basename(file_path)
    extension = os.path.splitext(filename)[1].strip('.')
    directory_path = os.path.join(destination_path, extension) if extension else destination_path
    
    os.makedirs(directory_path, exist_ok=True)  # Ensure directory exists

    dst_file_path = os.path.join(directory_path, filename)
    try:
        shutil.copy(file_path, dst_file_path)
        print(f'Copied {file_path} to {dst_file_path}')
    except IOError as e:
        print(f"Error copying {file_path} to {dst_file_path}: {e}")



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--src', type=str, help='Source directory')
    parser.add_argument('-d', '--dst', type=str, help='Destination directory')

    args = parser.parse_args()

    source_directory = args.src if args.src else os.getcwd()
    current_directory = os.getcwd()
    parent_directory_name = os.path.dirname(current_directory)
    destination_directory = args.dst if args.dst else f'{parent_directory_name}/dist'

    handle_directory(source_directory, destination_directory)
        