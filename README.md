# Hackathon: Build with AI 24/25
This repository serves as the collaborative work platform for the 24/25 Hackathon sponsored by the Google Developer Team. The commit usable for submission is tagged under **submission v1.0**.

## How to run
Below are the recommended steps for running our code:

### Prerequisites
* Conda
* VSCode
* Git *(optional)*

### First step
Extract the `.zip` from the GitHub page and decompress the file.

*OR*

Open a terminal (`CMD`, `PowerShell`, `Anaconda Prompt`, or others that recognize the `conda` command), navigate to the folder where you want to install the repository, and enter the following code:
```
git clone https://github.com/miguel-c05/Google-Hackathon-24-25.git
```

### Second step
If you haven't done so already, open one of the terminals mentioned in the previous step

### Third step
Enter the following code:
```
cd <repository_directory>
conda create -n hackathon --file requirements.txt
```
And wait for the installation to complete

### Fourth step
Open VSCode and, in the search bar at the top of the screen, type:
```
>Python: Select Interpreter
```
Press `Enter`, and select the Python interpreter whose name ends with `('hackathon')`

### Fifth step
Simply run `runner.py` using
```
cd <repository_directory>
runner.py
```
