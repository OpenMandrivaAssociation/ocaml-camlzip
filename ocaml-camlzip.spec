%define up_name	camlzip
%define name	ocaml-%{up_name}
%define version	1.03
%define release	%mkrel 4

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Reading and writing ZIP, JAR and GZIP files
License:	GPL
Group:		Development/Other
URL:		http://pauillac.inria.fr/~xleroy/software.html
Source0: 	http://caml.inria.fr/distrib/bazar-ocaml/%{up_name}-%{version}.tar.bz2
Patch0:		%{name}-1.03-findlib.patch
BuildRequires:	ocaml
BuildRequires:	findlib
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

%build
%make depend
%make all allopt

%install
rm -rf %{buildroot}
install -d -m 755 %{buildroot}/%{ocaml_sitelib}/camlzip
install -d -m 755 %{buildroot}/%{ocaml_sitelib}/stublibs
make install OCAMLFIND_INSTFLAGS="-destdir %{buildroot}/%{ocaml_sitelib}"
rm -f %{buildroot}/%{ocaml_sitelib}/stublibs/*.owner

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc LICENSE README Changes
%dir %{ocaml_sitelib}/camlzip
%{ocaml_sitelib}/camlzip/*.cmi

%files devel
%defattr(-,root,root)
%{ocaml_sitelib}/camlzip/*
%exclude %{ocaml_sitelib}/camlzip/*.cmi
%{ocaml_sitelib}/stublibs/dllcamlzip.so
