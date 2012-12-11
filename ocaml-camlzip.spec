%define up_name	camlzip
%define name	ocaml-%{up_name}
%define version	1.04
%define release	8

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Reading and writing ZIP, JAR and GZIP files
License:	LGPLv2 with exceptions
Group:		Development/Other
URL:		http://pauillac.inria.fr/~xleroy/software.html
Source0: 	http://caml.inria.fr/distrib/bazar-ocaml/%{up_name}-%{version}.tar.gz
Patch0:		%{name}-1.03-findlib.patch
Patch1:		test-makefile.dpatch
Patch2:		uncompress.dpatch
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
%patch0 -p1
%patch1 -p1
%patch2 -p1
sed -i -e "s:@VERSION@:%{version}:g" META

%build
%make depend
%make all allopt
mkdir -p doc
ocamldoc -colorize-code -html gzip.mli zip.mli zlib.mli -d doc

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
%doc test doc
%{_libdir}/ocaml/zip/*.a
%{_libdir}/ocaml/zip/*.cmx
%{_libdir}/ocaml/zip/*.cmxa
%{_libdir}/ocaml/zip/*.mli


%changelog
* Wed May 09 2012 Crispin Boylan <crisb@mandriva.org> 1.04-8
+ Revision: 797738
- Rebuild

* Thu Sep 10 2009 Florent Monnier <blue_prawn@mandriva.org> 1.04-7mdv2011.0
+ Revision: 436253
- rebuild
- consistency naming with Debian and Fedora

* Sat Aug 22 2009 Florent Monnier <blue_prawn@mandriva.org> 1.04-6mdv2010.0
+ Revision: 419718
- increm mkrel
- corrected the license field

* Sat Aug 22 2009 Florent Monnier <blue_prawn@mandriva.org> 1.04-5mdv2010.0
+ Revision: 419580
- patch for plain_uncompress function from debian by Sven Luther
- added a patch for the makefile of the tests
- added test dir, with patched makefile (patch from debian by Samuel Mimram)
  generating html doc

* Sat Aug 22 2009 Florent Monnier <blue_prawn@mandriva.org> 1.04-4mdv2010.0
+ Revision: 419488
- added missing files zlib.cmi / zlib.mli
  modified the install dir, to align on fedora, debian and upstream

* Sat Jun 27 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.04-3mdv2010.0
+ Revision: 389923
- rebuild

* Thu Jan 08 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.04-2mdv2009.1
+ Revision: 327123
- site-lib hierarchy doesn't exist anymore

  + Florent Monnier <blue_prawn@mandriva.org>
    - findlib package name

* Sun Dec 21 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.04-1mdv2009.1
+ Revision: 317101
- new version
- move all non-devel files into main package (Florent Monnier <fmonnier@linux-nantes.org>)

* Tue Dec 09 2008 Pixel <pixel@mandriva.com> 1.03-8mdv2009.1
+ Revision: 312252
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 1.03-7mdv2009.0
+ Revision: 254187
- rebuild

* Tue Mar 04 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.03-5mdv2008.1
+ Revision: 178364
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 01 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.03-4mdv2008.0
+ Revision: 77659
- drop macro definition, now in rpm-mandriva-setup
  ship .cmi file in non-devel subpackage

* Fri Jun 22 2007 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.03-3mdv2008.0
+ Revision: 43333
- build 'allopt' too

* Tue Jun 19 2007 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.03-2mdv2008.0
+ Revision: 41275
- rebuild

* Fri Apr 27 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.03-1mdv2008.0
+ Revision: 18545
- Import ocaml-camlzip

