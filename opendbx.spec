#
#  OpenDBX rpm spec file
#
#  By default OpenDBX is build with this backends:
#  - mysql
#  - odbc
#  - pgsql
#  - sqlite3
#  to disable use --without [module-name]
#
#  Optional supported backends are:
#  - firebird
#  - mssql
#  - oracle
#  - sqlite
#  - sybase
#  to enable use --with [module-name]
#

%if 0%{?_with_firebird:1}
  %define build_firebird 1
%endif
%if 0%{!?_without_firebird:1} && 0%{?fedora} >= 12
  %define build_firebird 1
%endif
%if 0%{!?_without_firebird:1} && 0%{?suse_version} >= 1120
  %define build_firebird 1
%endif

%if 0%{?_with_mssql:1}
  %define build_mssql 1
%endif
%if 0%{!?_without_mssql:1} && 0%{?fedora} >= 9
  %define build_mssql 1
%endif
%if 0%{!?_without_mssql:1} && 0%{?mdkversion} >= 200910
  %define build_mssql 1
%endif

%if 0%{!?_without_mysql:1}
  %define build_mysql 1
%endif

%if 0%{!?_without_odbc:1}
  %define build_odbc 1
%endif

%if 0%{?_with_oracle:1}
  %define build_oracle 1
%endif

%if 0%{!?_without_pgsql:1}
  %define build_pgsql 1
%endif

%if 0%{?_with_sqlite:1}
  %define build_sqlite 1
%endif

%if 0%{!?_without_sqlite3:1}
  %define build_sqlite3 1
%endif

%if 0%{?_with_sybase:1}
  %define build_sybase 1
%endif
%if 0%{!?_without_sybase:1} && 0%{?fedora} >= 9
  %define build_mssql 1
%endif
%if 0%{!?_without_sybase:1} && 0%{?mdkversion} >= 200910
  %define build_mssql 1
%endif

%define major 1
%define libname %mklibname %{name} %{major}
%define libplus %mklibname %{name}plus %{major}
%define devname %mklibname %{name} -d

Summary:	Unified database layer with a clean and lightweight interface
Name:		opendbx
Version:	1.4.6
Release:	125
Group:		Databases
License:	LGPL+
Url:		http://www.linuxnetworks.de/opendbx/download/
Source0:	http://linuxnetworks.de/opendbx/download/%{name}-%{version}.tar.gz
Source100:	%{name}.rpmlintrc
Patch1:		opendbx-1.4.6-doxygen1.8.8.patch
BuildRequires:	docbook2x
BuildRequires:	doxygen
BuildRequires:	gcc-c++
BuildRequires:	gettext
BuildRequires:	gettext-devel
BuildRequires:	readline-devel	
BuildRequires:	pkgconfig(ncurses)

%description
OpenDBX provides a clean and lightweight API for interfacing native relational
database APIs in a consistent way. By using the OpenDBX API you don't have to
adapt your program to the different database APIs by yourself.

%package i18n
Summary:	Translation files for %{name}
Group:		System/Internationalization
BuildArch:	noarch
Conflicts:	%{name} < 1.4.6-3

%description i18n
This package includes the translation files for %{name}.

%package utils
Summary:	Utility application for manipulating database content
Group:		Databases
Provides:	%{name} = %{version}-%{release}
Requires:	readline
Requires:	ncurses

%description utils
Utility application for manipulating database content either interactively by
the user or in batch mode.

%package -n %{libname}
Summary:	Shared library for OpenDBX
Group:		System/Libraries
Requires:	%{name}-i18n = %{version}-%{release}
Obsoletes:	%{name} < 1.4.6-3

%description -n %{libname}
The package contains a shared library for %{name}.

%package -n %{libplus}
Summary:	Shared library for OpenDBX
Group:		System/Libraries
Conflicts:	%{name} < 1.4.6-3

%description -n %{libplus}
The package contains a shared library for %{name}.

%package -n %{devname}
Summary:	OpenDBX development headers
Group:		Databases
Requires:	%{libname} = %{version}-%{release}
Requires:	%{libplus} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{name}-devel < 1.4.6-3

%description -n %{devname}
Header files for the OpenDBX database abstraction library.

%if 0%{?build_firebird:1}
%package firebird
Summary:	Firebird/Interbase backend for OpenDBX
Group:		Databases
Requires:	%{name}-utils = %{version}-%{release}
Requires:	firebird
BuildRequires:	firebird-devel

%description firebird
Firebird/Interbase backend for the OpenDBX database abstraction library.
%endif

%if 0%{?build_mssql:1}
%package mssql
Summary:	MS SQL Server backend for OpenDBX
Group:		Databases
Requires:	%{name}-utils = %{version}-%{release}
Requires:	freetds
BuildRequires:	freetds-devel

%description mssql
MS SQL Server backend for the OpenDBX database abstraction library.
%endif

%if 0%{?build_mysql:1}
%package mysql
Summary:	MySQL backend for OpenDBX
Group:		Databases
Requires:	%{name}-utils = %{version}-%{release}
Requires:	mysql
BuildRequires:	mysql-devel

%description mysql
MySQL backend for the OpenDBX database abstraction library.
%endif

%if 0%{?build_odbc:1}
%package odbc
Summary:	ODBC backend for OpenDBX
Group:		Databases
Requires:	%{name}-utils = %{version}-%{release}
Requires:	unixODBC
BuildRequires:	unixODBC-devel

%description odbc
ODBC backend for the OpenDBX database abstraction library.
%endif

%if 0%{?build_oracle:1}
%package oracle
Summary:	Oracle backend for OpenDBX
Group:		Databases
Requires:	%{name}-utils = %{version}-%{release}

%description oracle
Oracle ctlib backend for the OpenDBX database abstraction library.
%endif

%if 0%{?build_pgsql:1}
%package pgsql
Summary:	PostgreSQL backend for OpenDBX
Group:		Databases
Requires:	%{name}-utils = %{version}-%{release}
Requires:	postgresql
BuildRequires:	postgresql-devel

%description pgsql
PostgreSQL backend for the OpenDBX database abstraction library.
%endif

%if 0%{?build_sqlite:1}
%package sqlite
Summary:	SQLite backend for OpenDBX
Group:		Databases
Requires:	%{name}-utils = %{version}-%{release}
Requires:	sqlite < 3.0
BuildRequires:	sqlite-devel < 3.0

%description sqlite
SQLite backend for the OpenDBX database abstraction library.
%endif

%if 0%{?build_sqlite3:1}
%package sqlite3
Summary:	SQLite3 backend for OpenDBX
Group:		Databases
Requires:	%{name}-utils = %{version}-%{release}
Requires:	sqlite3-tools
BuildRequires:	pkgconfig(sqlite3)

%description sqlite3
SQLite3 backend for the OpenDBX database abstraction library.
%endif

%if 0%{?build_sybase:1}
%package sybase
Summary:	Sybase backend for OpenDBX
Group:		Databases
Requires:	%{name}-utils = %{version}-%{release}
Requires:	freetds
BuildRequires:	freetds-devel

%description sybase
Sybase ctlib backend for the OpenDBX database abstraction library.
%endif

%prep
%setup -q
%autopatch -p1

# fix build with doxygen 1.8.8, needs a suffix on the name to calculate the correct parser
pushd lib/opendbx
ln -s api api.dox
popd

autoreconf -i

%build
CPPFLAGS="%{!?_without_mysql:-I/usr/include/mysql} %{!?_without_pgsql:-I/usr/include/pgsql}"; export CPPFLAGS;
LDFLAGS="-L/lib64 %{!?_without_mysql:-L/usr/lib/mysql -L/usr/lib64/mysql}"; export LDFLAGS;

%configure \
	--with-backends="\
	%{?build_firebird:firebird }\
	%{?build_mssql:mssql }\
	%{?build_mysql:mysql }\
	%{?build_odbc:odbc }\
	%{?build_oracle:oracle }\
	%{?build_pgsql:pgsql }\
	%{?build_sqlite:sqlite }\
	%{?build_sqlite3:sqlite3 }\
	%{?build_sybase:sybase }\
	"

%make

%install
%makeinstall_std
%find_lang %{name}
%find_lang %{name}-utils

%files i18n -f %{name}.lang

%files -n %{libname}
%{_libdir}/libopendbx.so.%{major}*
%dir %{_libdir}/opendbx

%files -n %{libplus}
%{_libdir}/libopendbxplus.so.%{major}*

%files utils -f %{name}-utils.lang
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%{_bindir}/odbx-sql
%{_mandir}/man1/odbx-sql.*
%{_datadir}/%{name}/keywords

%files -n %{devname}
%{_includedir}/odbx.h
%{_includedir}/opendbx
%{_libdir}/libopendbx.so
%{_libdir}/libopendbxplus.so
%{_libdir}/pkgconfig/opendbx.pc
%{_libdir}/pkgconfig/opendbxplus.pc
%{_mandir}/man3/odb*.*
%{_mandir}/man3/Open*.*

%if 0%{?build_firebird:1}
%files firebird
%{_libdir}/opendbx/libfirebirdbackend.so*
%endif

%if 0%{?build_mssql:1}
%files mssql
%{_libdir}/opendbx/libmssqlbackend.so*
%endif

%if 0%{?build_mysql:1}
%files mysql
%{_libdir}/opendbx/libmysqlbackend.so*
%endif

%if 0%{?build_odbc:1}
%files odbc
%{_libdir}/opendbx/libodbcbackend.so*
%endif

%if 0%{?build_oracle:1}
%files oracle
%{_libdir}/opendbx/liboraclebackend.so*
%endif

%if 0%{?build_pgsql:1}
%files pgsql
%{_libdir}/opendbx/libpgsqlbackend.so*
%endif

%if 0%{?build_sqlite:1}
%files sqlite
%{_libdir}/opendbx/libsqlitebackend.so*
%endif

%if 0%{?build_sqlite3:1}
%files sqlite3
%{_libdir}/opendbx/libsqlite3backend.so*
%endif

%if 0%{?build_sybase:1}
%files sybase
%{_libdir}/opendbx/libsybasebackend.so*
%endif

