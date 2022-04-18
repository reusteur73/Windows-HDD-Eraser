import os, sys, psutil
from tqdm import tqdm

red = '\033[31m'
green = '\033[32m'
white = '\033[37m'

def main():
# Warning message
    print('\n' * 100)
    print(red, '⚠ WARNING ⚠ : This program will fill up the hard drive to erase all files.')
    print("Please make sure that you have deleted all files from the hard drive before running this program. (except for the program itself)")
    print("For better results, it's recommended to run program multiple times. But make sure wait for the program to finish before running it again.")
    print('The drive that will be erased:', os.getcwd()[0:2], white)
    drive_size = psutil.disk_usage('/').total
    drive = os.getcwd()[0:2]
    # 2GB in bytes, you can change it.
    file_size = 2000000000
    num_files = int(drive_size / file_size)
    print(green,"You are about to create {} files of {} bytes each. ({}GB) in {} HDD".format(num_files, file_size, file_size/1000000000, drive), white)
    print(green,'Total size of the files:', num_files * file_size / 1000000000, 'GB')
    print(red,"Are you sure you want to continue? (y/n)", white)
    print('\n' * 3)
    answer = input("Answer: ")
    if answer == "y" or answer == "Y" or answer == "yes" or answer == "Yes" or answer == "YES":
        print(green,'Starting erase...', white)
        pass
    else:
        print(red,"Exiting...", white)
        sys.exit()
    # Create the files
    try :
        for i in tqdm(range(num_files), desc="Creating files", unit="files", unit_scale=True, colour="green", bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}]"):
            with open('file_{}'.format(i), 'wb') as f:
                f.write(os.urandom(file_size))
                f.close()
        # Delete the files
        print(green,'All files created. Now Deleting files...', white)
    except Exception as e:
        print(red,'Error:', e, white)
        pass
    try: 
        for i in tqdm(range(num_files), desc="Deleting files", unit="files", unit_scale=True, colour="red", bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}]"):
            os.remove('file_{}'.format(i))
    except Exception as e:
        print(red,'Error:', e, white)
        pass
    print(green,'Done, you can run the program again for better results. Thanks for using this script!', white)

if __name__ == "__main__":
    main()