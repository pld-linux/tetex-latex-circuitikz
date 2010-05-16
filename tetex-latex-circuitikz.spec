
%define short_name circuitikz
%define	texhash	[ ! -x %{_bindir}/texhash ] || %{_bindir}/texhash 1>&2 ;

Summary:	CircuiTikz is a set of LaTeX macros designed to make it easy to draw electrical networks in scientific publications
Summary(hu.UTF-8):	A CircuiTikz LaTeX makrók gyűjteménye, amelyek elektromos hálózatok könnyű rajzolására készült.
Name:		tetex-latex-%{short_name}
Version:	0.1.1
Release:	1
License:	LaTeX Project Public License
Group:		Applications/Publishing/TeX
URL:		http://home.dei.polimi.it/mredaelli/circuitikz/index.html
Source0:	http://home.dei.polimi.it/mredaelli/downloads/circuitikz.zip
# Source0-md5:	04c429a958182eaf00d45dddd341c02a
BuildRequires:	unzip
Requires(post,postun):	/usr/bin/texhash
Requires:	tetex-latex
Requires:	tetex-pgf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CircuiTikz is a set of LaTeX macros designed to make it easy to draw
electrical networks in scientific publications.

%description -l hu.UTF-8
A CircuiTikz Latex makrók gyűjteménye, amelyek elektromos hálózatok
könnyű rajzolására készült.

%prep
%setup -q -n %{short_name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/texmf/tex/latex/%{short_name}

install *.sty $RPM_BUILD_ROOT%{_datadir}/texmf/tex/latex/%{short_name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%texhash

%postun
%texhash

%files
%defattr(644,root,root,755)
%doc CHANGELOG README
%{_datadir}/texmf/tex/latex/%{short_name}
