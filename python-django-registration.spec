%define realname django-registration

Name:           python-django-registration
Version:        1.0
Release:        1
Summary:        A user-registration application for Django

Group:          Development/Python
License:        BSD
URL:            http://bitbucket.org/ubernostrum/django-registration
Source0:        https://pypi.python.org/packages/source/d/django-registration/django-registration-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python-devel
BuildRequires:	python-setuptools
Requires:       python-django

%description
This is a fairly simple user-registration application for Django_, designed to
make allowing user signups as painless as possible.

%prep
%setup -q -n %{realname}-%{version}

%build
%{__python} setup.py build

%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%clean

%files
%doc docs/
%{py_puresitedir}/*

