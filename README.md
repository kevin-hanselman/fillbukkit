fillbukkit
==========
A plugin manager for Craftbukkit Minecraft server plugins.

## Features
- Install/update Bukkit plugins
- Install/update Craftbukkit server JAR
- Configurable start/stop/restart server for easy integration?

## Usage
    fillbukkit <operation> [...]

### Operations
    -A, --add                Add/install a plugin
    -D, --disable            Disable installed plugins
    -E, --enable             Enable installed plugins
    -h, --help               Display this list of operations
    -L, --list               List installed plugins
    -V, --version            Display the version of fillbukkit
    -R, --remove             Remove a plugin
    -S, --search             Search for a plugin in [supported plugin list?]
    -U, --upgrade            Upgrade installed plugins

### General Options
    -h, --help               See available options for an operation
    -q, --quiet              Suppress standard operation output
    -r, --release            [-ADELS] Select the plugin release to use (stable, beta, dev)
    -a, --all                [-DELU] Perform operation for all installed plugins
    -c, --craftbukkit        [-U] Perform an operation on the Craftbukkit JAR

## Configuration File
- Path to Craftbukkit plugins folder
- Path to disabled plugins folder
- Default release (stable, beta, dev) of Craftbukkit to use
- Default release (stable, beta, dev) for plugins (if not specified)

## Plugin List File
Each plugin will be a Section and can have the following Properties:

### Required properties
- stable
- jars

### Optional properties
- beta
- dev
