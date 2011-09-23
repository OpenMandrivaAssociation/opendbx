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


Name:    opendbx
Version:    1.4.5
Release:    46.7
Summary:    Unified database layer with a clean and lightweight interface
Summary(de.UTF-8):    Bibliothek zum Zugriff auf Datenbanken über eine einheitliche Schnittstelle
Summary(pl.UTF-8):    Rozszerzana biblioteka dostępu do baz danych
Group:    Databases
License:    LGPL
URL:    http://www.linuxnetworks.de/opendbx/download/
Source0:    %{name}-%{version}.tar.gz
BuildRoot:    %{_tmppath}/%{name}-%{version}-build
BuildRequires:    gcc-c++, gettext, gettext-devel

%description
OpenDBX provides a clean and lightweight API for interfacing native relational
database APIs in a consistent way. By using the OpenDBX API you don't have to
adapt your program to the different database APIs by yourself.

%description -l de.UTF-8
OpenDBX ist eine schlanke und einfach zu verwendende Bibliothek, die es
ermöglicht verschiedene Datenbankserver über eine konsistente Schnittstelle
anzusprechen.

%description -l pl.UTF-8
OpenDBX to skrajnie lekka, ale rozszerzalna biblioteka dostępu do baz
danych napisana w C. Udostępnia warstwę abstrakcji dla wszystkich
obsługiwanych baz danych w jednym, przejrzystym i prostym interfejsie
automatycznie prowadzącym do eleganckiego projektu kodu. Jest to
odpowiednia biblioteka, aby małym nakładem pracy aplikacja obsługiwała
różne bazy danych.


%package -n utils
Summary:    Utility application for manipulating database content
Summary(de.UTF-8):    Hilfswerkzeuge für die Manipulation von Datenbankinhalten
Group:    Databases
Requires:    %{name} >= %{version}
Requires:    readline, ncurses
BuildRequires:    gcc-c++, gettext, readline, readline-devel, ncurses, ncurses-devel

%description -n utils
Utility application for manipulating database content either interactively by
the user or in batch mode.

%description -n utils -l de.UTF-8
Hilfswerkzeuge für die Manipulation von Datenbankinhalten, entweder interaktiv
durch den Benutzer oder im Stapelbetrieb durch ein anderes Programm.


%package -n devel
Summary:    OpenDBX development headers
Summary(de.UTF-8):    Entwicklungsschnittstellen für OpenDBX
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki OpenDBX
Group:    Databases
Requires:    %{name} = %{version}-%{release}
Requires:    pkgconfig
BuildRequires: doxygen

%description -n devel
Header files for the OpenDBX database abstraction library

%description -n devel -l de.UTF-8
Schnittstellen der OpenDBX Datenbankbibliothek zur Softwareentwicklung

%description -n devel -l pl.UTF-8
Pliki nagłówkowe biblioteki opendbx.


%if 0%{?build_firebird:1}

%package -n firebird
Summary:    Firebird/Interbase backend for OpenDBX
Summary(de.UTF-8):    Firebird/Interbase Unterstützung für OpenDBX
Summary(pl.UTF-8):	Backend bazy danych Firebird dla biblioteki OpenDBX
Group:    Databases
Requires:    %{name} = %{version}-%{release}
Requires:    firebird
BuildRequires:    firebird-devel

%description -n firebird
Firebird/Interbase backend for the OpenDBX database abstraction library

%description -n firebird -l de.UTF-8
Firebird/Interbase Unterstützung für die OpenDBX Datenbankbibliothek

%description -n firebird -l pl.UTF-8
Backend bazy danych Firebird dla biblioteki opendbx.

%endif


%if 0%{?build_mssql:1}

%package -n mssql
Summary:    MS SQL Server backend for OpenDBX
Summary(de.UTF-8):    MS SQL Server Unterstützung für OpenDBX
Summary(pl.UTF-8):	Backend bazy danych MS SQL dla biblioteki OpenDBX
Group:    Databases
Requires:    %{name} = %{version}-%{release}
Requires:    freetds
BuildRequires:    freetds-devel

%description -n mssql
MS SQL Server backend for the OpenDBX database abstraction library

%description -n mssql -l de.UTF-8
MS SQL Server Unterstützung für die OpenDBX Datenbankbibliothek

%description -n mssql -l pl.UTF-8
Backend bazy danych MS SQL dla biblioteki opendbx.

%endif


%if 0%{?build_mysql:1}

%package -n mysql
Summary:    MySQL backend for OpenDBX
Summary(de.UTF-8):    MySQL Unterstützung für OpenDBX
Summary(pl.UTF-8):	Backend bazy danych MySQL dla biblioteki OpenDBX
Group:    Databases
Requires:    %{name} = %{version}-%{release}
Requires:    mysql
BuildRequires:    mysql-devel

%description -n mysql
MySQL backend for the OpenDBX database abstraction library

%description -n mysql -l de.UTF-8
MySQL Unterstützung für die OpenDBX Datenbankbibliothek

%description -n mysql -l pl.UTF-8
Backend bazy danych MySQL dla biblioteki opendbx.

%endif


%if 0%{?build_odbc:1}

%package -n odbc
Summary:    ODBC backend for OpenDBX
Summary(de.UTF-8):    ODBC Unterstützung für OpenDBX
Summary(pl.UTF-8):	Backend bazy danych ODBC dla biblioteki OpenDBX
Group:    Databases
Requires:    %{name} = %{version}-%{release}
Requires:    unixODBC
BuildRequires:    unixODBC-devel

%description -n odbc
ODBC backend for the OpenDBX database abstraction library

%description -n odbc -l de.UTF-8
ODBC Unterstützung für die OpenDBX Datenbankbibliothek

%description -n odbc -l pl.UTF-8
Backend bazy danych ODBC dla biblioteki opendbx.

%endif


%if 0%{?build_oracle:1}

%package -n oracle
Summary:    Oracle backend for OpenDBX
Summary(de.UTF-8):    Oracle Unterstützung für OpenDBX
Summary(pl.UTF-8):	Backend bazy danych Oracle dla biblioteki OpenDBX
Group:    Databases
Requires:    %{name} = %{version}-%{release}

%description -n oracle
Oracle ctlib backend for the OpenDBX database abstraction library

%description -n oracle -l de.UTF-8
Oracle Unterstützung für die OpenDBX Datenbankbibliothek

%description -n oracle -l pl.UTF-8
Backend bazy danych Oracle dla biblioteki OpenDBX.

%endif


%if 0%{?build_pgsql:1}

%package -n pgsql
Summary:    PostgreSQL backend for OpenDBX
Summary(de.UTF-8):    PostgreSQL Unterstützung für OpenDBX
Summary(pl.UTF-8):	Backend bazy danych PostgreSQL dla biblioteki OpenDBX
Group:    Databases
Requires:    %{name} = %{version}-%{release}
Requires:    postgresql
BuildRequires:    postgresql-devel

%description -n pgsql
PostgreSQL backend for the OpenDBX database abstraction library

%description -n pgsql -l de.UTF-8
PostgreSQL Unterstützung für die OpenDBX Datenbankbibliothek

%description -n pgsql -l pl.UTF-8
Backend bazy danych PostgreSQL dla biblioteki opendbx.

%endif


%if 0%{?build_sqlite:1}

%package -n sqlite
Summary:    SQLite backend for OpenDBX
Summary(de.UTF-8):    SQLite Unterstützung für OpenDBX
Summary(pl.UTF-8):	Backend bazy danych SQLite dla biblioteki OpenDBX
Group:    Databases
Requires:    %{name} = %{version}-%{release}
Requires:    sqlite < 3.0
BuildRequires:    sqlite-devel < 3.0

%description -n sqlite
SQLite backend for the OpenDBX database abstraction library

%description -n sqlite -l de.UTF-8
Sqlite Unterstützung für die OpenDBX Datenbankbibliothek

%description -n sqlite -l pl.UTF-8
Backend bazy danych sqlite dla biblioteki opendbx.

%endif


%if 0%{?build_sqlite3:1}

%package -n sqlite3
Summary:    SQLite3 backend for OpenDBX
Summary(de.UTF-8):    SQLite3 Unterstützung für OpenDBX
Summary(pl.UTF-8):	Backend bazy danych SQLite3 dla biblioteki OpenDBX
Group:    Databases
Requires:    %{name} = %{version}-%{release}
%if 0%{?mandriva_version}
Requires:    sqlite3-tools
BuildRequires: sqlite3-devel
%else
Requires:    sqlite >= 3.0
BuildRequires: sqlite-devel >= 3.0
%endif

%description -n sqlite3
SQLite3 backend for the OpenDBX database abstraction library

%description -n sqlite3 -l de.UTF-8
Sqlite3 Unterstützung für die OpenDBX Datenbankbibliothek

%description -n sqlite3 -l pl.UTF-8
Backend bazy danych sqlite3 dla biblioteki opendbx.

%endif


%if 0%{?build_sybase:1}

%package -n sybase
Summary:    Sybase backend for OpenDBX
Summary(de.UTF-8):    Sybase Unterstützung für OpenDBX
Summary(pl.UTF-8):	Backend bazy danych Sybase dla biblioteki OpenDBX
Group:    Databases
Requires:    %{name} = %{version}-%{release}
Requires:    freetds
BuildRequires:    freetds-devel

%description -n sybase
Sybase ctlib backend for the OpenDBX database abstraction library

%description -n sybase -l de.UTF-8
Sybase Unterstützung für die OpenDBX Datenbankbibliothek

%description -n sybase -l pl.UTF-8
Backend bazy danych sybase dla biblioteki opendbx.

%endif


%prep


%setup -q -n opendbx-%{version}


%build
CPPFLAGS="%{!?_without_mysql:-I/usr/include/mysql} %{!?_without_pgsql:-I/usr/include/pgsql}"; export CPPFLAGS;
LDFLAGS="-L/lib64 %{!?_without_mysql:-L/usr/lib/mysql -L/usr/lib64/mysql}"; export LDFLAGS;
autoreconf -i
%configure \
    --disable-rpath \
    --disable-static \
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
" || cat config.log

%{__make} %{?_smp_mflags}


%install
%{__make} DESTDIR=%{buildroot} install
rm %{buildroot}%{_libdir}/lib*.*a
rm %{buildroot}%{_libdir}/opendbx/lib*.*a
%find_lang %{name}
%find_lang %{name}-utils


%clean
if test "%{buildroot}" != "/"; then rm -rf %{buildroot}; fi


%post -p /sbin/ldconfig


%postun -p /sbin/ldconfig


%files -f %{name}.lang
%defattr(-,root,root,-)
%{_libdir}/libopendbx.so.*
%{_libdir}/libopendbxplus.so.*
%dir %{_libdir}/opendbx
%doc AUTHORS COPYING ChangeLog NEWS README TODO


%files utils -f %{name}-utils.lang
%defattr(-,root,root,-)
%{_bindir}/odbx-sql
%{_datadir}/%{name}
%{_datadir}/%{name}/keywords
#%{_mandir}/man1/*


%files devel
%defattr(-,root,root,-)
%{_includedir}/odbx.h
%{_includedir}/opendbx
%{_includedir}/opendbx/api*
%{_libdir}/libopendbx.so
%{_libdir}/libopendbxplus.so
%{_libdir}/pkgconfig/opendbx.pc
%{_libdir}/pkgconfig/opendbxplus.pc
#%{_mandir}/man3/*


%if 0%{?build_firebird:1}
%files firebird
%defattr(-,root,root,-)
%{_libdir}/opendbx/libfirebirdbackend.so*
%endif


%if 0%{?build_mssql:1}
%files mssql
%defattr(-,root,root,-)
%{_libdir}/opendbx/libmssqlbackend.so*
%endif


%if 0%{?build_mysql:1}
%files mysql
%defattr(-,root,root,-)
%{_libdir}/opendbx/libmysqlbackend.so*
%endif


%if 0%{?build_odbc:1}
%files odbc
%defattr(-,root,root,-)
%{_libdir}/opendbx/libodbcbackend.so*
%endif


%if 0%{?build_oracle:1}
%files oracle
%defattr(-,root,root,-)
%{_libdir}/opendbx/liboraclebackend.so*
%endif


%if 0%{?build_pgsql:1}
%files pgsql
%defattr(-,root,root,-)
%{_libdir}/opendbx/libpgsqlbackend.so*
%endif


%if 0%{?build_sqlite:1}
%files sqlite
%defattr(-,root,root,-)
%{_libdir}/opendbx/libsqlitebackend.so*
%endif


%if 0%{?build_sqlite3:1}
%files sqlite3
%defattr(-,root,root,-)
%{_libdir}/opendbx/libsqlite3backend.so*
%endif


%if 0%{?build_sybase:1}
%files sybase
%defattr(-,root,root,-)
%{_libdir}/opendbx/libsybasebackend.so*
%endif


