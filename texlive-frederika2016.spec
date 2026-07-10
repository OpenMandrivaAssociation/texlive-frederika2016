%global tl_name frederika2016
%global tl_revision 42157

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.000.2016.initial.release
Release:	%{tl_revision}.1
Summary:	An OpenType Greek calligraphy font
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/frederika2016
License:	ofl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/frederika2016.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/frederika2016.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Frederika2016 is an attempt to digitize Hermann Zapf's Frederika font.
The font is the Greek companion of Virtuosa by the same designer. This
font is a calligraphy font and this is an initial release.

