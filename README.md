fillbukkit
==========
A plugin manager for Craftbukkit Minecraft server plugins.

## Requires
- Python 3.x

## Features
- Install/update Bukkit plugins
- Install/update Craftbukkit server JAR

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
    search                   Search for a plugin in [supported plugin list?]
    upgrade                  Upgrade installed plugins

### Operation Options
    -h, --help               See available options for an operation
    -q, --quiet              Suppress standard operation output
    -r, --release            Select the plugin release to use (stable, beta, dev)
    -a, --all                Perform operation for all installed plugins
    -c, --craftbukkit        Perform an operation on the Craftbukkit JAR

## Configuration File
- Path to base Craftbukkit server folder
- Path to Craftbukkit plugins folder
- Path to disabled plugins folder

## Plugin List File
Each plugin name is a `[section]` and has the following keys/options:

### Required properties
- `description`: a description of the plugin
- `stable`: URL to the latest stable build of the plugin
- `jars`: a list of JAR files used by the plugin
- `format`: file format for the download URLs (e.g. jar, zip, tar, etc.)

### Optional properties
- `beta`: URL to the latest beta build of the plugin
- `dev`: URL to the latest unstable/dev build of the plugin