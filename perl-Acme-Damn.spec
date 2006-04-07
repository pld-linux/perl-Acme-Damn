#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Acme
%define	pnam	Damn
Summary:	Acme::Damn - 'Unbless' Perl objects
Summary(pl):	Acme::Damn - "odb³ogos³awianie" obiektów Perla
Name:		perl-Acme-Damn
Version:	0.03
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	02a3c8b947d3f2888bc2455f7405f7c1
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Acme::Damn provides a single routine, damn(), which takes a blessed
reference (a Perl object), and unblesses it, to return the original
reference. I can't think of any reason why you might want to do this,
but just because it's of no use doesn't mean that you shouldn't be
able to do it.

%description -l pl
Acme::Damn dostarcza jedn± funkcjê: damn(), która przyjmuje
pob³ogos³awion± referencjê (obiekt perlowy) i odb³ogos³awia j±, aby
zwróciæ oryginaln± referencjê. Nie znaleziono na razie powodu, ¿eby
to robiæ, ale to, ¿e takie dzia³anie nie ma zastosowania, nie znaczy,
¿e nie powinno daæ siê tego zrobiæ.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/Acme/*.pm
%dir %{perl_vendorarch}/auto/Acme/Damn
%{perl_vendorarch}/auto/Acme/Damn/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Acme/Damn/*.so
%{_mandir}/man3/*
