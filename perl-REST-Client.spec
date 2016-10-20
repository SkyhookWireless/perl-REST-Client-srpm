Name:           perl-REST-Client
Version:        272
Release:        1%{?dist}
Summary:        Simple client for interacting with RESTful http/https resources
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/REST-Client/
Source0:        http://www.cpan.org/modules/by-module/REST/REST-Client-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(Carp)
BuildRequires:  perl(CGI)
BuildRequires:  perl(constant)
BuildRequires:  perl(Crypt::SSLeay)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(HTTP::Server::Simple)
BuildRequires:  perl(HTTP::Server::Simple::CGI)
BuildRequires:  perl(Module::Install::Base)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More) >= 0.8
BuildRequires:  perl(URI)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XML::LibXML)
Requires:       perl(XML::LibXML)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
REST::Client provides a simple way to interact with HTTP RESTful resources.

%prep
%setup -q -n REST-Client-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc CHANGES
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Wed Jan 14 2015 David Dick <ddick@cpan.org> - 272-1
- Update to 272

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 271-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 271-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Mar 24 2014 David Dick <ddick@cpan.org> - 271-1
- Initial release
