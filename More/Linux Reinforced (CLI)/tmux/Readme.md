# Tmux 101
tmux, the terminal multiplexer, is easily one of the most used tools by the Linux community (and not just pentesters!). While not a malicious tool, tmux makes running simultaneous tasks throughout a pentest incredibly easy.

![tmux](Tmux_cheatsheet.png)

## Getting started
All tmux commands start with a keyboard button combination with control + B.

## Quick Commands
- `tmux` - Start a new tmux session
- `CTRL + B` + `D` - Detach from a tmux session
- `tmux ls` - List all tmux sessions
- `tmux new -s [session name]` - Create a new tmux session with a name
- `tmux attach -t [session name]` - Attach to a tmux session
- `tmux kill-session -t [session name]` - Kill a tmux session
- `tmux kill-session -a` - Kill all tmux sessions
- `tmux + B` + `C` - Create a new window
- `tmux + B` + `[` - Copy mode
- `tmux + B` + `g` - Go to top of window
- `tmux + B` + `G` - Go to top of window
- `tmux + B` + `q` - Exit copy mode
- `tmux + B` + `%` - Split window vertically
- `tmux + B` + `"` - Split window horizontally
- `tmux + B` + `X` - Kill pane
- `exit` - Exit session