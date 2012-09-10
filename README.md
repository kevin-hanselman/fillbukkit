fillbukkit
==========
A command-line Bukkit plugin manager for Craftbukkit-based Minecraft servers.

## Features
- Install, update, enable and disable Craftbukkit plugins
- Install and update the Craftbukkit server JAR
- No GUI required; perfect for lightweight Minecraft servers.

## Requirements
- Python 3.x

## Want to add support for a plugin?
Our goal is to expand the list of supported plugins over time. 
Make a pull request adding the plugin you'd like added to the [list of supported plugins][2]. 
Follow [the guidelines below][1] when adding a plugin to this list. We appreciate your help!

## Usage
    fillbukkit <operation> [...]

### Top-level Options
    -V, --version            Display the version of fillbukkit
    -h, --help               Display a list of operations

### Operations
    add                      Add/install a plugin
    disable                  Disable installed plugins
    enable                   Enable installed plugins
    ls                       List installed plugins
    rm                       Remove/uninstall plugins
    search                   Search for a supported plugin
    upgrade                  Upgrade installed plugins

### Sample Operation Options
    -h, --help               See more detailed options for an operation
    -r, --release            Select the plugin release to use (stable, beta, dev)
    -a, --all                Perform operation for all installed plugins

## Configuration File
These are the options provided in the file `fillbukkit.cfg`:
- `craftbukkit`: Path to base Craftbukkit server folder
- `plugins`: Path to Craftbukkit plugins folder. This shouldn't need to be changed.
- `update`: Path to the Craftbukkit plugins-update folder. This shouldn't need to be changed.
- `disabled`: Path to disabled plugins folder. This is where JARs not being run on your server will be temporarily stored.
- `dlcache`: Path to the folder to keep old downloaded archives. This allows `upgrade` to determine the need to copy new JARs.

## Plugin List File
These are the options provided in the file `dl.cfg`. 
Each plugin name is a `[section]` and has the following options:

### Required Plugin Properties
- `description`: a short description of the plugin
- `stable`: URL to the latest stable/recommended build of the plugin
- `format`: file format for the download URLs (one of `jar`, `zip`, `tar`, `bztar`, or `gztar`)

### Optional Plugin Properties
- `beta`: URL to the latest beta build of the plugin
- `dev`: URL to the latest bleeding-edge/dev build of the plugin

[1]:http://github.com/kevlar1818/fillbukkit#plugin-list-file
[2]:http://github.com/kevlar1818/fillbukkit/blob/master/dl.cfg