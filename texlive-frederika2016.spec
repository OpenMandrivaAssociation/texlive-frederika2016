Name:		texlive-frederika2016
Version:	42157
Release:	2
Summary:	An OpenType Greek calligraphy font
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/frederika2016
License:	ofl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/frederika2016.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/frederika2016.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Frederika2016 is an attempt to digitize Hermann Zapf's
Frederika font. The font is the Greek companion of Virtuosa by
the same designer. This font is a calligraphy font and this is
an initial release.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/fonts/opentype/public/frederika2016
%doc %{_texmfdistdir}/doc/fonts/frederika2016

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
