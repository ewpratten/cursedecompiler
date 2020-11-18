import argparse
import os
from typing import *
import requests
import shutil

FERNFLOWER_URL = "https://jitpack.io/com/github/MinecraftForge/FernFlower/master/FernFlower-master.jar"


def generateJarDownloadURL(file_id: int, name: Optional[str] = "unnamed") -> str:
    """Generates the download URL for a specific mod

    Args:
        file_id (int): CurseForge file ID
        name (Optional[str], optional): Mod name. Defaults to "unnamed".

    Returns:
        str: Download URL
    """
    return f"https://www.cursemaven.com/curse/maven/{name}/{file_id}/{name}-{file_id}.jar"


def writeRemoteFileLocally(local_uri: str, url: str):
    os.system(f"wget {url} -O {local_uri}")

    # resource = requests.get(url, headers={
    #     "Accept": "application/java-archive"}, stream=True)
    # resource.raw.decode_content = True

    # with open(local_uri, "wb") as fp:
    #     shutil.copyfileobj(resource.raw, fp)


def main() -> int:

    ap = argparse.ArgumentParser(
        prog="cursed", description="A tool to decompile Minecraft mods straight from CurseForge")
    ap.add_argument("name", help="Mod name")
    ap.add_argument("file_id", help="CurseForge file ID", type=int)
    ap.add_argument("-w", "--workspace", help="Path to custom workspace root",
                    default="/tmp/cursedecompiler")
    ap.add_argument("-f", "--fernflower", help="Path to custom FernFlower JAR")
    ap.add_argument("-j", "--java", help="Path to custom Java")
    args = ap.parse_args()

    java_path: str
    if args.java:
        java_path = args.java
    else:
        if os.system("which java"):
            print("Java not in PATH")
            return 1
        else:
            java_path = os.path.expandvars("$JAVA_HOME/bin/java")
    print(f"Using Java: {java_path}")

    if not os.path.exists(f"{args.workspace}/{args.name}"):
        os.makedirs(f"{args.workspace}/{args.name}/source")
        print("Created workspace")

    download_url = generateJarDownloadURL(args.file_id, args.name)
    print(f"Found JAR at: {download_url}")

    print("Downloading mod JAR")
    compiled_jar_path = f"{args.workspace}/{args.name}/{args.name}.jar"
    writeRemoteFileLocally(compiled_jar_path, download_url)

    fernflower_path: str
    if not args.fernflower:
        fernflower_path = f"{args.workspace}/fernflower.jar"
        if os.path.isfile(fernflower_path):
            print("Found fernflower")
        else:
            print("Downloading FernFlower")
            writeRemoteFileLocally(fernflower_path, FERNFLOWER_URL)
    else:
        print("Using custom fernflower")
        fernflower_path = args.fernflower

    command = f"{java_path} -jar {fernflower_path} {compiled_jar_path} {args.workspace}/"
    print(f"{command}")
    status = os.system(command)

    os.system(f"unzip -d{args.workspace}/{args.name}/source {args.workspace}/{args.name}.jar ")

    if status == 0:
        print(
            f"Decompiled sources are in: {args.workspace}/{args.name}/source")

    return status


if __name__ == "__main__":
    exit(main())
