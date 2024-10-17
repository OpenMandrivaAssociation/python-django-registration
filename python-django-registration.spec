%define realname django-registration

Name:           python-django-registration
Version:	3.0.1
Release:	1
Summary:        A user-registration application for Django

Group:          Development/Python
License:        BSD
URL:            https://bitbucket.org/ubernostrum/django-registration
Source0:	https://files.pythonhosted.org/packages/21/af/e24c34910a04b9cc5eee5238334d03df4fff10df892831f49bc309c1e636/django-registration-3.0.1.tar.gz

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

