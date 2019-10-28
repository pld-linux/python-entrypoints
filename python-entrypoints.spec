#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Discover and load entry points from installed packages
Summary(pl.UTF-8):	Wykrywanie i wczytywanie punktów wejścia z zainstalowanych pakietów
Name:		python-entrypoints
Version:	0.3
Release:	2
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/entrypoints/
Source0:	https://files.pythonhosted.org/packages/source/e/entrypoints/entrypoints-%{version}.tar.gz
# Source0-md5:	c5c61ea2e46a0c50ea08f4af7955a0b1
Patch0:		%{name}-use_setuptools.patch
URL:		https://pypi.org/project/entrypoints/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-configparser >= 3.5
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-pytest
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.5
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-pytest
%endif
%endif
%if %{with doc}
BuildRequires:	sphinx-pdg
%endif
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Entry points are a way for Python packages to advertise objects with
some common interface. The most common examples are console_scripts
entry points, which define shell commands by identifying a Python
function to run.

Groups of entry points, such as console_scripts, point to objects with
similar interfaces. An application might use a group to find its
plugins, or multiple groups if it has different kinds of plugins.

The entrypoints module contains functions to find and load entry
points.

%description -l pl.UTF-8
Punty wejścia to sposób, w jaki pakiety Pythona udostępniają obiekty z
jakimś wspólnym interfejsem. Najpowszechniejszym przykładem są punkty
wejściowe skryptów konsoli (console_scripts), definiujące polecenia
powłoki poprzez określanie funkcji pythonowych do uruchomienia.

Grupy punktów wejścia, takie jak console_scripts, wskazują na obiekty
z podobnymi interfejsami. Aplikacja może używać grupy do znalezienia
swoich wtyczek, lub wielu grup, jeśli używa wtyczek różnych rodzajów.

Moduł entrypoints zawiera funkcje pomagające znajdować i ładować
punkty wejścia.

%package -n python3-entrypoints
Summary:	Discover and load entry points from installed packages
Summary(pl.UTF-8):	Wykrywanie i wczytywanie punktów wejścia z zainstalowanych pakietów
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.5

%description -n python3-entrypoints
Entry points are a way for Python packages to advertise objects with
some common interface. The most common examples are console_scripts
entry points, which define shell commands by identifying a Python
function to run.

Groups of entry points, such as console_scripts, point to objects with
similar interfaces. An application might use a group to find its
plugins, or multiple groups if it has different kinds of plugins.

The entrypoints module contains functions to find and load entry
points.

%description -n python3-entrypoints -l pl.UTF-8
Punty wejścia to sposób, w jaki pakiety Pythona udostępniają obiekty z
jakimś wspólnym interfejsem. Najpowszechniejszym przykładem są punkty
wejściowe skryptów konsoli (console_scripts), definiujące polecenia
powłoki poprzez określanie funkcji pythonowych do uruchomienia.

Grupy punktów wejścia, takie jak console_scripts, wskazują na obiekty
z podobnymi interfejsami. Aplikacja może używać grupy do znalezienia
swoich wtyczek, lub wielu grup, jeśli używa wtyczek różnych rodzajów.

Moduł entrypoints zawiera funkcje pomagające znajdować i ładować
punkty wejścia.

%package apidocs
Summary:	API documentation for Python entrypoints module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona entrypoints
Group:		Documentation

%description apidocs
API documentation for Python entrypoints module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona entrypoints.

%prep
%setup -q -n entrypoints-%{version}
%patch0 -p1

%build
%if %{with python2}
%py_build

%if %{with tests}
%{__python} -m pytest tests
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
%{__python3} -m pytest tests
%endif
%endif

%if %{with doc}
%{__make} -C doc html
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py_sitescriptdir}/entrypoints.py[co]
%{py_sitescriptdir}/entrypoints-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-entrypoints
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py3_sitescriptdir}/entrypoints.py
%{py3_sitescriptdir}/__pycache__/entrypoints.cpython-*.py[co]
%{py3_sitescriptdir}/entrypoints-%{version}-py*.egg-info
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc doc/_build/html/{_static,*.html,*.js}
%endif
