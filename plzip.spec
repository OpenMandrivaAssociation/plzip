Name:		plzip
Summary:	Multi-threaded LZMA archiver
Version:	1.8
Release:	1
License:	GPLv3+
Group:		Archiving/Compression
URL:		https://www.nongnu.org/lzip/plzip.html
Source0:	http://download.savannah.gnu.org/releases/lzip/%{name}-%{version}.tar.gz
BuildRequires:	lzip
BuildRequires:	lzlib-devel

%description
Plzip is a massively parallel (multi-threaded), lossless data compressor based
on the LZMA algorithm, with very safe integrity checking and a user interface
similar to the one of gzip or bzip2. Plzip uses the lzip file format; the files
produced by plzip are fully compatible with lzip-1.4 or newer, and can be
rescued with lziprecover.

Plzip is intended for faster compression/decompression of big files
on multiprocessor machines, which makes it specially well suited
for distribution of big software files and large scale data archiving. On files
big enough, plzip can use hundreds of processors.

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install

%files
%{_bindir}/plzip
%{_mandir}/man1/plzip.1*
%{_infodir}/plzip.info*
%doc AUTHORS ChangeLog NEWS README
