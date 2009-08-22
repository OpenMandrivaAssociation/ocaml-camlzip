%define up_name	camlzip
%define name	ocaml-%{up_name}
%define version	1.04
%define release	%mkrel 4

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Reading and writing ZIP, JAR and GZIP files
License:	GPL
Group:		Development/Other
URL:		http://pauillac.inria.fr/~xleroy/software.html
Source: 	http://caml.inria.fr/distrib/bazar-ocaml/%{up_name}-%{version}.tar.gz
Patch:		%{name}-1.03-findlib.patch
BuildRequires:	ocaml
BuildRequires:	ocaml-findlib
BuildRequires:	zlib-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This Objective Caml library provides easy access to compressed files in ZIP and
GZIP format, as well as to Java JAR files. It provides functions for reading
from and writing to compressed files in these formats.

%package	devel
Summary:	Development files for %{name}
Group:		Development/Other
Requires:	zlib-devel
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains the development files needed to build applications
using %{name}.

%prep
%setup -q -n %{up_name}-%{version}
%patch -p1
sed -i -e "s:@VERSION@:%{version}:g" META

%build
%make depend
%make all allopt

%install
rm -rf %{buildroot}
install -d -m 755 %{buildroot}/%{_libdir}/ocaml/zip
install -d -m 755 %{buildroot}/%{_libdir}/ocaml/stublibs
make install OCAMLFIND_INSTFLAGS="-destdir %{buildroot}/%{_libdir}/ocaml"

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc LICENSE README Changes
%dir %{_libdir}/ocaml/zip
%{_libdir}/ocaml/zip/*.cmi
%{_libdir}/ocaml/zip/*.cma
%{_libdir}/ocaml/zip/META
%{_libdir}/ocaml/stublibs/dllcamlzip.so
%{_libdir}/ocaml/stublibs/dllcamlzip.so.owner

%files devel
%defattr(-,root,root)
%{_libdir}/ocaml/zip/*.a
%{_libdir}/ocaml/zip/*.cmx
%{_libdir}/ocaml/zip/*.cmxa
%{_libdir}/ocaml/zip/*.mli
