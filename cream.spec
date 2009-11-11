Summary:	User-friendly face for Vim
Summary(pl.UTF-8):	Przyjazny dla użytkownika interfejs do Vima
Name:		cream
Version:	0.42
Release:	1
License:	GPL v2
Group:		Applications/Editors/Vim
Source0:	http://dl.sourceforge.net/cream/%{name}-%{version}.tar.gz
# Source0-md5:	3a9a51c58b005a6466f3f70e015da38b
Source1:	%{name}.sh
Source2:	%{name}.desktop
URL:		http://cream.sourceforge.net/
Requires:	gvim
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cream is a modeless GUIification of Vim. Cream includes all the
features of Vim plus many custom utilities. A short list of features
includes syntax highlighting, spell check, multi-file find/replace,
bookmarking, function prototype popups, macros, auto-wrapping,
reformatting, justification, time/date stamps, file explorer,
completion, sorting, calendar, tag navigation, block commenting,
Microsoft, Unix and Apple format text editing, virtually unlimited
file sizes, 38 varieties of 8-bit, 2-byte, and Unicode support,
single/multiple document modes, unlimited undo/redo, show invisible
characters, word count, and more.

%description -l pl.UTF-8
Cream to pozbawione trybów ubranie Vima w graficzny interfejs
użytkownika. Zawiera wszystkie możliwości Vima z dodatkiem wielu
własnych narzędzi. Skrócona lista możliwości obejmuje podświetlanie
składni, sprawdzanie pisowni, wyszukiwanie i zastępowanie ciągów w
wielu plikach, zakładki, podpowiedzi prototypów funkcji, makra,
automatyczne zawijanie, reformatowanie, justowanie, znaczniki czasowe,
eksplorator plików, dopełnianie, sortowanie, kalendarz, nawigację po
znacznikach, komentowanie bloków, edycję tekstu w formacie Microsoftu,
uniksowym i Apple'a, praktycznie nieograniczone rozmiary plików, 38
wariacji kodowań 8-bitowych, 2-bajtowych i unikodowych, tryby pracy
jedno- i wielodokumentowy, nieograniczone undo/redo, pokazywanie
niewidocznych znaków, liczenie słów...

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/vim/cream/{addons,bitmaps,docs,docs-html,filetypes,help},%{_pixmapsdir}}
cp -a creamrc $RPM_BUILD_ROOT%{_datadir}/vim/cream
cp -a *.vim $RPM_BUILD_ROOT%{_datadir}/vim/cream
cp -a addons/*.vim $RPM_BUILD_ROOT%{_datadir}/vim/cream/addons
cp -a bitmaps/*.bmp $RPM_BUILD_ROOT%{_datadir}/vim/cream/bitmaps
cp -a bitmaps/*.xpm $RPM_BUILD_ROOT%{_datadir}/vim/cream/bitmaps
cp -a docs/*.txt $RPM_BUILD_ROOT%{_datadir}/vim/cream/docs
cp -a docs-html/*.html $RPM_BUILD_ROOT%{_datadir}/vim/cream/docs-html
##cp -a docs-html/*.css $RPM_BUILD_ROOT%{_datadir}/vim/cream/docs-html
cp -a docs-html/*.png $RPM_BUILD_ROOT%{_datadir}/vim/cream/docs-html
cp -a filetypes/*.vim $RPM_BUILD_ROOT%{_datadir}/vim/cream/filetypes
cp -a help/*.txt $RPM_BUILD_ROOT%{_datadir}/vim/cream/help

install -d $RPM_BUILD_ROOT%{_bindir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/%{name}

install -d $RPM_BUILD_ROOT%{_desktopdir}
cp -a %{SOURCE2} $RPM_BUILD_ROOT%{_desktopdir}

# icons
install %{name}.png $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.png

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/vim/%{name}
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
