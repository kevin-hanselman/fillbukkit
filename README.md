fillbukkit
==========
A plugin manager for Craftbukkit Minecraft server plugins.

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
    search                   Search for a plugin in [supported plugin list?]
    upgrade                  Upgrade installed plugins

### Operation Options
    -h, --help               See more detailed options for an operation
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
- `format`: file format for the download URLs (e.g. jar, zip, tar, etc.)
- `jars`: a comma-separated list of JAR files used by the plugin (only accessed if `format` is not `jar`)

### Optional properties
- `beta`: URL to the latest beta build of the plugin
- `dev`: URL to the latest unstable/dev build of the plugin