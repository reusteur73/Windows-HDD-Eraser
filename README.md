# Windows HDD eraser
<p style='font-size: 15px;'>The goal of this program is to overwrite HDD, In order to prevent your data from being found through forensic with tools such as Guymanager, TestDisk, PhotoRec and others.</p>

# How it works
<p style='font-size: 15px;'>The program detects the size of your hard drive, and calculates the number of files to create to fill it.
It creates the required number of files and then deletes them. The default file size is 2GB, but you can change it in line 18 source code.
</p>


# Before you start

<p style='font-size: 15px;'>Before you start, make sure you have deleted all the files from the hard drive, in order to leave only this python script.</p>

# How to use

-  1: Install requirements: python -m pip install -r requirements.txt
- 2: Run the program: python eraser.py
- 3: Once finished, you can run it again and again for better results.

