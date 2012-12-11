%define realname django-registration

Name:           python-django-registration
Version:        0.7
Release:        %mkrel 3
Summary:        A user-registration application for Django

Group:          Development/Python
License:        BSD
URL:            http://bitbucket.org/ubernostrum/django-registration
Source0:        http://bitbucket.org/ubernostrum/django-registration/get/v%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildArch:      noarch
BuildRequires:  python-devel
BuildRequires:	python-setuptools
Requires:       python-django

%description
This is a fairly simple user-registration application for Django_, designed to
make allowing user signups as painless as possible.

%prep
%setup -q -n %{realname}

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc AUTHORS.txt CHANGELOG.txt LICENSE.txt README.txt docs/
%{py_puresitedir}/*


%changelog
* Tue Nov 02 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.7-3mdv2011.0
+ Revision: 592246
- rebuild for python 2.7

* Fri Feb 12 2010 Jérôme Brenier <incubusss@mandriva.org> 0.7-2mdv2010.1
+ Revision: 505132
- fix summary
- import python-django-registration


