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
Version:	0.07
Release:	1
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
%if %{!?_with_tests:0}%{?_with_tests:1}
BuildRequires:	perl-File-Find-Rule
BuildRequires:	perl-Module-CoreList
BuildRequires:	perl-Test-Pod
BuildRequires:	perl-Test-Simple
BuildRequires:	perl(Test::Builder::Tester)
%endif
BuildRequires:	rpm-perlprov >= 3.0.3-26
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
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

# tests seem not to work - for unknown reason
%{?_with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT
mv -f $RPM_BUILD_ROOT%{_mandir}/man3/Prereq.3pm $RPM_BUILD_ROOT%{_mandir}/man3/Test::Prereq.3pm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_sitelib}/Test/*.pm
%{_mandir}/man3/*
