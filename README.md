# SpliceSamplesSorter
Python app sorting Splice audio files in category.

## Goal
We all know the pain of dealing with the chaos of the Splice sample folder structure. Having to open 10 subfolders to access a sample...
Don't waste your time anymore, with SpliceSamplesSorter you will be able to rearrange your samples in a fast and efficient way.

## How to use
1. This app is coded in **Python 3.9**, therefore you first need to make sure that you have Python installed, at least Python 3.x, the closer to the version I used to code, the less chance the application will break.
You can download the latest version here : https://www.python.org/downloads/<br/>
BE SURE TO CHECK "Add path" WHEN YOU INSTALL PYTHON.

2. Then, open spliceSamplesSorter.py with any code editor (Notepad, Notepad++, SublimeText, VSCode, etc) and modify the path (at line 8) to fit yours, the text between the apostrophes must be the root path of Splice samples, it might depends on how you setup the installation of Splice, one way to check is to go in Splice settings and check Splice folder category. When done, save the modifications and close the editor.
```python
########## PATH ###############

src = 'D:\Splice'

###############################
```

3. Open your Terminal (Command Prompt on Windows (you can press the Windows key and type "cmd" to find it)). Now you need to set the running location of the terminal so it runs in the location where you put spliceSamplesSorter.py. You can easily find the path of the file: right click > properties > copy the location.

4. In the terminal, paste :
```bash
cd "{path}"
```
where {path} is the location you just copied. And press enter key.

5. Now type :
```bash
python spliceSamplesSorter.py
```
Press enter key.

6. Enjoy :)

## Info
* All files are NOT MOVED but copied over root directory, this allows to come back in case you decide you don't want the files to be sorted anymore. After the process is finished, you can find all the files sorted in different folders "sorted{category}" in the Splice folder.
* The algorithm sorts the files based on their name, the accuracy of the file name will highly influence the sorting accuracy.
