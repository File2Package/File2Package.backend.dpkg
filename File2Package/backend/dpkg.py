import json
import typing
from pathlib import Path

import sh
from AnyVer import AnyVer
from fuckapt import *
from PackageRef import VersionedPackageRef


def init(interfaces):
	class DPKGFile2PackagePopulator(interfaces.IFile2PackagePopulator):
		__slots__ = ("infoFilesLoc", "defaultArch")

		def __init__(self, infoFilesLoc: Path = infoFilesLoc, defaultArch: str = defaultArch):
			self.infoFilesLoc = infoFilesLoc
			self.defaultArch = defaultArch

		def packagesMappingYielder(self, pkgs):
			index = {pkg["Package"].text: AnyVer(pkg["Version"].text) for pkg in readStatusFile() if "Version" in pkg}

			for p in pkgs:
				nameArch = p.stem.split(":")
				if len(nameArch) != 1:
					name, arch = nameArch
				else:
					name = nameArch[0]
					arch = self.defaultArch

				if name in index:
					ref = interfaces.VersionedPackageRef(name, arch, version=index[name])
				else:
					ref = interfaces.BasePackageRef(name, arch)

				yield interfaces.FilesPackageMapping(ref, self.__class__.filesYielder(p))

		def __call__(self):
			pkgs = tuple(self.infoFilesLoc.glob("*.list"))
			return len(pkgs), self.packagesMappingYielder(pkgs)

		@staticmethod
		def filesYielder(p: Path):
			with p.open("rt", encoding="utf-8") as f:
				for l in f:
					yield Path(l.strip())

	return DPKGFile2PackagePopulator
