#!/usr/bin/env python

import os,sys

cwd = sys.argv[1]
mode = sys.argv[2]

os.chdir(cwd)
if os.path.isfile(".p4bracnch"):
    os.system("vgbuild --full64 --dir zebu --target clean_coverage ; vgbuild --full64 --dir zebu --debug --gcov ; vgbuild --full64 --dir zebu --debug --gcov --target l0_tests")
    if mode == "1":
        os.system("vgbuild --full64 --dir zebu --target report_summary")
else:
    os.system("vgbuild --full64 --dir test --target clean_coverage ; vgbuild --full64 --dir test --debug --gcov ; vgbuild --full64 --dir test --debug --gcov --target l0_tests")
    if mode == "1":
        os.system("vgbuild --full64 --dir test  --target report_coverage")

