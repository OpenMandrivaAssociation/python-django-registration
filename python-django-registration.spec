%define module django-registration
%define oname django_registration

Name:		python-django-registration
Version:	5.2.1
Release:	1
Summary:	A user-registration application for Django
Group:		Development/Python
License:	BSD
URL:		https://github.com/ubernostrum/django-registration
Source0:	%{URL}/archive/%{version}/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(confusable-homoglyphs)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(pdm-backend)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	python%{pyver}dist(django)
Requires:       python%{pyver}dist(django) >= 4.2

%description
This is a fairly simple user-registration application for Django_, designed to
make allowing user signups as painless as possible.

%files
%doc README.rst
%license LICENSE
%{py_puresitedir}/%{oname}
%{py_puresitedir}/%{oname}-%{version}.dist-info
