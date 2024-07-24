import os
import shutil
import re

def create_folders_and_copy_file(base_path, x, source_file):
    # Format the number to 3 digits
    formatted_number = f"{x:03d}"

    # Define the main folder name
    main_folder = f"epnd_c{formatted_number}_lo"

    # Define subfolders
    subfolders = ["_bg", "_clip", "_conte", "_info", "_lo", "_pool", "_sheet"]

    # Create the main folder
    main_folder_path = os.path.join(base_path, main_folder)
    os.makedirs(main_folder_path, exist_ok=True)

    # Create the subfolders inside the main folder
    for subfolder in subfolders:
        subfolder_path = os.path.join(main_folder_path, subfolder)
        os.makedirs(subfolder_path, exist_ok=True)

    # Define the destination file name
    destination_file = f"epnd_c{formatted_number}_v01_1920816_hon.aep"
    destination_path = os.path.join(main_folder_path, destination_file)

    # Copy and rename the file
    shutil.copy2(source_file, destination_path)

    print(f"创建卡文件夹: {main_folder}")
    print(f"复制AEP到: {destination_path}")

def list_cards(base_path):
    try:
        folders = [f for f in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, f))]
        card_folders = [folder for folder in folders if re.match(r"epnd_c\d{3}(?:_\d{3})?_lo", folder)]
        if card_folders:
            print("当前卡有:")
            for folder in card_folders:
                print(folder.replace("_lo", "").replace("epnd_", ""))
        else:
            print("没有找到任何卡文件夹。")
    except Exception as e:
        print(f"读取卡文件夹时出错: {e}")

def delete_card(base_path, x):
    # Format the number to 3 digits
    formatted_number = f"{x:03d}"
    # Define the folder name to be deleted
    folder_to_delete = f"epnd_c{formatted_number}_lo"
    folder_path = os.path.join(base_path, folder_to_delete)
    try:
        if os.path.exists(folder_path) and os.path.isdir(folder_path):
            confirmation = input(f"确认删除卡文件夹 {folder_to_delete} 吗？(y/n): ").lower()
            if confirmation == 'y':
                shutil.rmtree(folder_path)
                print(f"已删除卡文件夹: {folder_to_delete}")
            else:
                print("取消删除。")
        else:
            print("没有找到该卡文件夹。")
    except Exception as e:
        print(f"删除卡文件夹时出错: {e}")

def create_multiple_folders(base_path, start, end, source_file):
    for i in range(start, end + 1):
        create_folders_and_copy_file(base_path, i, source_file)

# Define the base path where the folders should be created
base_path = r"/Users/chenxing/Documents/卒制/EPND_PRODUCTION/"

# Define the source file path
aep_file = r"/Users/chenxing/Documents/卒制/EPND_PRODUCTION/epnd_c000_v01_1920816_hon.aep"

print("创建卡文件夹系统")

if __name__ == "__main__":
    while True:
        try:
            cut_no = input("输入卡号: ")
            if cut_no == "ls":
                list_cards(base_path)
            elif cut_no == "rm":
                list_cards(base_path)
                try:
                    delete_no = int(input("输入要删除的卡号: "))
                    if delete_no == 0:
                        print("不能删除c000")
                    else:
                        delete_card(base_path, delete_no)
                except ValueError:
                    print("请输入有效的卡号数字")
            elif "-" in cut_no:
                try:
                    start, end = map(int, cut_no.split("-"))
                    create_multiple_folders(base_path, start, end, aep_file)
                except ValueError:
                    print("请输入有效的范围，例如 1-100")
            else:
                create_folders_and_copy_file(base_path, int(cut_no), aep_file)
        except ValueError:
            print("请输入数字")
            continue