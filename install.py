import os

li = [
    "mkdir $HOME/glibc/ && cd $HOME/glibc",
    "wget http://ftp.gnu.org/gnu/libc/glibc-2.34.tar.gz",
    "tar -xvzf glibc-2.34.tar.gz",
    "mkdir build",
    "mkdir glibc-2.34-install",
    "cd build",
    "../glibc-2.34/configure --prefix=$HOME/Final-Project-Priv-Escalation/glibc/glibc-2.34-install",
    "make",
    "make install"
]

for i in li:
    os.system(i)