#
# Conditional build:
# _with_tests - perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Test
%define		pnam	Prereq
Summary:	Test::Prereq Perl module - check if Makefile.PL has the right pre-requisites
Summary(pl):	Modu� Perla Test::Prereq - sprawdzanie, czy spe�nione s� zale�no�ci podane w Makefile.PL
Name:		perl-Test-Prereq
Version:	0.19
Release:	3
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ce3fba34ac610400de95c37e82796aa6
Patch0:		%{name}_typo.patch
BuildRequires:	perl >= 5.6
%if %{!?_with_tests:0}%{?_with_tests:1}
BuildRequires:	perl-File-Find-Rule
BuildRequires:	perl-Module-CoreList
BuildRequires:	perl-Test-Manifest >= 0.9
BuildRequires:	perl-Test-Pod
BuildRequires:	perl-Test-Simple
BuildRequires:	perl(Test::Builder::Tester)
%endif
BuildRequires:	rpm-perlprov >= 4.0.2-104
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The prereq_ok() function examines the modules it finds in blib/lib/
and the test files it finds in t/. It figures out which modules they
use, skips the modules that are in the Perl core, and compares the
remaining list of modules to those in the PREREQ_PM section of
Makefile.PL.

THIS IS ALPHA SOFTWARE. IT HAS SOME PROBLEMS.

%description -l pl
Funkcja prereq_ok() sprawdza modu�y, kt�re znajdzie w blib/lib/ oraz
pliki test�w, kt�re znajdzie w t/. Okre�la, kt�rych modu��w u�ywaj�,
pomija modu�y nale��ce do podstawowego Perla i por�wnuje list� modu��w
z tymi podanymi w sekcji PREREQ_PM w Makefile.PL.

TO JEST OPROGRAMOWANIE ALPHA. MA TROCH� PROBLEM�W.

%package Build
Summary:	Test::Prereq::Build Perl module - test prerequisites in Module::Build scripts
Summary(pl):	Modu� Perla Test::Prereq::Build - wst�pne sprawdzanie w skryptach Module::Build
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}-%{release}

%description Build
Test::Prereq::Build Perl module overrides methods in Test::Prereq to
make it work with Module::Build.

%description Build -l pl
Modu� Perla Test::Prereq::Build przes�ania metody Test::Prereq, aby
umo�liwi� jego wsp�prac� z Module::Build.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1

%build
%{__perl} Makefile.PL
%{__make}

# tests seem not to work - for unknown reason
%{?_with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_sitelib}/Test/*.pm
%{_mandir}/man3/*Prereq.3*

%files Build
%defattr(644,root,root,755)
%dir %{perl_sitelib}/Test/Prereq
%{perl_sitelib}/Test/Prereq/*.pm
%{_mandir}/man3/*Build.3*
