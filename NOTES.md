# Notes

## Ubuntu

Ubuntu and its derivatives have a file `/etc/debian_version` that carries that
information about the Debian version it kind of relates to.

It can also be examined in different versions using docker:

    $ docker run --rm ubuntu:21.10 cat /etc/debian_version
    11.0

    $ docker run --rm ubuntu:22.10 cat /etc/debian_version
    bookworm/sid

    $ docker run --rm ubuntu:23.10 cat /etc/debian_version
    trixie/sid

    $ docker run --rm ubuntu:24.10 cat /etc/debian_version
    trixie/sid

    $ docker run --rm ubuntu:20.04 cat /etc/debian_version
    bullseye/sid

    $ docker run --rm ubuntu:22.04 cat /etc/debian_version
    bookworm/sid

    $ docker run --rm ubuntu:24.04 cat /etc/debian_version
    trixie/sid

Here's a comprehensive list: https://askubuntu.com/questions/445487/what-debian-version-are-the-different-ubuntu-versions-based-on

## libosinfo

The project libosinfo has GPL-licensed data here: https://gitlab.com/libosinfo/osinfo-db/-/blob/main

Specifically, https://gitlab.com/libosinfo/osinfo-db/-/tree/main/data/os has
one directory per OS with files per version, i.e. here is
[a file for Trisquel 11](https://gitlab.com/libosinfo/osinfo-db/-/blob/main/data/os/trisquel.info/trisquel-11.xml.in)
that has some information about the fact that it derives from Ubuntu 22.04:

    <derives-from id="http://ubuntu.com/ubuntu/22.04"/>
