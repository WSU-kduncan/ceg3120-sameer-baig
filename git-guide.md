## Command line git

- status
  - Shows status of the local repository. This status includes:
    - number of local commits that have not been synced with remote (GitHub)
    - list of files in local folder than are NOT being tracked by git
    - list of files in local folder that have changes that need to be committed
  - `git status`
- clone
	- Connects the remote repository to the local system being used
	- `git clone git@github.com:professor/student.git`
- add
	- Adds tracking to files to push to Github
	- `git add filename`
- rm
	- Removes tracking and deletes the file
		- `git rm filename`
	- Removes tracking but keeps the actual file saved
		- `git rm --cached filename`
- commit
	- Saves the changes to the file, allows to add a log to detail changes
	- `git commit`
- push
	- Sends the changes made on files with tracking to the remote reposistory
	- `git push`
- fetch
	- Gathers all commits made from the remote repository, does not merge with the current branch
	- `git fetch`
- merge
	- Combines all commits in the local repository to current branch
	- `git merge`
- pull
	- Retrieves data from remote repository, and combines it to current branch
	- `git pull`
- branch
	- Creates branches, as well as listing them, and allows for renaming and deleting them as well
	- `git branch branch_name`
- checkout
	- Allows user to move to another branch
	- `git checkout branch_name`

## git files & folders

- .git folder
	- Folder that contains all information relating to version control, like tracking and managing changes to files and code
- .gitignore file
	- File that tells Git to ignore when files are being commited and pushed to Github

## GitHub

- Pull requests
- SSH authentication to repositories
