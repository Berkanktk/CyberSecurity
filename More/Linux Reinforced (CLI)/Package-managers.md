# Package management in linux

# General information
| Command   | Description                                                                                       |
| --------- | ------------------------------------------------------------------------------------------------- |
| dpkg      | The `dpkg` is a tool to install, build, remove, and manage Debian packages.                        |
| apt       | Apt provides a high-level command-line interface for the package management system.               |
| aptitude  | Aptitude is an alternative to apt and is a high-level interface to the package manager.            |
| snap      | Install, configure, refresh, and remove snap packages. Snaps enable the secure distribution of the latest apps and utilities. |
| gem       | Gem is the front-end to RubyGems, the standard package manager for Ruby.                            |
| pip       | Pip is a Python package installer recommended for installing Python packages not available in the Debian archive. |
| git       | Git is a fast, scalable, distributed revision control system with an unusually rich command set.    |

# Specific information
## apt
- relies on a repository
- apt list = list installed packages
- apt show <name> = description
- apt remove <name> = remove package
- apt purge <name> = remove package and configs
- sudo apt update && sudo apt full-upgrade = upgrade repoes

## aptitude
- interactive gui

## snap
- like a store
- devs can add apps to the store
- apt install snapd