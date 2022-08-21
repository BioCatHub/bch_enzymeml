import libcombine
import os


if os.path.exists("assets/TESTOMEX.omex"):
    os.remove("assets/TESTOMEX.omex")  

archive = libcombine.CombineArchive()
archive.initializeFromArchive("assets/testfile.omex")
archive.addFile("assets/biocathub.json", "test.json",libcombine.KnownFormats.lookupFormat("json"))
archive.writeToFile("assets/TESTOMEX.omex")


