#!/usr/bin/env python3
import sys
from pathlib import Path
from collections import OrderedDict
import unittest
from debparse.deb_control import parse as debParse

import psutil
import sh
dpkgS = sh.dpkg.bake("-S")
dpkgs = sh.dpkg.bake("-s")

thisFile = Path(__file__).absolute()
thisDir = thisFile.parent.absolute()
repoMainDir = thisDir.parent.absolute()
sys.path.append(str(repoMainDir))

dict = OrderedDict

from File2Package import File2Package
from File2Package.interfaces import BasePackageRef, VersionedPackageRef
from AnyVer import AnyVer
from File2Package.backend.dpkg import defaultArch

class TestDebPkgResolver(unittest.TestCase):
	def testResolver(self):
		with File2Package("dpkg") as d:
			pr = psutil.Process()
			for m in pr.memory_maps():
				if m.path and m.path[0] == "/":
					p = Path(m.path)
					etalon = None
					try:
						res = dpkgS(p)
					except:
						continue
					res = res.rsplit(':', 1)[0].strip().split(":")
					if len(res) ==1:
						res.append(defaultArch)
					etalon = BasePackageRef(*res)
					res2 = debParse(data=str(dpkgs(etalon.name)))
					pkg = res2.packages[0]
					if "Version" in pkg:
						etalon = etalon.clone(cls=VersionedPackageRef, version=AnyVer(pkg["Version"].text))
					
					with self.subTest(etalon=etalon, path=p):
						ourP = d[p]
						self.assertEqual(ourP, etalon)


if __name__ == "__main__":
	unittest.main()
