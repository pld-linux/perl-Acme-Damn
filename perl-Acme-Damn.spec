#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Acme
%define	pnam	Damn
Summary:	Acme::Damn - 'Unbless' Perl objects.
#Summary(pl):	
Name:		perl-Acme-Damn
Version:	0.02
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Acme/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	5728213d994298847d135192bd2f74b0
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Acme::Damn provides a single routine, damn(), which takes a blessed
reference (a Perl object), and unblesses it, to return the original
reference. I can't think of any reason why you might want to do this,
but just because it's of no use doesn't mean that you shouldn't be able
to do it.

# %description -l pl
# TODO

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
