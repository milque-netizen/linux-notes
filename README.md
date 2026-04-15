### View all connected disks and mount points
```bash
lsblk
```
*Added on: 2026-04-15 16:20*

### desc
```bash
cmd
```
*Added on: 2026-04-15 16:22*

## Check current Asus laptop power profile (Quiet, Balanced, Performance)
```bash
asusctl -s
```
*Added on: 2026-04-15 16:26*

## View git commit history with GPG verification details
```bash
git log --show-signature
```
*Added on: 2026-04-15 16:29*

## Check disk partitions and mount points
```bash
lsblk
```
*Added on: 2026-04-15 16:40*

## How to prioritize IPv4 over IPv6 for faster connections
```bash
sudo nano /etc/gai.conf
```
*Added on: 2026-04-15 21:15*

## Test if GitHub recognizes my SSH/GPG key
```bash
ssh -T git@github.com
```
*Added on: 2026-04-15 22:20*

## Download files from the github
```bash
git clone git@github.com:milque-netizen/linux-notes.git
```
*Added on: 2026-04-15 22:25*

## Most recent commit on GitHub
```bash
git log -n 1 origin
```
*Added on: 2026-04-15 22:29*

## Go along with the new repository
```bash
git push -u origin main
```
*Added on: 2026-04-15 22:35*

## Check where my local repo is pushing its code
```bash
git remote -v
```
*Added on: 2026-04-15 22:37*

## View git commit history with GPG verification details
```bash
git log --show-signature
```
*Added on: 2026-04-15 22:46*

## Make it global (so you can use it anywhere)
```bash
sudo ln -sf ~/projects/linux-notes/note.py /usr/local/bin/note
```
*Added on: 2026-04-15 22:48*

## Create a link to the script in your local binary directory
```bash
sudo ln -s ~/projects/linux-notes/note.py /usr/local/bin/note
```
*Added on: 2026-04-15 22:50*

## Setup environment for the project (git init)
```bash
mkdir -p ~/projects/linux-notes && cd ~/projects/linux-notes
```
*Added on: 2026-04-15 22:54*

## Link local repo to your new GitHub repo
```bash
git remote add origin git@github.com:milque-netizen/test-signing.git
```
*Added on: 2026-04-15 22:58*

## Push the signed commit
```bash
git push -u origin main
```
*Added on: 2026-04-15 22:59*

## Start fresh connection with the GitHub
```bash
ssh -T git@github.com
```
*Added on: 2026-04-15 23:00*

