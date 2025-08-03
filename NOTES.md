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
one directory per OS with files per version, e.g. here is
[a file for Trisquel 11](https://gitlab.com/libosinfo/osinfo-db/-/blob/main/data/os/trisquel.info/trisquel-11.xml.in)
that has some information about the fact that it derives from Ubuntu 22.04:

    <derives-from id="http://ubuntu.com/ubuntu/22.04"/>

## /etc/os-release

Ubunutu and Linux Mint have a file called `/etc/os-release`

    $ cat /etc/os-release
    NAME="Linux Mint"
    VERSION="20.3 (Una)"
    ID=linuxmint
    ID_LIKE=ubuntu
    PRETTY_NAME="Linux Mint 20.3"
    VERSION_ID="20.3"
    HOME_URL="https://www.linuxmint.com/"
    SUPPORT_URL="https://forums.linuxmint.com/"
    BUG_REPORT_URL="http://linuxmint-troubleshooting-guide.readthedocs.io/en/latest/"
    PRIVACY_POLICY_URL="https://www.linuxmint.com/"
    VERSION_CODENAME=una
    UBUNTU_CODENAME=focal

    $ docker run --rm ubuntu:24.04 cat /etc/os-release
    PRETTY_NAME="Ubuntu 24.04.2 LTS"
    NAME="Ubuntu"
    VERSION_ID="24.04"
    VERSION="24.04.2 LTS (Noble Numbat)"
    VERSION_CODENAME=noble
    ID=ubuntu
    ID_LIKE=debian
    HOME_URL="https://www.ubuntu.com/"
    SUPPORT_URL="https://help.ubuntu.com/"
    BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
    PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
    UBUNTU_CODENAME=noble
    LOGO=ubuntu-logo
