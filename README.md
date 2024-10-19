# DroneApi
Api to handle all the request that comes to drone
#all github commands
1. Setup and Configuration
git config --global user.name "Your Name" # Set your username
git config --global user.email "your.email@example.com" # Set your email
2. Creating a New Repository
git init # Initialize a new repository
git clone <repository-url> # Clone an existing repository
3. Basic Workflow
git status # Check the status of the repository
git add <file> # Add a specific file to staging
git add . # Add all changes in the current directory
git commit -m "Commit message" # Commit changes with a message
4. Branching and Merging
git branch # List all branches
git branch <branch-name> # Create a new branch
git checkout <branch-name> # Switch to a branch
git checkout -b <branch-name> # Create and switch to a new branch
git merge <branch-name> # Merge a branch into the current branch
git branch -d <branch-name> # Delete a local branch
5. Working with Remote Repositories
git remote add <name> <repository-url> # Add a remote repository
git remote -v # View remote repositories
git fetch <remote-name> # Fetch changes from the remote repository
git pull <remote-name> <branch-name> # Pull changes from the remote repository
git push <remote-name> <branch-name> # Push changes to the remote repository
6. Stashing Changes
git stash # Stash changes
git stash list # List stashed changes
git stash apply # Apply stashed changes
git stash drop <stash@{n}> # Drop a specific stash
7. Tagging
git tag <tag-name> # Create a new tag
git tag # List all tags
git push <remote-name> --tags # Push tags to the remote repository
8. Undoing Changes
git reset <file> # Unstage a file
git revert <commit-id> # Revert a commit
git reset --hard <commit-id> # Reset to a previous commit (discard changes)
9. Checking Commit History
git log # View commit history
git diff # Show changes between commits
git diff <commit> # Compare with a specific commit
10. Miscellaneous
git branch --show-current # Show the current branch
git ls-files --others --exclude-standard # Check for untracked files
