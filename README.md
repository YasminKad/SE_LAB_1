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

4)The restore, reset, and revert commands in Git are all used to undo changes, but they do so in different ways.

Restore:
The restore command restores files in the working tree from either the index or another commit. The branch is not updated if  restore is used. Restore is useful for discarding changes that have not yet been staged or committed.
For example, if you want to undo some accidental changes that you made earlier, you can use the restore command to restore the file to its previous state.

Reset:
The most important thing about  reset is that it updates the branch, moving the tip to a previous commit. This effectively discards any commits that were made after the point of the reset command.
This is useful for undoing changes that have already been committed, but which you no longer want in the repository history.
For example, you can use the reset command to undo a commit which contains a bug and move the branch back to the previous commit.

Revert:
The revert command creates a new commit that undoes the changes made by another commit. This still allows you to undo the changes from the previous commit.
This is useful for undoing changes that have already been committed, but which you still want to be able to revert to later just in case.
For example, if you have made a commit that contains a new feature, but you decide that you don't want that feature after all, you can use the revert command to create a new commit that undoes the changes from the original commit  to get to it later .

5)The stage command in Git is used to add changes from the working tree to the staging area.Also, the staging area is a temporary area where you can review and select the changes that you desire to include in your following commit.
The git stash command in Git is used to temporarily save the current state of the working directory and index (including unstaged changes). This can be useful if you need to switch branches or shelve your changes for later due to any unexpected reason.

6)Snapshot:
A snapshot in Git is a representation of the state of a repository at a specific point in time during development. 
It is created when you commit your changes to the repository. The snapshot contains all the files and directories in the repository, as well as their metadata, such as the last time they were changed and the related contributor.
Commits are connected to snapshots as each commit creates a new snapshot. When you commit the changes  you made to your project, Git creates a new snapshot of the repository and then moves the branch pointer to that snapshot. This means that you can always go back to a previous commit by moving the branch pointer back to that previously mentioned snapshot.



