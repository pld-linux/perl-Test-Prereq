#
# Conditional build:
# _with_tests - perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Test
%define		pnam	Prereq
Summary:	Test::Prereq Perl module - check if Makefile.PL has the right pre-requisites
Summary(pl):	Modu³ Perla Test::Prereq - sprawdzanie, czy spe³nione s± zale¿no¶ci podane w Makefile.PL
Name:		perl-Test-Prereq
Version:	0.19
Release:	2
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ce3fba34ac610400de95c37e82796aa6
BuildRequires:	perl-devel >= 5.6
%if %{!?_with_tests:0}%{?_with_tests:1}
BuildRequires:	perl-File-Find-Rule
BuildRequires:	perl-Module-CoreList
BuildRequires:	perl-Test-Manifest >= 0.9
BuildRequires:	perl-Test-Pod
BuildRequires:	perl-Test-Simple
BuildRequires:	perl(Test::Builder::Tester)
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
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
Funkcja prereq_ok() sprawdza modu³y, które znajdzie w blib/lib/ oraz
pliki testów, które znajdzie w t/. Okre¶la, których modu³ów u¿ywaj±,
pomija modu³y nale¿±ce do podstawowego Perla i porównuje listê modu³ów
z tymi podanymi w sekcji PREREQ_PM w Makefile.PL.

TO JEST OPROGRAMOWANIE ALPHA. MA TROCHÊ PROBLEMÓW.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
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
%{perl_vendorlib}/Test/*.pm
%dir %{perl_vendorlib}/Test/Prereq
%{perl_vendorlib}/Test/Prereq/*.pm
%{_mandir}/man3/*
