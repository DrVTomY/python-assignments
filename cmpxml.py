from xmldiff import main, formatting

diff = main.diff_files('xml1.xml', 'xml2.xml', formatter=formatting.XMLFormatter(normalize=formatting.WS_BOTH))

print(diff)
