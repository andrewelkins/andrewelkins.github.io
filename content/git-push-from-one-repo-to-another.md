Title: GIT push from one repo to another
Date: 2015-10-15 11:05
Author: Andrew Elkins
Category: PHP
Slug: git-push-from-one-repo-to-another
Status: published

Splitting off from a branch to another git repo seems like it would
suck. In reality it's simple. Two lines and you're set.

Things you'll need:

-   Source repo pulled down locally
-   Target repo created on your git server (GitHub, BitBucket,
    GitLab, etc)
-   Url for target git repo
-   Branches

> \$ cd /path/to/source  
> \$ git remote add
> targetrepo git@bitbucket.org:my\_team/my\_awesome\_target\_repo.git  
> \$ git push targetrepo my\_branch\_to\_create\_off\_of:master

That'll create the master branch off of the branch
"my\_branch\_to\_create\_off\_of" from your local repo.
