# Prep steps (off camera). Replace ADMIN and CONTRIB with the two usernames.

## 1. Contributor account (5 min)
- github.com > Sign up with the @expert.micro1.ai address. Username: something plain, e.g. the
  expert handle. Verify the email. Upload no real photo; the default avatar is fine.
- Add an SSH key for this account: `ssh-keygen -t ed25519 -f ~/.ssh/id_contrib -C contrib` then
  Settings > SSH and GPG keys > New SSH key, paste `~/.ssh/id_contrib.pub`.
- Add to `~/.ssh/config`:
  ```
  Host github-contrib
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_contrib
    IdentitiesOnly yes
  ```

## 2. Repository as ADMIN (10 min)
- github.com > New repository: name `orders-api`, Public, no README (we push our own). Create.
- On this Mac, in a fresh folder:
  ```
  mkdir -p ~/nodus/admin && cd ~/nodus/admin
  cp -R <this task folder>/prep orders-api && cd orders-api && rm PREP_STEPS.md
  git init -b main && git add -A && git commit -m "Initial order pricing service with tests"
  git remote add origin git@github.com:ADMIN/orders-api.git   # or the https URL
  git push -u origin main
  ```
- Actions tab: the `tests` workflow runs on that push. Wait for the green check. This first run is
  what makes `tests` selectable later as a required status check.
- Settings > Collaborators and teams > Add people > CONTRIB with **Write**. Accept the invitation
  from the contributor account (email link or github.com notifications).
- Settings > Rules > Rulesets: confirm it is empty. Leave it empty.

## 3. Contributor clone (5 min)
```
mkdir -p ~/nodus/contrib && cd ~/nodus/contrib
git clone git@github-contrib:ADMIN/orders-api.git && cd orders-api
git config user.name "CONTRIB" && git config user.email "CONTRIB@users.noreply.github.com"
git remote -v      # must show github-contrib, so the push uses the contributor key
```
- Check the identity works without any prompt: `git fetch` (no password, no token).
- In the Terminal window you will record from: `export PS1='$ '` so the Mac user and host name
  are not on screen. Keep this window as the contributor's terminal.

## 4. Browser windows
- Window A: signed in as ADMIN, one tab on github.com/ADMIN/orders-api. Bookmarks bar hidden.
- Window B (a different Chrome profile, or Safari, or a private window): signed in as CONTRIB, one
  tab on the same repo.
- Notifications off (macOS Focus). Nothing else open.

## 5. Rehearsal (10 min), then reset
- Run the whole shot list once without recording. Then reset so the recording starts clean:
  - Admin: Settings > Rules > Rulesets > protect-main > delete.
  - Close the rehearsal PR without merging; delete the branch `docs/readme-maintainers` on GitHub.
  - Contributor terminal: `git switch main && git fetch && git reset --hard origin/main &&
    git branch -D docs/readme-maintainers`.
  - If the rehearsal merged anything, revert on main so README is back to the original.
- Confirm again: Rulesets empty, Actions has a green `tests` run, contributor clone on `main`.
