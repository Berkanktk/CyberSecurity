# Useful VIM commands
## Cursor movement
`h` - move cursor left  
`j` - move cursor down  
`k` - move cursor up  
`l` - move cursor right   
`H` - move to top of screen  
`M` - move to middle of screen  
`L` - move to bottom of screen  
`e` - jump forwards to the end of a word  
`0` - jump to the start of the line  
`gg` - go to the first line of the document   
`G` - go to the last line of the document  

## Editing
`r` - replace a single character.  
`R` - replace more than one character, until ESC is pressed.  
`J` - join line below to the current one with one space in between  
`cc` - change (replace) entire line  
`u` - undo  
`U` - restore (undo) last changed line  
`.` - repeat last command  

## Marking text (visual mode)
`v` - start visual mode, mark lines, then do a command (like y-yank)  
`V` - start linewise visual mode  
`o` - move to other end of marked area  
`aw` - mark a word  
`ab` - a block with ()  
`aB` - a block with {}    
`Esc` - exit visual mode

## Visual commands
`>` - shift text right  
`<` - shift text left   
`y` - yank (copy) marked text  
`d` - delete marked text  
`~` - switch case  
`u` - change marked text to lowercase  
`U` - change marked text to uppercase  

## Insert mode - inserting/appending text
`i` - insert before the cursor  
`I` - insert at the beginning of the line  
`a` - insert (append) after the cursor   
`A` - insert (append) at the end of the line  
`o` - append (open) a new line below the current line  
`O` - append (open) a new line above the current line  
`ea` - insert (append) at the end of the word  
`Esc` - exit insert mode  
 
## Marks and positions
`:marks` - list of marks  
`ma` - set current position for mark A  
`'a` - jump to position of mark A  
`:changes` - list of changes

## Macros
`qa` - record macro a  
`q` - stop recording macro  
`@a` - run macro a

## Cut and paste
`yy` - yank (copy) a line  
`2yy` - yank (copy) 2 lines  
`yw` - yank (copy) the characters of the word from the cursor position to the start of the next word  
`y$` - yank (copy) to end of line  
`p` - put (paste) the clipboard after cursor  
`P` - put (paste) before cursor  
`gp` - put (paste) the clipboard after cursor and leave cursor after the new text  
`dd` - delete (cut) a line  
`2dd` - delete (cut) 2 lines  
`D` - delete (cut) to the end of the line  
`d$` - delete (cut) to the end of the line  
`x` - delete (cut) character

## Indent text
`>>` - indent (move right) line one shiftwidth  
`<<` - de-indent (move left) line one shiftwidth

## Exiting
`:w` - write (save) the file, but don't exit  
`:w !sudo tee %` - write out the current file using sudo  
`:wq` - write (save) and quit  
`:q` - quit (fails if there are unsaved changes)  
`:q!` - quit and throw away unsaved changes  
`:wqa` - write (save) and quit on all tabs  

## Search and replace
`/pattern` - search for pattern  
`?pattern` - search backward for pattern  
`n` - repeat search in same direction  
`N` - repeat search in opposite direction  
`:%s/old/new/g` - replace all old with new throughout file

## Search in multiple files
`:vim[grep] /pattern/ {`{file}`}` - search for pattern in multiple files  
`:cn[ext]` - jump to the next match  
`:cp[revious]` - jump to the previous match  
`:cope[n]` - open a window containing the list of matches  

## Tabs
`:tabnew` open a file in a new tab