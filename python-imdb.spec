%define module	imdb
%define name	python-%{module}
%define oname	IMDbPY
%define version	3.9
%define rel	3

Summary:	Python module for the IMDb movie database
Name:		%{name}
Version:	%{version}
Release:	%mkrel %{rel}
License:	GPLv2+
Group:		Development/Python
Source:		http://downloads.sourceforge.net/imdbpy/%{oname}-%{version}.tar.gz
URL:		http://imdbpy.sourceforge.net/
BuildRequires:	python-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}

%description
IMDbPY is a Python package useful to retrieve and manage the data of
the IMDb movie database.

IMDbPY is mainly a tool intended for programmers and developers, but
some example scripts are included.

%prep
%setup -q -n %{oname}-%{version}
chmod -x docs/*.ico

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install \
	--root=%{buildroot} \
	--optimize=2

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc docs/*
%{_bindir}/*.py
%{py_platsitedir}/*
