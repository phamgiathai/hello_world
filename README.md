# hello_world
This is my hello world project. I want to push it on github.
```bash
# 1 Create a new repo on Github (remote)
# 2 Download remote repo from Github to my computer
cd <folder you want to store the repo>
git clone https://github.com/phamgiathai/hello_world.git 
# 3 Change working directory to repo folder
cd <your path contains hello_world repo> 
# 4 Open repo folder in VSC
code . #open hello_world with VSC
# 5 Check NEW changes, created files in your local repo (on your computer)
git status # Ex file README highlighted in red
# 6 Add new changes into an envelop
git add <file name> # 
# 7 Recheck everything is added in the envelop
git status # Ex file README highlighted in green
# 8 Write a comment / title on your envelop
git commit -m "add README"
# 9 Send the new changes from my local computer to remote repo
git push 
```
