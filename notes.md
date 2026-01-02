# Notes

## Git Basics

🔹 What is Git?
Git is a version control system
It tracks changes in code over time
Allows us to:
Save versions (snapshots)
Go back to old versions
Work safely without losing code

🔹 What is a Git Repository?
A folder tracked by Git
Created using git init
Contains a hidden .git folder
.git stores:
commit history
branches
configuration

🔹 Git Workflow (Big Picture)
Working Directory → Staging Area → Repository → GitHub
Working Directory: where we write/edit code
Staging Area: files selected for next commit
Repository: saved snapshots (commits)
GitHub: remote cloud copy

🔹 git init
Initializes Git in a folder
Starts tracking files
“Convert this folder into a Git repository”

🔹 git status
Purpose
Shows current state of the repository
Displays:
untracked files
modified files
staged files
Note
Safe command (does not change anything)

🔹git add
🔹git add README.md
🔹git add .
Purpose
Moves files to the staging area
Meaning:
Select files to include in the next commit
git add . → stages all changes
git add file.py → stages a specific file

🔹Staging Area (Important Concept)
Acts as a filter between editing and committing
Allows committing only selected changes
Prevents accidental or incomplete commits

🔹git commit
🔹git commit -m "Commit message"
Purpose:
Saves a snapshot of staged files
Commit message explains why the change was made
Meaning:
Save this version permanently
🔹What is a Commit?
A saved snapshot of the project
Each commit has:
unique ID (hash)
message
timestamp
Commits are reversible

🔹Branch
A branch is a timeline of commits
Default branch is usually main
You worked on the main branch

🔹git branch -M main
🔹git branch -M main
Purpose
Renames the current branch to main
Why
main is the modern standard
GitHub expects main by default

🔹What is GitHub?
A remote repository hosting platform
Stores code online
Used for:
backup
sharing
collaboration
interview portfolio

🔹Remote Repository
Remote = cloud version of the repository
Local repository must be connected to push code

🔹git remote add origin
🔹git remote add origin <repository-url>
Purpose
Connects local repository to GitHub
Meaning
Save this GitHub repository as origin
origin is just a nickname for the remote URL

🔹git remote -v
🔹git remote -v
Purpose
Shows connected remote repositories
Displays fetch and push URLs

🔹git push
🔹git push -u origin main
Purpose
Uploads local commits to GitHub
Explanation
origin → remote name
main → branch name
-u → sets upstream (future pushes need only git push)

One-Line Git Summary
git init   → start tracking
git add    → stage changes
git commit → save snapshot
git push   → upload to GitHub




## Python Notes
( You can add Python concepts later )

---

## LeetCode Patterns
( Add patterns as you learn )
