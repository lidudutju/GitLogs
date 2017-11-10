# GitLogs

A few lines of python code to checkout a git repository's history commit data in command line.

## Usage

This tool needs *gawk* dependency, so if you haven't installed *gawk*, open your terminal, and install it.  

```bash
brew install gawk
```

Then in terminal, *cd* to your git repository's directory. Make sure you have installed python in your mac, then run  

```bash
python ~/Desktop/GitLog.py
```

The result in terminal are: 

```bash
[~] cd ~/Desktop/c_wmapp_android                                                                           
[c_wmapp_android] python ~/Desktop/GitLog.py                                                       develop 
Author:  zhaonan_iwm  Commits: 794  Added Lines:  39923  Removed Lines: 17977
Author:  yupeng_iwm  Commits: 235  Added Lines:  54291  Removed Lines: 52645
Author:  lidu  Commits: 201  Added Lines:  16303  Removed Lines: 10141
Author:  zhangdongdong  Commits: 178  Added Lines:  30893  Removed Lines: 10479
```

