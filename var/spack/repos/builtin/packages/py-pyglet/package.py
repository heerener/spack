# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyPyglet(PythonPackage):
    """pyglet is a cross-platform windowing and multimedia library for Python
    for developing games and other visually rich applications.
    """

    homepage = "https://github.com/pyglet/pyglet"
    pypi = "pyglet/pyglet-2.0.9-py3-none-any.whl"

    version(
        "2.0.10",
        sha256="e10a1f1a6a2dcfbf23155913746ff6fbf8ea18c5ee813b6d0e79d273bb2b3c18",
        expand=False,
    )
    version(
        "2.0.9",
        sha256="8520b22dde75f47167e1fedeed58ac0bb0c890c0dca17d8528427d6b318cd9cc",
        expand=False,
    )
    version("1.4.2", sha256="fda25ae5e99057f05bd339ea7972196d2f44e6fe8fb210951ab01f6609cdbdb7")
    version("1.2.1", sha256="d1afb253d6de230e73698377566da333ef42e1c82190216aa7a0c1b729d6ff4d")

    depends_on("py-setuptools", type="build")
    depends_on("py-future", type=("build", "run"))
    depends_on("python@2.7:2.8,3.4:", type=("build", "run"))

    def url_for_version(self, version):
        if version <= Version("1.4.2"):
            return (
                f"https://files.pythonhosted.org/packages/source/p/pyglet/pyglet-{version}.tar.gz"
            )
