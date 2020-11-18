# Curse Decompiler

The Curse Decompiler (`cursed`) is a Linux-only tool that will download any Minecraft mod from [CurseForge](https://www.curseforge.com), and decompile it automatically.

## Installation

Clone this repo, then run:

```sh
python3 setup.py install
```

Your system must have the `unzip` and `wget` programs installed.

## Usage

First, you must find the asset ID of a Minecraft mod. When downloading from the CurseForge website, this will be the number at the end of the URL. For example, the ID of the following download URl is `3101936`:

```
https://www.curseforge.com/minecraft/mc-mods/areas/download/3101936
```

With this URL, you can run

```sh
python3 -m cursed [mod name] [mod id]
```

Extra options can be viewed by running `python3 -m cursed -h`