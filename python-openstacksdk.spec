# Copyright 2024 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: python-openstacksdk
Epoch: 100
Version: 3.3.0
Release: 1%{?dist}
BuildArch: noarch
Summary: An SDK for building applications to work with OpenStack
License: Apache-2.0
URL: https://github.com/openstack/openstacksdk/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
openstacksdk is a client library for building applications to work with
OpenStack clouds. The project aims to provide a consistent and complete
set of interactions with OpenStack's many services, along with complete
documentation, examples, and tools.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-openstacksdk
Summary: An SDK for building applications to work with OpenStack
Requires: python3
Requires: python3-cryptography >= 2.7
Requires: python3-decorator >= 4.4.1
Requires: python3-dogpile.cache >= 0.6.5
Requires: python3-iso8601 >= 0.1.11
Requires: python3-jmespath >= 0.9.0
Requires: python3-jsonpatch >= 1.16
Requires: python3-keystoneauth1 >= 3.18.0
Requires: python3-netifaces >= 0.10.4
Requires: python3-os-service-types >= 1.7.0
Requires: python3-pbr >= 2.0.0
Requires: python3-platformdirs >= 3
Requires: python3-PyYAML >= 3.13
Requires: python3-requestsexceptions >= 1.2.0
Provides: python3-openstacksdk = %{epoch}:%{version}-%{release}
Provides: python3dist(openstacksdk) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-openstacksdk = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(openstacksdk) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-openstacksdk = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(openstacksdk) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-openstacksdk
openstacksdk is a client library for building applications to work with
OpenStack clouds. The project aims to provide a consistent and complete
set of interactions with OpenStack's many services, along with complete
documentation, examples, and tools.

%files -n python%{python3_version_nodots}-openstacksdk
%license LICENSE
%{python3_sitelib}/*
%endif

%if 0%{?sle_version} > 150000
%package -n python3-openstacksdk
Summary: An SDK for building applications to work with OpenStack
Requires: python3
Requires: python3-cryptography >= 2.7
Requires: python3-decorator >= 4.4.1
Requires: python3-dogpile.cache >= 0.6.5
Requires: python3-iso8601 >= 0.1.11
Requires: python3-jmespath >= 0.9.0
Requires: python3-jsonpatch >= 1.16
Requires: python3-keystoneauth1 >= 3.18.0
Requires: python3-netifaces >= 0.10.4
Requires: python3-os-service-types >= 1.7.0
Requires: python3-pbr >= 2.0.0
Requires: python3-platformdirs >= 3
Requires: python3-PyYAML >= 3.13
Requires: python3-requestsexceptions >= 1.2.0
Provides: python3-openstacksdk = %{epoch}:%{version}-%{release}
Provides: python3dist(openstacksdk) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-openstacksdk = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(openstacksdk) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-openstacksdk = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(openstacksdk) = %{epoch}:%{version}-%{release}

%description -n python3-openstacksdk
openstacksdk is a client library for building applications to work with
OpenStack clouds. The project aims to provide a consistent and complete
set of interactions with OpenStack's many services, along with complete
documentation, examples, and tools.

%files -n python3-openstacksdk
%license LICENSE
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?sle_version} > 150000)
%package -n python3-openstacksdk
Summary: An SDK for building applications to work with OpenStack
Requires: python3
Requires: python3-cryptography >= 2.7
Requires: python3-decorator >= 4.4.1
Requires: python3-dogpile.cache >= 0.6.5
Requires: python3-iso8601 >= 0.1.11
Requires: python3-jmespath >= 0.9.0
Requires: python3-jsonpatch >= 1.16
Requires: python3-keystoneauth1 >= 3.18.0
Requires: python3-netifaces >= 0.10.4
Requires: python3-os-service-types >= 1.7.0
Requires: python3-pbr >= 2.0.0
Requires: python3-platformdirs >= 3
Requires: python3-pyyaml >= 3.13
Requires: python3-requestsexceptions >= 1.2.0
Provides: python3-openstacksdk = %{epoch}:%{version}-%{release}
Provides: python3dist(openstacksdk) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-openstacksdk = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(openstacksdk) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-openstacksdk = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(openstacksdk) = %{epoch}:%{version}-%{release}

%description -n python3-openstacksdk
openstacksdk is a client library for building applications to work with
OpenStack clouds. The project aims to provide a consistent and complete
set of interactions with OpenStack's many services, along with complete
documentation, examples, and tools.

%files -n python3-openstacksdk
%license LICENSE
%{python3_sitelib}/*
%endif

%changelog
