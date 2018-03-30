#!/usr/bin/env python3

from distutils.core import setup

setup(name = "RazerTOP",
      version = "1.0",
      author = "Lucas C. Villa Real",
      author_email = "lucasvr@gobolinux.org",
      url = "https://github.com/lucasvr/RazerTOP",
      description = "Htop-like memory and cpu usage monitor using the Razer keyboard LEDs",
      long_description = "Htop-like memory and cpu usage monitor using the Razer keyboard LEDs",
      license = "GNU General Public License v3",
      classifiers = [
          "Environment :: Console",
          "Development Status :: 4 - Beta",
          "License :: OSI Approved :: GNU General Public License v3"
      ],
      platforms = ["Linux"],
      scripts = ["razertop"]
)
