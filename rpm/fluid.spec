# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.26
# 

Name:       fluid

# >> macros
# << macros

Summary:    fluid package
Version:    0.2.0.20140101.e9ea587
Release:    1
Group:      Applications/System
License:    BSD
Source0:    fluid-%{version}.tar.bz2
Source100:  fluid.yaml
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  cmake
BuildRequires:  python
BuildRequires:  bzip2-devel

%description
A package of fluid functions

%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
cd upstream
# << build pre

%cmake .  \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo

make %{?jobs:-j%jobs}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
cd upstream
# << install pre
%make_install

# >> install post
# << install post

%files
%defattr(-,root,root,-)
%{_libdir}/hawaii/qml/Fluid/
# >> files
# << files
