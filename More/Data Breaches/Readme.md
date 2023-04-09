# BreachCompilation
Here is a link for downloading a compilation of various data breaches (sadly I don't have the platforms they are from). The folder size is 44GB and contains a sorted list of user credentials in plain text. 

Download breached password list from magnet located here: `magnet:?xt=urn:btih:7ffbcd8cee06aba2ce6561688cf68ce2addca0a3&dn=BreachCompilation&tr=udp%3A%2F%2Ftracker.openbittorrent.com%3A80&tr=udp%3A%2F%2Ftracker.leechers-paradise.org%3A6969&tr=udp%3A%2F%2Ftracker.coppersurfer.tk%3A6969&tr=udp%3A%2F%2Fglotorrents.pw%3A6969&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337`

I've already checked the link for malicious content using [Emailveritas](https://www.emailveritas.com/url-checker-results), and it is completely safe.

## How to download the file
Download it by using a torrent client.

I did it by installing `transmission-cli` from the terminal:
```bash
sudo apt install transmission-cli
```

Then I ran the command:
```bash
transmission-cli magnet:?xt=urn:btih:7ffbcd8cee06aba2ce6561688cf68ce2addca0a3&dn=BreachCompilation&tr=udp%3A%2F%2Ftracker.openbittorrent.com%3A80&tr=udp%3A%2F%2Ftracker.leechers-paradise.org%3A6969&tr=udp%3A%2F%2Ftracker.coppersurfer.tk%3A6969&tr=udp%3A%2F%2Fglotorrents.pw%3A6969&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337
```

This will start downloading the file. It will take a while, and you can actually see the files on your computer by going into your `/Downloads` folder. The folder is called `BreachCompilation`.

## How to use the breach compilation
Move into the folder
```bash
cd Downloads/BreachCompilation/ # query scripts and readme can be found here
cd Downloads/BreachCompilation/data # the actual location of the data.
```

Then you can use the `grep` command to manually search for a specific password, email, domain or username. Its fully up to you. Here is an example of searching for the email `johndoe@hotmail.com`

```bash
grep -Ri "johndoe@hotmail.com" ./*
```

Since there is lots of subfolders sorted alphabetically(`a/`, `b/`, `c/`, etc.), using grep recursively with the `-R` flag will search through all of them. 

The `-i` flag is used to ignore case sensitivity. 

The `./` is used to search from the current directory.

