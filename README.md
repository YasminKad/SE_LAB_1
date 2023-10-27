# SE_LAB_1
Working with Github: Simple to do list project

In this project we aimed to build a simple to do list. We have designed our project with an OO aproach and so defined the classes Task, Task_List, Category and Menu coupled with a main file to handle all the processes and functionalities of the project. 

To implement the mentioned to do list project, we have done the following tasks:

- Created this git repository to be able to develop the porject in our team

- Created a sample gitignore file for the unnecessary files

- Created separate branches per each class designed (feature/classname-class) to be able to develop each object and feature async and merge them to the main branch at the final stage.
  Our existing branches: feature/category-class, feature/task-class, feature/task_list-class, feature/menu-class, main 

- Developed and implemented each class separately through its unique branch over time. This implementation has been step by step. Each class function has been implemented in a separte commit to be able to follow the atomic commit practice with a proper commit message (writen due to the best practices of commit message submission).

- Through the development process, there where some conflicts in different development parts since classes where developed asynchronously and through different branches by different team members; We resolved the occurred conflicts when merging the branches in the files that had overlapped functionalities or conflicts. 

- At the final stage we merged the child branches with the main branch using pull requests (according to the estricted main branch merging access).

- You could use the built to do list by running the main.py file in the main branch :)

Questions:

1)The .git folder contains all the information needed to track the codebase changes. In other words, the project's
version control (commits, remote repo address etc.) is handled using this file.
For .git to be built, a new repo should be created and to the git "git init" command is the proper way to build a new repo.

2)When you have the approach of atomic committing in a project, the commits should be as small as possible and so, each
commit does one, and only one simple thing that can be summed up in a simple sentence.
The same work for pull-request. When you are working on a fork of somebody else's project, the requests made during this
process should be as same as the commits in atomic commit.

3)All following commands, manage and manipulate the commit history on a git repo.

Fetch:
Is the action of getting updates from a remote repo to your local, without immediately applying them. It kind of works
as a mailbox.

Pull:
Is the action of getting updates from a remote repo and immediately automatically applying them. It kind of works as a
mailbox being checked and its letters read right away.

Merge:
Is the action of combining two different recipes into one. It kind of combines both local and upcoming changes and mixes
these different changes together.

Rebase:
Is the action of moving or reorganizing the sequence of commits in a project which is useful for making the commit history
easier to follow. It kind of like the action of rewriting the history of a novel.

Cherry-pick:
Is the action of selecting specific commits from one branch and apply them to another branch without merging or 
reorganizing the entire tree. It kind of represents a unique fruit you select and add to a fruit basket.
