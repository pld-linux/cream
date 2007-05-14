Summary:	User-friendly face for Vim
Name:		cream
Version:	0.38
Release:	0.1
Source0:	http://dl.sourceforge.net/cream/%{name}-%{version}.tar.gz
# Source0-md5:	3415244ec2d58139063d8ab2604d3bb6
License:	GPL v2
Group:		Applications/Editors/Vim
URL:		http://cream.sourceforge.net/
BuildRequires:	ImageMagick
BuildRequires:	desktop-file-utils
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

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/vim/cream/{addons,bitmaps,docs,docs-html,filetypes,help,spelldicts},%{_pixmapsdir}}
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
cp -a spelldicts/cream-spell-dict-eng-s*.vim $RPM_BUILD_ROOT%{_datadir}/vim/cream/spelldicts
cp -a spelldicts/cream-spell-dict.vim $RPM_BUILD_ROOT%{_datadir}/vim/cream/spelldicts

install -d $RPM_BUILD_ROOT%{_bindir}
cp -a cream $RPM_BUILD_ROOT%{_bindir}

install -d $RPM_BUILD_ROOT%{_desktopdir}
cp -a cream.desktop $RPM_BUILD_ROOT%{_desktopdir}

# menu
desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="TextEditor" \
  --dir $RPM_BUILD_ROOT%{_desktopdir} $RPM_BUILD_ROOT%{_desktopdir}/*

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
