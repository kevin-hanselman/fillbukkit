fillbukkit
==========
A command-line Bukkit plugin manager for Craftbukkit-based Minecraft servers.

## Features
- Install, update, enable and disable Craftbukkit plugins
- Install and update the Craftbukkit server JAR

## Requirements
- Python 3.x

## Want to add support for a plugin?
- Make a pull request adding a section to the plugin list file as described below

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
    rm                       Remove a plugin
    search                   Search for a supported plugin
    upgrade                  Upgrade installed plugins

### Operation Options
    -h, --help               See more detailed options for an operation
    -r, --release            Select the plugin release to use (stable, beta, dev)
    -a, --all                Perform operation for all installed plugins
    -c, --craftbukkit        Perform an operation on the Craftbukkit JAR

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