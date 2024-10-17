%define module	imdb
%define oname	IMDbPY

Summary:	Python module for the IMDb movie database
Name:		python-%{module}
Version:	4.9
Release:	2
License:	GPLv2+
Group:		Development/Python
Source:		https://sourceforge.net/projects/imdbpy/files/IMDbPY/4.9/IMDbPY-%{version}.tar.gz
URL:		https://imdbpy.sourceforge.net/
BuildRequires:	python-devel
BuildRequires:	python-setuptools

%description
IMDbPY is a Python package useful to retrieve and manage the data of
the IMDb movie database.

IMDbPY is mainly a tool intended for programmers and developers, but
some example scripts are included.

%prep
%setup -q -n %{oname}-%{version}
chmod -x docs/*.ico

%build
python setup.py build

%install
python setup.py install --skip-build --root %{buildroot}
# Move doc files to correct place
mv %{buildroot}/usr/doc %{buildroot}/%{py_puresitedir}/imdb/
mv %{buildroot}/usr/etc %{buildroot}/%{py_puresitedir}/imdb/

%clean

%files
%{_bindir}/*.py
%ifarch x86_64
%{py_puresitedir}/imdb/
%endif
%{py_platsitedir}/*
