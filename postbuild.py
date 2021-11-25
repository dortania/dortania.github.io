import re, subprocess, datetime, sys
from pathlib import Path

for directory in ["latest", "release"]:
    configuration_path = Path("Deploy/" + directory + "/Configuration.html")
    differences_path = Path("Deploy/" + directory + "/Differences.html")
    errata_path = Path("Deploy/" + directory + "/Errata.html")

    configuration = configuration_path.read_text()
    differences = differences_path.read_text()
    errata = errata_path.read_text() if errata_path.exists() else "" # Errata not in 0.5.9 yet

    # Strip table garbage
    table = [re.compile(r'<tr style="[\w \d\-:;]*" id="TBL-\d+-\d+-">(<td style="[\w \d\-:;]*" id="TBL-\d+-\d+-\d+" class="td\d\d">\s*<\/td>)+\s*<\/tr>'),
                re.compile(r'<tr style="[\w \d\-:;]*" id="TBL-\d+-\d+-">(<td colspan="2" style="[\w \d\-:;]*" id="TBL-\d+-\d+-\d+" class="td\d\d">\s*<span class="cmidrule">.*?<\/span>\s*<\/td>)+\s*<\/tr>'),
                re.compile(r'<td class="align-(even|label)">\s*<\/td>')]
    for i in table:
        configuration = i.sub("", configuration)

    # Fix font-family stuff
    font_family = re.compile(r'font-family="(.*?)" font-size="(.*?)"')
    font_family_replacement = 'class="\\1-\\2"'
    configuration = font_family.sub(font_family_replacement, configuration)
    errata = font_family.sub(font_family_replacement, errata)

    # Fix svg
    svg = re.compile(r'<!--l\. \d{3}--><p class="noindent" >\s+<!--l\. \d{3}--><p class="noindent" ><object.*?<p>SVG-Viewer needed.</p></object>\s+Figure 1. Directory Structure</p>')
    configuration = svg.sub("The directory structure was unable to be rendered and was therefore removed.", configuration)

    # Fix random </p> at beginning of differences
    if differences[:5] == "</p>\n":
        differences = differences[5:]

    # Add head and body tags to differences
    differences = """<!DOCTYPE html> \n<html lang="en-US" xml:lang="en-US" > \n<head><title>Differences</title> \n<meta  charset="utf-8" /> \n<meta name="generator" content="TeX4ht (http://www.tug.org/tex4ht/)" /> \n<meta name="viewport" content="width=device-width,initial-scale=1" /> \n<link rel="stylesheet" type="text/css" href="Differences.css" /> \n<meta name="src" content="Differences.tex" /> \n</head><body \n>""" + differences
    differences += "</body>\n</html>"

    # Fix title
    configuration = configuration.replace("<title></title>", "<title>Configuration</title>")
    errata = errata.replace("<title></title>", "<title>Errata</title>")

    # Add custom CSS
    configuration = configuration.replace("</head>", """<link rel="stylesheet" type="text/css" href="../main.css" /></head>""")
    errata = errata.replace("</head>", """<link rel="stylesheet" type="text/css" href="../main.css" /></head>""")
    differences = differences.replace("</head>", """<link rel="stylesheet" type="text/css" href="../main.css" /></head>""")

    # Fix logo
    configuration = configuration.replace("Logos/Logo-.png", "Logos/Logo.png")
    errata = errata.replace("../Logos/Logo-.png", "Logos/Logo.png")
    differences = differences.replace("../Logos/Logo-.png", "Logos/Logo.png")

    # Write back to file
    configuration_path.write_text(configuration)
    differences_path.write_text(differences)
    if errata:
        errata_path.write_text(errata)

index = Path("Deploy/README.md").read_text()

# Add commit hash, release name, and date to index
commit_hash = subprocess.run("git rev-parse HEAD".split(), capture_output=True, cwd=Path("latest")).stdout.decode().strip()
index = index.replace("COMMIT_HASH_FULL", commit_hash)
index = index.replace("COMMIT_HASH", commit_hash[:8])
index = index.replace("RELEASE_NAME", sys.argv[1])
index = index.replace("COMPILE_TIME", datetime.datetime.now(tz=datetime.timezone.utc).strftime("%Y-%m-%d %X (%Z)"))

# Write back to file
Path("Deploy/README.md").write_text(index)
