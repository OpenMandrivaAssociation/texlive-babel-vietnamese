# revision 30578
# category Package
# catalog-ctan /macros/latex/contrib/babel-contrib/vietnamese
# catalog-date 2013-05-20 00:05:10 +0200
# catalog-license lppl1.3
# catalog-version 1.3
Name:		texlive-babel-vietnamese
Version:	1.3
Release:	9
Summary:	Babel support for typesetting Vietnamese
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/babel-contrib/vietnamese
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-vietnamese.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-vietnamese.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides the language definition file for support
of Vietnamese in babel.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/babel-vietnamese/vietnam.ldf
%{_texmfdistdir}/tex/generic/babel-vietnamese/vietnamese.ldf
#- source
%doc %{_texmfdistdir}/source/generic/babel-vietnamese/vietnamese.dtx
%doc %{_texmfdistdir}/source/generic/babel-vietnamese/vietnamese.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex source %{buildroot}%{_texmfdistdir}
