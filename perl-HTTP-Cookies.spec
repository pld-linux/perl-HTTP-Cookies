#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	HTTP
%define		pnam	Cookies
%include	/usr/lib/rpm/macros.perl
Summary:	HTTP::Cookies - HTTP cookie jars
Summary(pl.UTF-8):	HTTP::Cookies - pojemnik na ciasteczka HTTP
Name:		perl-HTTP-Cookies
Version:	6.00
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/HTTP/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	21bed72b30a46604c152b7e25cf1cb45
URL:		http://search.cpan.org/dist/HTTP-Cookies/
BuildRequires:	perl-devel >= 1:5.8.8
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-HTTP-Date >= 6
BuildRequires:	perl-HTTP-Message >= 6
%endif
Requires:	perl-HTTP-Date >= 6
Requires:	perl-HTTP-Message >= 6
Conflicts:	perl-libwww < 6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This class is for objects that represent a "cookie jar" -- that is, a
database of all the HTTP cookies that a given LWP::UserAgent object
knows about.

This module implements the old style cookies as well as the new style
cookies described in RFC 2965.

Instances of the class HTTP::Cookies are able to store a collection
of Set-Cookie2: and Set-Cookie: headers and are able to use this
information to initialize Cookie-headers in HTTP::Request objects.
The state of a HTTP::Cookies object can be saved in and restored from
files.

%description -l pl.UTF-8
Klasa HTTP::Cookies jest przeznaczona dla obiektów reprezentujących
"pojemniki na ciasteczka" - tzn. bazę danych wszystkich ciasteczek
HTTP, jakie zna dany obiekt LWP::UserAgent.

Ten moduł implementuje ciasteczka starego typu, jak i nowego,
opisanego w RFC 2965.

Instancje klasy HTTP::Cookies mogą przechowywać zbiór nagłówków
Set-Cookie2: oraz Set-Cookie: i wykorzystywać te informacje do
zainicjowania nagłówków Cookie w obiektach HTTP::Request. Stan
obiektu HTTP::Cookies można zapisać w pliku, a później z niego
odtworzyć.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/HTTP/Cookies.pm
%{perl_vendorlib}/HTTP/Cookies
%{_mandir}/man3/HTTP::Cookies*.3pm*
